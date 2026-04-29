<script setup>
import { onMounted } from 'vue'
import { useBountyBoardStore } from '@/stores/bountyBoard'
import BoardHeader from '@/components/BoardHeader.vue'
import StatsGrid from '@/components/StatsGrid.vue'
import FilterPanel from '@/components/FilterPanel.vue'
import BountiesPanel from '@/components/BountiesPanel.vue'
import PlanetsPanel from '@/components/PlanetsPanel.vue'

const store = useBountyBoardStore()

onMounted(() => {
  store.loadBoard()
})
</script>

<template>
  <main class="galaxy-shell">
    <div class="nebula-layer" aria-hidden="true" />

    <BoardHeader />
    <StatsGrid />
    <FilterPanel />

    <p v-if="store.errorMessage" class="feedback error">{{ store.errorMessage }}</p>
    <p v-else-if="store.isLoading" class="feedback loading">Scanning frontier channels...</p>

    <section v-else class="content-grid">
      <BountiesPanel />
      <PlanetsPanel />
    </section>
  </main>
</template>

<style scoped>
.galaxy-shell {
  position: relative;
  min-height: 100vh;
  padding: clamp(1rem, 2vw, 2.2rem);
  color: var(--text-main);
}

.nebula-layer {
  position: fixed;
  inset: 0;
  z-index: -1;
  background:
    radial-gradient(circle at 15% 20%, rgba(255, 183, 94, 0.3), transparent 45%),
    radial-gradient(circle at 80% 10%, rgba(64, 224, 208, 0.28), transparent 50%),
    radial-gradient(circle at 60% 80%, rgba(255, 110, 61, 0.22), transparent 48%),
    linear-gradient(120deg, #06141a 10%, #0b2430 50%, #051017 100%);
}

.feedback {
  margin-bottom: 1rem;
  border-radius: 12px;
  padding: 0.7rem 0.85rem;
}

.loading {
  background: rgba(64, 224, 208, 0.12);
  border: 1px solid rgba(64, 224, 208, 0.3);
}

.error {
  background: rgba(255, 110, 61, 0.14);
  border: 1px solid rgba(255, 110, 61, 0.36);
}

.content-grid {
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  gap: 0.9rem;
}

@media (max-width: 1050px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}
</style>
