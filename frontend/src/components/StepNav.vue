<template>
  <div class="step-nav">
    <button
      v-for="step in steps"
      :key="step.num"
      class="step-pill"
      :class="{
        active: step.num === currentStep,
        available: step.available,
        disabled: !step.available
      }"
      :title="step.available ? `Go to ${step.label}` : `${step.label} not available`"
      @click="step.available && navigate(step)"
    >
      <span class="pill-num">{{ step.num }}</span>
      <span class="pill-label">{{ step.label }}</span>
    </button>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  currentStep: { type: Number, required: true },
  projectId:   { type: String, default: null },
  simulationId:{ type: String, default: null },
  reportId:    { type: String, default: null },
})

const router = useRouter()

const steps = computed(() => [
  {
    num: 1,
    label: 'Graph',
    available: !!props.projectId,
    route: props.projectId ? { name: 'Process', params: { projectId: props.projectId } } : null,
  },
  {
    num: 2,
    label: 'Env Setup',
    available: !!props.simulationId,
    route: props.simulationId ? { name: 'Simulation', params: { simulationId: props.simulationId } } : null,
  },
  {
    num: 3,
    label: 'Simulation',
    available: !!props.simulationId,
    route: props.simulationId ? { name: 'SimulationRun', params: { simulationId: props.simulationId } } : null,
  },
  {
    num: 4,
    label: 'Report',
    available: !!props.reportId,
    route: props.reportId ? { name: 'Report', params: { reportId: props.reportId } } : null,
  },
  {
    num: 5,
    label: 'Interact',
    available: !!props.reportId,
    route: props.reportId ? { name: 'Interaction', params: { reportId: props.reportId } } : null,
  },
])

const navigate = (step) => {
  if (step.route && step.num !== props.currentStep) {
    router.push(step.route)
  }
}
</script>

<style scoped>
.step-nav {
  display: flex;
  align-items: center;
  gap: 4px;
}

.step-pill {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: 4px;
  border: 1px solid transparent;
  background: transparent;
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.step-pill.disabled {
  color: #444;
  border-color: #2a2a2a;
  cursor: default;
}

.step-pill.available {
  color: #888;
  border-color: #3a3a3a;
}

.step-pill.available:hover {
  color: #ccc;
  border-color: #666;
  background: #1a1a1a;
}

.step-pill.active {
  color: #fff;
  border-color: #666;
  background: #222;
}

.pill-num {
  font-size: 10px;
  color: #555;
  font-weight: 600;
}

.step-pill.active .pill-num {
  color: #aaa;
}

.step-pill.available:not(.active):hover .pill-num {
  color: #888;
}

.pill-label {
  font-size: 11px;
}
</style>
