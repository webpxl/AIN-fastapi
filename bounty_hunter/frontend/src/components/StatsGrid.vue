<script setup>
import { useBountyBoardStore } from '@/stores/bountyBoard'
const store = useBountyBoardStore()
</script>

<template>
  <section class="stats-grid">
    <article>
      <h2>Total Bounties</h2>
      <p>{{ store.bounties.length }}</p>
    </article>
    <article>
      <h2>Active Hunts</h2>
      <p>{{ store.activeBountyCount }}</p>
    </article>
    <article>
      <h2>Captured Targets</h2>
      <p>{{ store.capturedBountyCount }}</p>
    </article>
    <article>
      <h2>Highest Reward</h2>
      <p>{{ store.formatCredits(store.topReward) }} cr</p>
    </article>
  </section>
</template>

<style scoped>
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.85rem;
  margin-bottom: 1rem;
}

.stats-grid article {
  background: rgba(8, 28, 37, 0.7);
  border: 1px solid rgba(99, 234, 255, 0.2);
  border-radius: 16px;
  padding: 0.9rem;
}

.stats-grid h2 {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 0.35rem;
}

.stats-grid p {
  font-size: 1.3rem;
  font-weight: 700;
}

@media (max-width: 720px) {
  .stats-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
</style>
