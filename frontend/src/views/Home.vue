<template>
  <div class="home-container">
    <!-- Top Navigation Bar -->
    <nav class="navbar">
      <div class="nav-brand">MIROFISH OFFLINE</div>
      <div class="nav-links">
        <a href="https://github.com/levilniAtBain/MiroFish-Offline" target="_blank" class="github-link">
          Visit our Github <span>↗</span>
        </a>
      </div>
    </nav>

    <div class="main-content">

      <!-- ── INTRO HEADER ─────────────────────────────────── -->
      <section class="intro-section">
        <div class="intro-top">
          <div class="logo-cluster">
            <img src="../assets/logo/MiroFish_logo_compressed.jpeg" alt="MiroFish" class="miro-logo" />
            <div class="logo-sep"></div>
            <div class="bain-logo">BAIN</div>
          </div>
          <span class="version-chip">v0.1-preview · Offline Edition</span>
        </div>

        <p class="intro-desc">
          MiroFish extracts <strong>reality seeds</strong> from any document and runs a fully offline
          <strong>multi-agent social simulation</strong> — predicting opinion dynamics, emergent behaviour,
          and social cascades entirely on your machine. No cloud. No data leaves your environment.
        </p>

        <!-- ── COLLAPSIBLE CARDS ───────────────────────────── -->
        <div class="accordion">

          <!-- 1. History -->
          <div class="acc-item" :class="{ open: open.has('history') }">
            <button class="acc-header" @click="toggle('history')">
              <span class="acc-arrow">{{ open.has('history') ? '−' : '+' }}</span>
              <span class="acc-label">History of MiroFish</span>
            </button>
            <div class="acc-body">
              <p><strong>MiroFish</strong> was created by <strong>Guo Hangjiang</strong> (known as "Baifu"), a 20-year-old senior at Beijing University of Posts and Telecommunications. His first project, <em>BettaFish</em> — a multi-agent sentiment analysis tool — hit #1 on GitHub's global trending list in late 2024 with 20 000 stars in a single week.</p>
              <p>That momentum caught the attention of <strong>Chen Tianqiao</strong>, founder of Shanda Group and former richest man in China, who invited Guo for an internship with full creative freedom. Using <em>"vibe coding"</em> powered by AI assistants (including Claude Code), Guo built MiroFish from scratch in just <strong>ten days</strong> in early 2026. He sent a demo video to Chen Tianqiao the same evening — and within 24 hours, Shanda committed <strong>¥30 million (~$4.1M)</strong> in seed funding. Guo went from intern to CEO overnight.</p>
              <p>MiroFish topped GitHub's global trending list on <strong>March 7, 2026</strong>, accumulating 33 000+ stars and nearly 1 900 forks within days. It is built on the <strong>OASIS</strong> multi-agent framework by CAMEL-AI, capable of simulating up to one million agents with 23 types of social interactions.</p>
              <p class="history-bain-note"><strong>This edition</strong> is an adapted offline fork developed at <strong>Bain &amp; Company</strong> — re-architected for full air-gap operation with Neo4j, Ollama/Anthropic, and a consulting-grade report layer, so sensitive client data never leaves the analyst's machine.</p>
            </div>
          </div>

          <!-- 2. What it does -->
          <div class="acc-item" :class="{ open: open.has('what') }">
            <button class="acc-header" @click="toggle('what')">
              <span class="acc-arrow">{{ open.has('what') ? '−' : '+' }}</span>
              <span class="acc-label">What MiroFish does</span>
            </button>
            <div class="acc-body">
              <ul class="feature-list">
                <li><span class="feat-tag">EXTRACT</span> Reads PDF, MD, TXT documents and builds a knowledge graph of entities and relationships using Neo4j + GraphRAG.</li>
                <li><span class="feat-tag">PERSONA</span> Generates diverse AI agent profiles (up to 100+) from the graph — each with an MBTI, profession, interests, and social media habits.</li>
                <li><span class="feat-tag">SIMULATE</span> Runs a 72-hour parallel Twitter + Reddit simulation where agents post, comment, like, repost, and interact autonomously.</li>
                <li><span class="feat-tag">ANALYSE</span> A dedicated Report Agent synthesises every action into a structured prediction report with scenario analysis.</li>
                <li><span class="feat-tag">INTERACT</span> Chat live with any simulated individual or with the Report Agent to probe the findings further.</li>
              </ul>
            </div>
          </div>

          <!-- 3. Architecture -->
          <div class="acc-item" :class="{ open: open.has('arch') }">
            <button class="acc-header" @click="toggle('arch')">
              <span class="acc-arrow">{{ open.has('arch') ? '−' : '+' }}</span>
              <span class="acc-label">Architecture</span>
            </button>
            <div class="acc-body arch-body">
              <div class="arch-diagram">
                <!-- Layer labels -->
                <div class="arch-layer-label top">Input</div>
                <div class="arch-layer-label mid">Processing</div>
                <div class="arch-layer-label bot">Output</div>

                <!-- Nodes -->
                <div class="arch-nodes">
                  <div class="arch-node input">
                    <div class="node-icon">📄</div>
                    <div class="node-label">Documents</div>
                    <div class="node-sub">PDF · MD · TXT</div>
                  </div>

                  <div class="arch-connector">
                    <div class="conn-line">
                      <span class="data-dot d1"></span>
                      <span class="data-dot d2"></span>
                    </div>
                    <div class="conn-label">GraphRAG</div>
                  </div>

                  <div class="arch-node proc">
                    <div class="node-icon">🕸</div>
                    <div class="node-label">Neo4j Graph</div>
                    <div class="node-sub">Entities · Relations</div>
                  </div>

                  <div class="arch-connector">
                    <div class="conn-line">
                      <span class="data-dot d3"></span>
                      <span class="data-dot d4"></span>
                    </div>
                    <div class="conn-label">LLM profiling</div>
                  </div>

                  <div class="arch-node proc">
                    <div class="node-icon">🤖</div>
                    <div class="node-label">Agent Pool</div>
                    <div class="node-sub">OASIS · 100+ agents</div>
                  </div>

                  <div class="arch-connector">
                    <div class="conn-line">
                      <span class="data-dot d5"></span>
                      <span class="data-dot d6"></span>
                    </div>
                    <div class="conn-label">Simulation</div>
                  </div>

                  <div class="arch-node proc">
                    <div class="node-icon">📊</div>
                    <div class="node-label">Action Log</div>
                    <div class="node-sub">Posts · Reactions</div>
                  </div>

                  <div class="arch-connector">
                    <div class="conn-line">
                      <span class="data-dot d7"></span>
                      <span class="data-dot d8"></span>
                    </div>
                    <div class="conn-label">Analysis</div>
                  </div>

                  <div class="arch-node output">
                    <div class="node-icon">📝</div>
                    <div class="node-label">Report + Chat</div>
                    <div class="node-sub">Insights · Predictions</div>
                  </div>
                </div>

                <!-- Tech stack badges -->
                <div class="arch-stack">
                  <span class="stack-badge">Neo4j</span>
                  <span class="stack-badge">OASIS</span>
                  <span class="stack-badge">Claude / Ollama</span>
                  <span class="stack-badge">Flask</span>
                  <span class="stack-badge">Vue 3</span>
                  <span class="stack-badge">Docker</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 4. How it works -->
          <div class="acc-item" :class="{ open: open.has('how') }">
            <button class="acc-header" @click="toggle('how')">
              <span class="acc-arrow">{{ open.has('how') ? '−' : '+' }}</span>
              <span class="acc-label">How it works — the agentic pipeline</span>
            </button>
            <div class="acc-body">
              <div class="steps-pipeline">
                <div v-for="step in howSteps" :key="step.num" class="how-step">
                  <div class="step-num">{{ step.num }}</div>
                  <div class="step-content">
                    <div class="step-title">{{ step.title }}</div>
                    <div class="step-desc">{{ step.desc }}</div>
                  </div>
                  <div v-if="step.num < 5" class="step-arrow">→</div>
                </div>
              </div>
              <div class="agentic-note">
                <span class="note-tag">AGENTIC LOOP</span>
                Each round, every agent independently decides its action (post / react / idle) guided by its memory, persona, and the current social context — no scripted behaviour, fully emergent dynamics.
              </div>
            </div>
          </div>

          <!-- 5. GitHub -->
          <div class="acc-item" :class="{ open: open.has('github') }">
            <button class="acc-header" @click="toggle('github')">
              <span class="acc-arrow">{{ open.has('github') ? '−' : '+' }}</span>
              <span class="acc-label">Repositories</span>
            </button>
            <div class="acc-body">
              <div class="link-cards">
                <a href="https://github.com/levilniAtBain/MiroFish-Offline" target="_blank" class="link-card primary">
                  <span class="link-icon">🏦</span>
                  <div>
                    <div class="link-title">MiroFish Offline — Bain fork</div>
                    <div class="link-sub">levilniAtBain/MiroFish-Offline</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://github.com/nikmcfly/MiroFish-Offline" target="_blank" class="link-card">
                  <span class="link-icon">🐟</span>
                  <div>
                    <div class="link-title">MiroFish Offline — Official</div>
                    <div class="link-sub">nikmcfly/MiroFish-Offline</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://github.com/camel-ai/oasis" target="_blank" class="link-card">
                  <span class="link-icon">🌊</span>
                  <div>
                    <div class="link-title">OASIS Multi-Agent Framework</div>
                    <div class="link-sub">camel-ai/oasis</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
              </div>
            </div>
          </div>

          <!-- 6. Articles & Videos -->
          <div class="acc-item" :class="{ open: open.has('media') }">
            <button class="acc-header" @click="toggle('media')">
              <span class="acc-arrow">{{ open.has('media') ? '−' : '+' }}</span>
              <span class="acc-label">Articles &amp; Videos</span>
            </button>
            <div class="acc-body">
              <div class="media-section-label">Videos</div>
              <div class="link-cards">
                <a href="https://www.youtube.com/watch?v=5SSGximONlY" target="_blank" class="link-card">
                  <span class="link-icon">▶</span>
                  <div>
                    <div class="link-title">The First Open Source Swarm Intelligence Engine</div>
                    <div class="link-sub">YouTube · overview &amp; demo</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://www.youtube.com/watch?v=dbITcA6sRNo" target="_blank" class="link-card">
                  <span class="link-icon">▶</span>
                  <div>
                    <div class="link-title">MiroFish AI Explained: The Multi-Agent Engine</div>
                    <div class="link-sub">YouTube · architecture deep-dive</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://www.youtube.com/watch?v=UXlMVSsVhzU" target="_blank" class="link-card">
                  <span class="link-icon">▶</span>
                  <div>
                    <div class="link-title">Agent Swarms, GraphRAG &amp; Deterministic Bots</div>
                    <div class="link-sub">YouTube · technical breakdown</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://www.youtube.com/watch?v=ISulTJ51Sdc" target="_blank" class="link-card">
                  <span class="link-icon">▶</span>
                  <div>
                    <div class="link-title">"God's Eye AI" Simulates Thousands of Buyers</div>
                    <div class="link-sub">YouTube · market &amp; business angle</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
              </div>
              <div class="media-section-label" style="margin-top:16px">Articles</div>
              <div class="link-cards">
                <a href="https://theophilelafargue.substack.com/p/mirofish-or-the-mirror-that-thinks" target="_blank" class="link-card">
                  <span class="link-icon">📝</span>
                  <div>
                    <div class="link-title">The Mirror That Thinks — on Emergence &amp; Prediction</div>
                    <div class="link-sub">Substack · philosophical analysis</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://agentnativedev.medium.com/mirofish-swarm-intelligence-with-1m-agents-that-can-predict-everything-114296323663" target="_blank" class="link-card">
                  <span class="link-icon">📝</span>
                  <div>
                    <div class="link-title">Swarm Intelligence with 1M Agents</div>
                    <div class="link-sub">Medium · technical overview</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://medium.com/@shubhjain191/mirofish-the-god-view-engine-8151f96a40f6" target="_blank" class="link-card">
                  <span class="link-icon">📝</span>
                  <div>
                    <div class="link-title">MiroFish: The God View Engine</div>
                    <div class="link-sub">Medium · product perspective</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
                <a href="https://www.linkedin.com/pulse/swarm-intelligence-comes-forecasting-how-mirofish-simulates-borish-lahve" target="_blank" class="link-card">
                  <span class="link-icon">📝</span>
                  <div>
                    <div class="link-title">Swarm Intelligence Comes to Forecasting</div>
                    <div class="link-sub">LinkedIn · business use cases</div>
                  </div>
                  <span class="link-arrow">↗</span>
                </a>
              </div>
            </div>
          </div>

          <!-- 7. Bain Use Cases -->
          <div class="acc-item" :class="{ open: open.has('bain') }">
            <button class="acc-header" @click="toggle('bain')">
              <span class="acc-arrow">{{ open.has('bain') ? '−' : '+' }}</span>
              <span class="acc-label">Bain use cases</span>
            </button>
            <div class="acc-body">
              <p>MiroFish turns any client document into a <strong>synthetic stakeholder panel</strong> — letting Bain teams stress-test strategies, messages, and decisions against realistic simulated reactions before a single slide is shared externally.</p>
              <div class="bain-usecases">
                <div class="buc-card">
                  <div class="buc-icon">📢</div>
                  <div class="buc-title">Comms &amp; Message Testing</div>
                  <div class="buc-desc">Run an announcement (restructuring, M&amp;A, price change) through thousands of simulated employees, customers, or investors. Identify which segments react positively/negatively before the real release.</div>
                </div>
                <div class="buc-card">
                  <div class="buc-icon">🗳</div>
                  <div class="buc-title">Policy &amp; Regulatory Impact</div>
                  <div class="buc-desc">Simulate how different stakeholder communities respond to regulatory proposals or policy shifts — useful for government affairs, public sector, and ESG workstreams.</div>
                </div>
                <div class="buc-card">
                  <div class="buc-icon">🛍</div>
                  <div class="buc-title">Consumer &amp; Market Research</div>
                  <div class="buc-desc">Replace or augment focus groups: generate diverse consumer personas from brand or category documents and observe emergent opinion dynamics on product launches or repositioning.</div>
                </div>
                <div class="buc-card">
                  <div class="buc-icon">⚙</div>
                  <div class="buc-title">Change Management</div>
                  <div class="buc-desc">Model employee reactions to a transformation programme. Identify resistance hotspots by role, tenure, or MBTI profile before the change roadmap is locked.</div>
                </div>
                <div class="buc-card">
                  <div class="buc-icon">🌐</div>
                  <div class="buc-title">Geopolitical &amp; Competitive Scenarios</div>
                  <div class="buc-desc">Probe how industry or political actors might respond to a client's strategic move — useful in M&amp;A due diligence, market entry, and competitor playbook workstreams.</div>
                </div>
                <div class="buc-card">
                  <div class="buc-icon">🔒</div>
                  <div class="buc-title">Fully Confidential</div>
                  <div class="buc-desc">All simulations run locally — client documents, personas, and results never leave your machine. Fully compliant with Bain data security requirements.</div>
                </div>
              </div>
            </div>
          </div>

          <!-- 8. Tips -->
          <div class="acc-item" :class="{ open: open.has('tips') }">
            <button class="acc-header" @click="toggle('tips')">
              <span class="acc-arrow">{{ open.has('tips') ? '−' : '+' }}</span>
              <span class="acc-label">Tips for usage</span>
            </button>
            <div class="acc-body">
              <div class="tips-grid">
                <div class="tip-card" v-for="tip in tips" :key="tip.title">
                  <div class="tip-icon">{{ tip.icon }}</div>
                  <div class="tip-title">{{ tip.title }}</div>
                  <div class="tip-desc">{{ tip.desc }}</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ── DASHBOARD: UPLOAD CONSOLE ──────────────────────── -->
      <section class="dashboard-section">
        <div class="console-box">
          <div class="console-section">
            <div class="console-header">
              <span>01 / Reality Seeds</span>
              <span>Supported: PDF, MD, TXT</span>
            </div>
            <div
              class="upload-zone"
              @dragover.prevent="handleDragOver"
              @dragleave.prevent="handleDragLeave"
              @drop.prevent="handleDrop"
              @click="triggerFileInput"
            >
              <input ref="fileInput" type="file" multiple accept=".pdf,.md,.txt" @change="handleFileSelect" style="display: none" :disabled="loading" />
              <div v-if="files.length === 0" class="upload-placeholder">
                <div class="upload-icon">↑</div>
                <div class="upload-title">Drag &amp; drop files here</div>
                <div class="upload-hint">or click to browse</div>
              </div>
              <div v-else class="file-list">
                <div v-for="(file, index) in files" :key="index" class="file-item">
                  <span>📄</span>
                  <span class="file-name">{{ file.name }}</span>
                  <button @click.stop="removeFile(index)" class="remove-btn">×</button>
                </div>
              </div>
            </div>
          </div>

          <div class="console-divider"><span class="console-divider-text">Parameters</span></div>

          <div class="console-section">
            <div class="console-header">
              <span>>_ 02 / Simulation Prompt</span>
            </div>
            <div class="input-wrapper">
              <textarea v-model="formData.simulationRequirement" class="code-input" placeholder="// Describe your simulation or prediction goal in natural language" rows="6" :disabled="loading"></textarea>
              <div class="model-badge">Engine: Claude / Ollama + Neo4j (local)</div>
            </div>
          </div>

          <div class="btn-section">
            <button class="start-btn" @click="startSimulation" :disabled="!canSubmit || loading">
              <span v-if="!loading">Start Engine</span>
              <span v-else>Initializing...</span>
              <span>→</span>
            </button>
          </div>
        </div>
      </section>

      <HistoryDatabase />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'

