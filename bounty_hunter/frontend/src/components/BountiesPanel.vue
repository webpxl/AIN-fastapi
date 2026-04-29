<script setup>
import { useBountyBoardStore } from '@/stores/bountyBoard'
const store = useBountyBoardStore()
</script>

<template>
  <article class="bounties-panel panel">
    <div class="panel-head">
      <h2>Bounties</h2>
      <span>{{ store.filteredBounties.length }} results</span>
    </div>

    <div v-if="!store.filteredBounties.length" class="empty-state">No bounties match your filters.</div>

    <ul v-else class="bounty-list">
      <li v-for="bounty in store.filteredBounties" :key="bounty.id" class="bounty-card">
        <div>
          <h3>{{ bounty.target_name }}</h3>
          <p>{{ bounty.planet.name }} · {{ bounty.planet.sector }}</p>
        </div>
        <div class="reward-meta">
          <strong>{{ store.formatCredits(bounty.reward_amount) }} cr</strong>
          <span :class="['status-pill', bounty.status === 'Active' ? 'active' : 'captured']">{{
            bounty.status
          }}</span>
        </div>
      </li>
    </ul>
  </article>
</template>

<style scoped>
.panel {
  background: rgba(6, 24, 34, 0.7);
  border: 1px solid rgba(82, 204, 227, 0.24);
  border-radius: 16px;
  padding: 1rem;
  backdrop-filter: blur(7px);
}

.panel-head {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.7rem;
}

.panel-head span {
  color: var(--accent-amber);
}

.bounty-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 0.6rem;
}

.bounty-card {
  border: 1px solid rgba(113, 224, 245, 0.2);
  border-radius: 12px;
  padding: 0.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.65rem;
  animation: rise 360ms ease both;
}

.bounty-card h3 {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.97rem;
}

.bounty-card p {
  color: var(--text-muted);
  font-size: 0.84rem;
}

.reward-meta {
  text-align: right;
}

.reward-meta strong {
  display: block;
}

.status-pill {
  display: inline-block;
  margin-top: 0.23rem;
  border-radius: 999px;
  font-size: 0.72rem;
  padding: 0.2rem 0.55rem;
}

.status-pill.active {
  background: rgba(64, 224, 208, 0.18);
  border: 1px solid rgba(64, 224, 208, 0.4);
}

.status-pill.captured {
  background: rgba(255, 183, 94, 0.18);
  border: 1px solid rgba(255, 183, 94, 0.45);
}

.empty-state {
  padding: 0.75rem;
  border-radius: 12px;
  background: rgba(64, 224, 208, 0.08);
  border: 1px dashed rgba(64, 224, 208, 0.35);
}

@keyframes rise {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
