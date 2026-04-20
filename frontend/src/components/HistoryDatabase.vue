<template>
  <div 
    class="history-database"
    :class="{ 'no-projects': projects.length === 0 && !loading }"
    ref="historyContainer"
  >
    <!-- Background decoration: technical grid lines (only shown when there are projects) -->
    <div v-if="projects.length > 0 || loading" class="tech-grid-bg">
      <div class="grid-pattern"></div>
      <div class="gradient-overlay"></div>
    </div>

    <!-- Title section -->
    <div class="section-header">
      <div class="section-line"></div>
      <span class="section-title">Simulation Records</span>
      <div class="section-line"></div>
    </div>

    <!-- List container (only shown when there are projects) -->
    <div v-if="projects.length > 0" class="cards-list">
      <div
        v-for="(project, index) in projects"
        :key="project.simulation_id"
        class="project-row"
        @click="navigateToProject(project)"
      >
        <!-- Left: ID + step status + files -->
        <div class="row-left">
          <div class="row-meta">
            <span class="card-id">{{ formatSimulationId(project.simulation_id) }}</span>
            <div class="card-status-icons">
              <span class="status-icon" :class="{ available: project.project_id, unavailable: !project.project_id }" title="Graph Construction">◇</span>
              <span class="status-icon available" title="Environment Setup">◈</span>
              <span class="status-icon" :class="{ available: project.report_id, unavailable: !project.report_id }" title="Analysis Report">◆</span>
            </div>
          </div>
          <div class="row-files">
            <template v-if="project.files && project.files.length > 0">
              <span v-for="(file, fi) in project.files.slice(0, 3)" :key="fi" class="file-tag" :class="getFileType(file.filename)">{{ getFileTypeLabel(file.filename) }}</span>
              <span v-if="project.files.length > 3" class="files-more">+{{ project.files.length - 3 }}</span>
            </template>
            <span v-else class="empty-file-text">No Files</span>
          </div>
        </div>

        <!-- Center: title + description -->
        <div class="row-center">
          <h3 class="card-title">{{ project.simulation_title || getSimulationTitle(project.simulation_requirement) }}</h3>
          <p class="card-desc">{{ truncateText(project.simulation_requirement, 120) }}</p>
        </div>

        <!-- Right: date, progress, open -->
        <div class="row-right">
          <div class="card-datetime">
            <span class="card-date">{{ formatDate(project.created_at) }}</span>
            <span class="card-time">{{ formatTime(project.created_at) }}</span>
          </div>
          <span class="card-progress" :class="getProgressClass(project)">
            <span class="status-dot">●</span> {{ formatRounds(project) }}
          </span>
          <button class="card-open-btn" @click.stop="quickOpen(project)">Open ↗</button>
        </div>

        <div class="card-bottom-line"></div>
      </div>
    </div>

    <!-- Loading state -->
    <div v-if="loading" class="loading-state">
      <span class="loading-spinner"></span>
      <span class="loading-text">Loading...</span>
    </div>

    <!-- Simulation playback details modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedProject" class="modal-overlay" @click.self="closeModal">
          <div class="modal-content">
            <!-- Modal header -->
            <div class="modal-header">
              <div class="modal-title-section">
                <span class="modal-id">{{ formatSimulationId(selectedProject.simulation_id) }}</span>
                <span class="modal-progress" :class="getProgressClass(selectedProject)">
                  <span class="status-dot">●</span> {{ formatRounds(selectedProject) }}
                </span>
                <span class="modal-create-time">{{ formatDate(selectedProject.created_at) }} {{ formatTime(selectedProject.created_at) }}</span>
              </div>
              <button class="modal-close" @click="closeModal">×</button>
            </div>

            <!-- Modal content -->
            <div class="modal-body">
              <!-- Simulation requirement -->
              <div class="modal-section">
                <div class="modal-label">Simulation Requirement</div>
                <div class="modal-requirement">{{ selectedProject.simulation_requirement || 'None' }}</div>
              </div>

              <!-- File list -->
              <div class="modal-section">
                <div class="modal-label">Associated Files</div>
                <div class="modal-files" v-if="selectedProject.files && selectedProject.files.length > 0">
                  <div v-for="(file, index) in selectedProject.files" :key="index" class="modal-file-item">
                    <span class="file-tag" :class="getFileType(file.filename)">{{ getFileTypeLabel(file.filename) }}</span>
                    <span class="modal-file-name">{{ file.filename }}</span>
                  </div>
                </div>
                <div class="modal-empty" v-else>No Associated Files</div>
              </div>
            </div>

            <!-- Simulation playback divider -->
            <div class="modal-divider">
              <span class="divider-line"></span>
              <span class="divider-text">Simulation Playback</span>
              <span class="divider-line"></span>
            </div>

            <!-- Navigation buttons -->
            <div class="modal-actions">
              <button
                class="modal-btn btn-project"
                @click="goToProject"
                :disabled="!selectedProject.project_id"
              >
                <span class="btn-step">Step 1</span>
                <span class="btn-icon">◇</span>
                <span class="btn-text">Graph Build</span>
              </button>
              <button
                class="modal-btn btn-simulation"
                @click="goToSimulation"
                :disabled="!selectedProject.simulation_id"
              >
                <span class="btn-step">Step 2</span>
                <span class="btn-icon">◈</span>
                <span class="btn-text">Env Setup</span>
              </button>
              <button
                class="modal-btn btn-run"
                @click="goToSimulationRun"
                :disabled="!selectedProject.simulation_id"
              >
                <span class="btn-step">Step 3</span>
                <span class="btn-icon">▶</span>
                <span class="btn-text">Simulation</span>
              </button>
              <button
                class="modal-btn btn-report"
                @click="goToReport"
                :disabled="!selectedProject.report_id"
              >
                <span class="btn-step">Step 4</span>
                <span class="btn-icon">◆</span>
                <span class="btn-text">Report</span>
              </button>
              <button
                class="modal-btn btn-interact"
                @click="goToInteraction"
                :disabled="!selectedProject.report_id"
              >
                <span class="btn-step">Step 5</span>
                <span class="btn-icon">⬡</span>
                <span class="btn-text">Interact</span>
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, onActivated, watch, nextTick } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { getSimulationHistory } from '../api/simulation'