const router = useRouter()

// Accordion state
const open = reactive(new Set())
const toggle = (id) => {
  if (open.has(id)) open.delete(id)
  else open.add(id)
}

// How it works steps
const howSteps = [
  { num: 1, title: 'Graph Build', desc: 'Extract entities & relations from documents into Neo4j using GraphRAG.' },
  { num: 2, title: 'Env Setup', desc: 'LLM generates 100+ diverse agent personas grounded in the graph.' },
  { num: 3, title: 'Simulation', desc: 'OASIS runs 72-hour parallel Twitter + Reddit with full agent autonomy.' },
  { num: 4, title: 'Report', desc: 'Report Agent synthesises every action into a structured prediction.' },
  { num: 5, title: 'Interact', desc: 'Chat with any agent or the Report Agent to probe the findings.' },
]

const tips = [
  { icon: '📑', title: 'Document quality matters', desc: 'Rich, specific source documents produce more realistic agent behaviours. Include diverse stakeholder perspectives.' },
  { icon: '🎯', title: 'Precise prompt, precise results', desc: 'The simulation prompt should specify the scenario clearly — who is affected, what the trigger event is, what you want to understand.' },
  { icon: '⏱', title: 'Rounds vs depth', desc: 'More rounds → longer simulation but richer emergent dynamics. 48–72 hours of simulated time (≈ 48–72 rounds) is a good default.' },
  { icon: '🤖', title: 'Agent count', desc: 'Start with 20–40 agents for quick tests. 80–100 agents for production-quality results (takes 10–30 min).' },
  { icon: '💬', title: 'Use the chat', desc: 'After simulation, interview specific agents to understand WHY they reacted as they did — this is often more valuable than the report alone.' },
  { icon: '🔁', title: 'Iterate', desc: 'Re-use the same graph with different simulation prompts to compare scenarios. Only Step 3 needs to re-run.' },
]

