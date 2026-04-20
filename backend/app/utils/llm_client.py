"""
LLM Client Wrapper
Unified API calls supporting OpenAI, Anthropic (native SDK), and Ollama.
- Anthropic: uses the native anthropic SDK for full max_tokens support
- Ollama: uses OpenAI-compatible SDK with num_ctx injection
- Others: standard OpenAI-compatible SDK
"""

import json
import os
import re
from typing import Optional, Dict, Any, List
import httpx
from openai import OpenAI

from ..config import Config


class LLMClient:
    """LLM Client"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        timeout: float = 300.0
    ):
        self.api_key = api_key or Config.LLM_API_KEY
        self.base_url = base_url or Config.LLM_BASE_URL
        self.model = model or Config.LLM_MODEL_NAME
        self.timeout = timeout

        if not self.api_key:
            raise ValueError("LLM_API_KEY not configured")

        verify_ssl = os.environ.get('LLM_VERIFY_SSL', 'true').lower() != 'false'

        # Anthropic: initialise native SDK client
        if self._is_anthropic():
            from anthropic import Anthropic
            self._anthropic_client = Anthropic(
                api_key=self.api_key,
                timeout=timeout,
                http_client=httpx.Client(verify=verify_ssl),
            )
            self.client = None
        else:
            self._anthropic_client = None
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
                timeout=timeout,
                http_client=httpx.Client(verify=verify_ssl),
            )

        # Ollama context window size — prevents prompt truncation.
        # Read from env OLLAMA_NUM_CTX, default 8192 (Ollama default is only 2048).
        self._num_ctx = int(os.environ.get('OLLAMA_NUM_CTX', '8192'))

    def _is_ollama(self) -> bool:
        """Check if we're talking to an Ollama server."""
        return '11434' in (self.base_url or '')

    def _is_anthropic(self) -> bool:
        """Check if we're talking to Anthropic's API."""
        return 'anthropic.com' in (self.base_url or '')

    def _chat_anthropic(
        self,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int,
        json_mode: bool = False
    ) -> str:
        """Send request via native Anthropic SDK."""
        # Separate system message from conversation messages
        system_content = ""
        conversation = []
        for msg in messages:
            if msg["role"] == "system":
                system_content = msg["content"]
            else:
                conversation.append({"role": msg["role"], "content": msg["content"]})

        kwargs = dict(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=conversation,
        )
        if system_content:
            kwargs["system"] = system_content

        response = self._anthropic_client.messages.create(**kwargs)
        return response.content[0].text

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        Send chat request

        Args:
            messages: Message list
            temperature: Temperature parameter
            max_tokens: Max token count
            response_format: Response format (e.g., JSON mode)

        Returns:
            Model response text
        """
        if self._is_anthropic():
            content = self._chat_anthropic(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                json_mode=(response_format is not None),
            )
            content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
            return content

        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        if response_format:
            kwargs["response_format"] = response_format

        # For Ollama: pass num_ctx via extra_body to prevent prompt truncation
        if self._is_ollama() and self._num_ctx:
            kwargs["extra_body"] = {
                "options": {"num_ctx": self._num_ctx}
            }

        response = self.client.chat.completions.create(**kwargs)
        content = response.choices[0].message.content
        # Some models (like MiniMax M2.5) include <think>thinking content in response, need to remove
        content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
        return content

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        Send chat request and return JSON

        Args:
            messages: Message list
            temperature: Temperature parameter
            max_tokens: Max token count

        Returns:
            Parsed JSON object
        """
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        # Clean markdown code block markers
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            # Try to extract the outermost JSON object in case of trailing garbage
            match = re.search(r'\{[\s\S]*\}', cleaned_response)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    pass
            raise ValueError(f"Invalid JSON format from LLM: {cleaned_response}")