const router = useRouter()
const route = useRoute()

// State
const projects = ref([])
const loading = ref(true)
const historyContainer = ref(null)
const selectedProject = ref(null)

// Get style class based on round progress
const getProgressClass = (simulation) => {
  const current = simulation.current_round || 0
  const total = simulation.total_rounds || 0

  if (total === 0 || current === 0) {
    // Not started
    return 'not-started'
  } else if (current >= total) {
    // Completed
    return 'completed'
  } else {
    // In progress
    return 'in-progress'
  }
}

// Format date (only display date part)
const formatDate = (dateStr) => {
  if (!dateStr) return ''
  try {
    const date = new Date(dateStr)
    return date.toISOString().slice(0, 10)
  } catch {
    return dateStr?.slice(0, 10) || ''
  }
}

// Format time (display hours:minutes)
const formatTime = (dateStr) => {
  if (!dateStr) return ''
  try {
    const date = new Date(dateStr)
    const hours = date.getHours().toString().padStart(2, '0')
    const minutes = date.getMinutes().toString().padStart(2, '0')
    return `${hours}:${minutes}`
  } catch {
    return ''
  }
}

// Truncate text
const truncateText = (text, maxLength) => {
  if (!text) return ''
  return text.length > maxLength ? text.slice(0, maxLength) + '...' : text
}

// Generate title from simulation requirement (first 20 characters)
const getSimulationTitle = (requirement) => {
  if (!requirement) return 'Unnamed Simulation'
  const title = requirement.slice(0, 20)
  return requirement.length > 20 ? title + '...' : title
}

// Format simulation_id display (first 6 characters)
const formatSimulationId = (simulationId) => {
  if (!simulationId) return 'SIM_UNKNOWN'
  const prefix = simulationId.replace('sim_', '').slice(0, 6)
  return `SIM_${prefix.toUpperCase()}`
}

// Format round display (current round/total rounds)
const formatRounds = (simulation) => {
  const current = simulation.current_round || 0
  const total = simulation.total_rounds || 0
  if (total === 0) return 'Not Started'
  return `${current}/${total} rounds`
}

// Get file type (for styling)
const getFileType = (filename) => {
  if (!filename) return 'other'
  const ext = filename.split('.').pop()?.toLowerCase()
  const typeMap = {
    'pdf': 'pdf',
    'doc': 'doc', 'docx': 'doc',
    'xls': 'xls', 'xlsx': 'xls', 'csv': 'xls',
    'ppt': 'ppt', 'pptx': 'ppt',
    'txt': 'txt', 'md': 'txt', 'json': 'code',
    'jpg': 'img', 'jpeg': 'img', 'png': 'img', 'gif': 'img',
    'zip': 'zip', 'rar': 'zip', '7z': 'zip'
  }
  return typeMap[ext] || 'other'
}

// Get file type label text
const getFileTypeLabel = (filename) => {
  if (!filename) return 'FILE'
  const ext = filename.split('.').pop()?.toUpperCase()
  return ext || 'FILE'
}