// Upload form
const formData = ref({ simulationRequirement: '' })
const files = ref([])
const loading = ref(false)
const isDragOver = ref(false)
const fileInput = ref(null)

const canSubmit = computed(() => formData.value.simulationRequirement.trim() !== '' && files.value.length > 0)

const triggerFileInput = () => { if (!loading.value) fileInput.value?.click() }
const handleFileSelect = (e) => addFiles(Array.from(e.target.files))
const handleDragOver = () => { isDragOver.value = true }
const handleDragLeave = () => { isDragOver.value = false }
const handleDrop = (e) => { isDragOver.value = false; addFiles(Array.from(e.dataTransfer.files)) }

const addFiles = (newFiles) => {
  const valid = newFiles.filter(f => ['.pdf', '.md', '.txt'].some(ext => f.name.toLowerCase().endsWith(ext)))
  files.value = [...files.value, ...valid]
}

const removeFile = (i) => files.value.splice(i, 1)

const startSimulation = () => {
  if (!canSubmit.value || loading.value) return
  import('../store/pendingUpload.js').then(({ setPendingUpload }) => {
    setPendingUpload(files.value, formData.value.simulationRequirement)
    router.push({ name: 'Process', params: { projectId: 'new' } })
  })
}
</script>

<style scoped>
/* ── Base ───────────────────────────────────────────────── */
.home-container {
  min-height: 100vh;
  background: #fff;
  font-family: 'Space Grotesk', 'Noto Sans SC', system-ui, sans-serif;
}

