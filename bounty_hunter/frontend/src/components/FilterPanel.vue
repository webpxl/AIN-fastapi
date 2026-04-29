<script setup>
import { useBountyBoardStore } from '@/stores/bountyBoard'
const store = useBountyBoardStore()
</script>

<template>
  <section class="control-panel">
    <label>
      Search
      <input v-model="store.bountySearch" type="text" placeholder="Target or planet" />
    </label>

    <label>
      Sector
      <select v-model="store.selectedSector">
        <option value="all">All sectors</option>
        <option v-for="sector in store.sectorOptions" :key="sector" :value="sector">{{ sector }}</option>
      </select>
    </label>

    <label>
      Status
      <select v-model="store.statusFilter">
        <option value="all">All statuses</option>
        <option value="Active">Active</option>
        <option value="Captured">Captured</option>
      </select>
    </label>

    <label>
      Min Reward
      <input v-model.number="store.minReward" type="number" min="0" step="500" />
    </label>

    <label>
      Sort
      <select v-model="store.sortBy">
        <option value="rewardDesc">Reward high to low</option>
        <option value="rewardAsc">Reward low to high</option>
        <option value="targetAsc">Target A to Z</option>
      </select>
    </label>
  </section>
</template>

<style scoped>
.control-panel {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 0.7rem;
  margin-bottom: 1.1rem;
}

.control-panel label {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-size: 0.82rem;
  color: var(--text-muted);
}

input,
select {
  border: 1px solid rgba(82, 204, 227, 0.35);
  background: rgba(2, 21, 29, 0.68);
  border-radius: 12px;
  padding: 0.6rem 0.75rem;
  color: var(--text-main);
  outline: none;
}

input:focus,
select:focus {
  border-color: rgba(255, 183, 94, 0.9);
}

@media (max-width: 1050px) {
  .control-panel {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .control-panel {
    grid-template-columns: 1fr;
  }
}
</style>