// Truncate filename (preserve extension)
const truncateFilename = (filename, maxLength) => {
  if (!filename) return 'Unknown File'
  if (filename.length <= maxLength) return filename

  const ext = filename.includes('.') ? '.' + filename.split('.').pop() : ''
  const nameWithoutExt = filename.slice(0, filename.length - ext.length)
  const truncatedName = nameWithoutExt.slice(0, maxLength - ext.length - 3) + '...'
  return truncatedName + ext
}

// Open project details modal
const navigateToProject = (simulation) => {
  selectedProject.value = simulation
}

// Close modal
const closeModal = () => {
  selectedProject.value = null
}

// Navigate to Graph Construction page (Project)
const goToProject = () => {
  if (selectedProject.value?.project_id) {
    router.push({
      name: 'Process',
      params: { projectId: selectedProject.value.project_id }
    })
    closeModal()
  }
}

// Navigate to Environment Setup page (Simulation)
const goToSimulation = () => {
  if (selectedProject.value?.simulation_id) {
    router.push({
      name: 'Simulation',
      params: { simulationId: selectedProject.value.simulation_id }
    })
    closeModal()
  }
}

// Navigate to Analysis Report page (Report)
const goToReport = () => {
  if (selectedProject.value?.report_id) {
    router.push({
      name: 'Report',
      params: { reportId: selectedProject.value.report_id }
    })
    closeModal()
  }
}

// Navigate to Simulation Run page (Step 3)
const goToSimulationRun = () => {
  if (selectedProject.value?.simulation_id) {
    router.push({
      name: 'SimulationRun',
      params: { simulationId: selectedProject.value.simulation_id }
    })
    closeModal()
  }
}

// Navigate to Interaction page (Step 5)
const goToInteraction = () => {
  if (selectedProject.value?.report_id) {
    router.push({
      name: 'Interaction',
      params: { reportId: selectedProject.value.report_id }
    })
    closeModal()
  }
}

// Quick open: jump directly to the most advanced completed step
const quickOpen = (project) => {
  if (project.report_id) {
    router.push({ name: 'Report', params: { reportId: project.report_id } })
  } else if (project.simulation_id) {
    router.push({ name: 'Simulation', params: { simulationId: project.simulation_id } })
  } else if (project.project_id) {
    router.push({ name: 'Process', params: { projectId: project.project_id } })
  }
}

// Load history projects
const loadHistory = async () => {
  try {
    loading.value = true
    const response = await getSimulationHistory(20)
    if (response.success) {
      projects.value = response.data || []
    }
  } catch (error) {
    console.error('Failed to load history projects:', error)
    projects.value = []
  } finally {
    loading.value = false
  }
}

// Watch for route changes and reload data when returning to home page
watch(() => route.path, (newPath) => {
  if (newPath === '/') loadHistory()
})

onMounted(async () => {
  await nextTick()
  await loadHistory()
})

onActivated(() => { loadHistory() })
</script>

<style scoped>
/* Container */
.history-database {
  position: relative;
  width: 100%;
  min-height: 280px;
  margin-top: 40px;
  padding: 35px 0 40px;
  overflow: visible;
}

/* Simplified display when no projects */
.history-database.no-projects {
  min-height: auto;
  padding: 40px 0 20px;
}

/* Technical grid background */
.tech-grid-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  pointer-events: none;
}

/* Use CSS background pattern to create fixed-spacing square grid */
.grid-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image:
    linear-gradient(to right, rgba(0, 0, 0, 0.05) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(0, 0, 0, 0.05) 1px, transparent 1px);
  background-size: 50px 50px;
  /* Position from top-left, height changes extend only to bottom without affecting existing grid */
  background-position: top left;
}

.gradient-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    linear-gradient(to right, rgba(255, 255, 255, 0.9) 0%, transparent 15%, transparent 85%, rgba(255, 255, 255, 0.9) 100%),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.8) 0%, transparent 20%, transparent 80%, rgba(255, 255, 255, 0.8) 100%);
  pointer-events: none;
}

/* Title section */
.section-header {
  position: relative;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  margin-bottom: 24px;
  font-family: 'JetBrains Mono', 'SF Mono', monospace;
  padding: 0 40px;
}

.section-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #E5E7EB, transparent);
  max-width: 300px;
}

.section-title {
  font-size: 0.8rem;
  font-weight: 500;
  color: #9CA3AF;
  letter-spacing: 3px;
  text-transform: uppercase;
}

/* List container */
.cards-list {
  display: flex;
  flex-direction: column;
  gap: 0;
  padding: 0 40px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Project row (list item) */
.project-row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 32px;
  padding: 20px 24px;
  background: #FFFFFF;
  border: 1px solid #E5E7EB;
  border-bottom: none;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease;
  overflow: hidden;
}