/* ── Navbar ─────────────────────────────────────────────── */
.navbar {
  height: 56px;
  background: #000;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
}

.nav-brand {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  letter-spacing: 1px;
  font-size: 1.1rem;
}

.github-link {
  color: #fff;
  text-decoration: none;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 6px;
  opacity: 0.7;
  transition: opacity 0.2s;
}
.github-link:hover { opacity: 1; }

/* ── Main content wrapper ───────────────────────────────── */
.main-content {
  max-width: 1100px;
  margin: 0 auto;
  padding: 48px 40px 80px;
}

/* ── Intro section ──────────────────────────────────────── */
.intro-section {
  margin-bottom: 60px;
}

.intro-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.logo-cluster {
  display: flex;
  align-items: center;
  gap: 20px;
}

.miro-logo {
  height: 48px;
  width: auto;
  object-fit: contain;
}

.logo-sep {
  width: 1px;
  height: 32px;
  background: #ddd;
}

.bain-logo {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.5rem;
  font-weight: 900;
  color: #CC0000;
  letter-spacing: 3px;
}

.version-chip {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #999;
  border: 1px solid #E5E5E5;
  padding: 4px 10px;
  border-radius: 20px;
}

.intro-desc {
  font-size: 1.05rem;
  color: #444;
  line-height: 1.75;
  max-width: 820px;
  margin: 0 0 32px 0;
  border-left: 3px solid #FF4500;
  padding-left: 16px;
}