.project-row:first-child {
  border-radius: 4px 4px 0 0;
}

.project-row:last-child {
  border-bottom: 1px solid #E5E7EB;
  border-radius: 0 0 4px 4px;
}

.project-row:only-child {
  border-radius: 4px;
  border-bottom: 1px solid #E5E7EB;
}

.project-row:hover {
  background: #FAFAFA;
  border-color: rgba(0, 0, 0, 0.25);
  z-index: 1;
}

/* Row columns */
.row-left {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex-shrink: 0;
  width: 180px;
}

.row-meta {
  display: flex;
  align-items: center;
  gap: 10px;
}

.row-center {
  flex: 1;
  min-width: 0;
}

.row-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
  flex-shrink: 0;
  width: 130px;
}

/* ID */
.card-id {
  font-family: 'JetBrains Mono', 'SF Mono', monospace;
  font-size: 0.72rem;
  color: #6B7280;
  letter-spacing: 0.5px;
  font-weight: 500;
}

/* Feature status icons */
.card-status-icons {
  display: flex;
  align-items: center;
  gap: 5px;
}

.status-icon {
  font-size: 0.75rem;
  transition: all 0.2s ease;
  cursor: default;
}

.status-icon.available { opacity: 1; }
.status-icon:nth-child(1).available { color: #3B82F6; }
.status-icon:nth-child(2).available { color: #F59E0B; }
.status-icon:nth-child(3).available { color: #10B981; }
.status-icon.unavailable { color: #D1D5DB; opacity: 0.5; }

/* Files row */
.row-files {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  align-items: center;
}

.files-more {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6rem;
  color: #9CA3AF;
  padding: 1px 4px;
}

.empty-file-text {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  color: #C4C9D4;
  letter-spacing: 0.3px;
}

/* File tag */
.file-tag {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 18px;
  padding: 0 5px;
  border-radius: 2px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.58rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.2px;
  flex-shrink: 0;
  min-width: 30px;
}

.file-tag.pdf   { background: #f2e6e6; color: #a65a5a; }
.file-tag.doc   { background: #e6eff5; color: #5a7ea6; }
.file-tag.xls   { background: #e6f2e8; color: #5aa668; }
.file-tag.ppt   { background: #f5efe6; color: #a6815a; }
.file-tag.txt   { background: #f0f0f0; color: #757575; }
.file-tag.code  { background: #eae6f2; color: #815aa6; }
.file-tag.img   { background: #e6f2f2; color: #5aa6a6; }
.file-tag.zip   { background: #f2f0e6; color: #a69b5a; }
.file-tag.other { background: #f3f4f6; color: #6b7280; }

/* Card title */
.card-title {
  font-family: 'Inter', -apple-system, sans-serif;
  font-size: 1rem;
  font-weight: 700;
  color: #111827;
  margin: 0 0 6px 0;
  line-height: 1.4;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: color 0.2s ease;
}

.project-row:hover .card-title {
  color: #2563EB;
}

/* Card description */
.card-desc {
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  color: #6B7280;
  margin: 0;
  line-height: 1.55;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Date/time */
.card-datetime {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 2px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  color: #9CA3AF;
}

/* Progress */
.card-progress {
  display: flex;
  align-items: center;
  gap: 5px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.3px;
}

.status-dot { font-size: 0.45rem; }

.card-progress.completed   { color: #10B981; }
.card-progress.in-progress { color: #F59E0B; }
.card-progress.not-started { color: #9CA3AF; }

/* Open button */
.card-open-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  color: #6B7280;
  background: transparent;
  border: 1px solid #E5E7EB;
  border-radius: 3px;
  padding: 4px 10px;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s ease, background 0.2s ease, color 0.2s ease;
}

.project-row:hover .card-open-btn {
  opacity: 1;
}

.card-open-btn:hover {
  background: #000;
  color: #fff;
  border-color: #000;
}

/* Bottom accent line on hover */
.card-bottom-line {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2px;
  width: 0;
  background: #000;
  transition: width 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}

.project-row:hover .card-bottom-line {
  width: 100%;
}

/* Loading state */
.empty-state, .loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: 48px;
  color: #9CA3AF;
}

.empty-icon {
  font-size: 2rem;
  opacity: 0.5;
}

.loading-spinner {
  width: 24px;
  height: 24px;
  border: 2px solid #E5E7EB;
  border-top-color: #6B7280;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .cards-list { padding: 0 16px; }
  .project-row { flex-wrap: wrap; gap: 16px; }
  .row-left { width: 100%; flex-direction: row; align-items: center; }
  .row-right { width: 100%; flex-direction: row; align-items: center; justify-content: space-between; }
}
</style>