.intro-desc strong { color: #000; }

/* ── Accordion ──────────────────────────────────────────── */
.accordion {
  display: flex;
  flex-direction: column;
  border: 1px solid #E5E5E5;
  border-radius: 4px;
  overflow: hidden;
}

.acc-item {
  border-bottom: 1px solid #E5E5E5;
}
.acc-item:last-child { border-bottom: none; }

.acc-header {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 20px;
  background: #FAFAFA;
  border: none;
  cursor: pointer;
  text-align: left;
  transition: background 0.15s;
  font-family: 'JetBrains Mono', monospace;
}
.acc-header:hover { background: #F0F0F0; }
.acc-item.open .acc-header { background: #F5F5F5; }

.acc-arrow {
  font-size: 1.1rem;
  color: #FF4500;
  font-weight: 700;
  width: 16px;
  text-align: center;
  flex-shrink: 0;
}

.acc-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #111;
  letter-spacing: 0.3px;
}

.acc-body {
  display: none;
  padding: 20px 24px 24px;
  background: #fff;
  font-size: 0.92rem;
  color: #444;
  line-height: 1.7;
}
.acc-item.open .acc-body { display: block; }

.acc-body p { margin: 0 0 12px 0; }
.history-bain-note { border-left: 3px solid #CC0000; padding-left: 12px; background: rgba(204,0,0,0.04); border-radius: 0 4px 4px 0; }
.acc-body p:last-child { margin: 0; }

/* Feature list */
.feature-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.feature-list li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.feat-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  font-weight: 700;
  background: #000;
  color: #fff;
  padding: 2px 6px;
  border-radius: 2px;
  flex-shrink: 0;
  margin-top: 3px;
  letter-spacing: 0.5px;
}

/* ── Architecture diagram ───────────────────────────────── */
.arch-body { overflow-x: auto; }

.arch-diagram {
  min-width: 700px;
  padding: 16px 0 24px;
}

.arch-nodes {
  display: flex;
  align-items: center;
  gap: 0;
  margin-bottom: 20px;
}

.arch-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 14px 16px;
  border: 1.5px solid #E0E0E0;
  border-radius: 6px;
  min-width: 110px;
  background: #fff;
  transition: border-color 0.2s, box-shadow 0.2s;
  position: relative;
}

.arch-node:hover {
  border-color: #000;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.arch-node.input  { border-color: #3B82F6; background: #EFF6FF; }
.arch-node.output { border-color: #10B981; background: #ECFDF5; }
.arch-node.proc   { border-color: #E0E0E0; }

.node-icon  { font-size: 1.6rem; line-height: 1; }
.node-label { font-size: 0.78rem; font-weight: 700; color: #111; text-align: center; }
.node-sub   { font-family: 'JetBrains Mono', monospace; font-size: 0.6rem; color: #888; text-align: center; }

/* Animated connectors */
.arch-connector {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  flex: 1;
  min-width: 60px;
}

.conn-line {
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #E0E0E0, #E0E0E0);
  position: relative;
  overflow: hidden;
}

.data-dot {
  position: absolute;
  top: -3px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #FF4500;
  animation: flow 2s linear infinite;
}

.data-dot.d1 { animation-delay: 0s; }
.data-dot.d2 { animation-delay: 1s; }
.data-dot.d3 { animation-delay: 0.3s; }
.data-dot.d4 { animation-delay: 1.3s; }
.data-dot.d5 { animation-delay: 0.6s; }
.data-dot.d6 { animation-delay: 1.6s; }
.data-dot.d7 { animation-delay: 0.9s; }
.data-dot.d8 { animation-delay: 1.9s; }

@keyframes flow {
  0%   { left: -8px; opacity: 0; }
  10%  { opacity: 1; }
  90%  { opacity: 1; }
  100% { left: 100%; opacity: 0; }
}

.conn-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.58rem;
  color: #AAA;
  letter-spacing: 0.3px;
  white-space: nowrap;
}

/* Tech stack badges */
.arch-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 8px;
}

.stack-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  font-weight: 600;
  padding: 3px 10px;
  border: 1px solid #D0D0D0;
  border-radius: 20px;
  color: #555;
  background: #F9F9F9;
}

/* ── How it works ───────────────────────────────────────── */
.steps-pipeline {
  display: flex;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 0;
  margin-bottom: 20px;
}

.how-step {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.step-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.4rem;
  font-weight: 900;
  color: #ECECEC;
  line-height: 1;
  flex-shrink: 0;
}

.step-content {
  flex: 1;
  min-width: 130px;
  max-width: 160px;
  padding-bottom: 4px;
}

.step-title {
  font-weight: 700;
  font-size: 0.85rem;
  color: #111;
  margin-bottom: 4px;
}

.step-desc {
  font-size: 0.78rem;
  color: #666;
  line-height: 1.5;
}

.step-arrow {
  font-size: 1.2rem;
  color: #CCC;
  padding: 0 8px;
  align-self: center;
  flex-shrink: 0;
}

.agentic-note {
  border: 1px solid #FF4500;
  border-left-width: 3px;
  padding: 12px 16px;
  border-radius: 4px;
  background: #FFF8F6;
  font-size: 0.85rem;
  color: #333;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  flex-wrap: wrap;
}

.note-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  font-weight: 700;
  background: #FF4500;
  color: #fff;
  padding: 2px 6px;
  border-radius: 2px;
  flex-shrink: 0;
  margin-top: 2px;
}

/* ── GitHub / Links ─────────────────────────────────────── */
.link-cards {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.link-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 18px;
  border: 1px solid #E5E5E5;
  border-radius: 6px;
  text-decoration: none;
  color: #333;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.link-card:hover {
  border-color: #000;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.link-card.primary {
  border-color: #000;
  background: #FAFAFA;
}

.link-icon { font-size: 1.4rem; }

.link-title {
  font-weight: 600;
  font-size: 0.9rem;
  color: #111;
  margin-bottom: 2px;
}

.link-sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #999;
}

.link-arrow {
  margin-left: auto;
  font-size: 1rem;
  color: #999;
}

/* ── Articles & Media ───────────────────────────────────── */
.media-section-label {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 10px;
}

/* ── Bain Use Cases ─────────────────────────────────────── */
.bain-usecases {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  margin-top: 16px;
}

.buc-card {
  background: #FAFAFA;
  border: 1px solid #E5E5E5;
  border-radius: 6px;
  padding: 16px;
}

.buc-icon { font-size: 1.5rem; margin-bottom: 8px; }
.buc-title { font-weight: 700; font-size: 0.85rem; color: #111; margin-bottom: 6px; }
.buc-desc { font-size: 0.78rem; color: #666; line-height: 1.5; }

.buc-card:last-child {
  border-color: #CC0000;
  background: rgba(204,0,0,0.03);
}

/* ── Tips grid ──────────────────────────────────────────── */
.tips-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.tip-card {
  border: 1px solid #E5E5E5;
  border-radius: 6px;
  padding: 14px 16px;
  background: #FAFAFA;
}

.tip-icon {
  font-size: 1.4rem;
  margin-bottom: 8px;
}

.tip-title {
  font-weight: 700;
  font-size: 0.82rem;
  color: #111;
  margin-bottom: 6px;
}

.tip-desc {
  font-size: 0.78rem;
  color: #666;
  line-height: 1.55;
}

/* ── Dashboard / Upload console ─────────────────────────── */
.dashboard-section {
  border-top: 1px solid #E5E5E5;
  padding-top: 48px;
  margin-bottom: 48px;
}

.console-box {
  border: 1px solid #CCC;
  padding: 8px;
  max-width: 720px;
  margin: 0 auto;
}

.console-section { padding: 20px; }

.console-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #666;
}

.upload-zone {
  border: 1px dashed #CCC;
  height: 180px;
  overflow-y: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: #FAFAFA;
}

.upload-placeholder { text-align: center; }

.upload-icon {
  width: 40px;
  height: 40px;
  border: 1px solid #DDD;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 12px;
  color: #999;
}

.upload-title { font-weight: 500; font-size: 0.9rem; margin-bottom: 4px; }
.upload-hint  { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #999; }

.file-list {
  width: 100%;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-item {
  display: flex;
  align-items: center;
  background: #fff;
  padding: 6px 10px;
  border: 1px solid #EEE;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.82rem;
  gap: 8px;
}

.file-name { flex: 1; }

.remove-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.1rem;
  color: #999;
  line-height: 1;
  padding: 0;
}

.console-divider {
  display: flex;
  align-items: center;
  margin: 4px 0;
  border-top: 1px solid #EEE;
}

.console-divider-text {
  padding: 0 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  color: #BBB;
  letter-spacing: 1px;
}

.input-wrapper {
  position: relative;
  border: 1px solid #DDD;
  background: #FAFAFA;
}

.code-input {
  width: 100%;
  border: none;
  background: transparent;
  padding: 16px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88rem;
  line-height: 1.6;
  resize: vertical;
  outline: none;
  min-height: 130px;
  box-sizing: border-box;
}

.model-badge {
  position: absolute;
  bottom: 8px;
  right: 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  color: #AAA;
}

.btn-section { padding: 0 20px 20px; }

.start-btn {
  width: 100%;
  background: #000;
  color: #fff;
  border: none;
  padding: 18px 24px;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  letter-spacing: 1px;
  transition: background 0.2s;
}

.start-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.start-btn:not(:disabled):hover { background: #222; }

/* ── Responsive ─────────────────────────────────────────── */
@media (max-width: 768px) {
  .main-content { padding: 32px 20px 60px; }
  .tips-grid { grid-template-columns: 1fr 1fr; }
  .steps-pipeline { flex-direction: column; }
  .step-arrow { display: none; }
  .arch-nodes { overflow-x: auto; }
}

@media (max-width: 480px) {
  .tips-grid { grid-template-columns: 1fr; }
  .intro-top { flex-direction: column; align-items: flex-start; gap: 12px; }
}
</style>
