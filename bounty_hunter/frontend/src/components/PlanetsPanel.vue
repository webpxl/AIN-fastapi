<script setup>
import { useBountyBoardStore } from '@/stores/bountyBoard'
const store = useBountyBoardStore()
</script>

<template>
  <article class="planets-panel panel">
    <div class="panel-head">
      <h2>Planets</h2>
      <span>{{ store.planets.length }} mapped</span>
    </div>

    <ul class="planet-list">
      <li v-for="planet in store.planetsWithCounts" :key="planet.id" class="planet-card">
        <div>
          <h3>{{ planet.name }}</h3>
          <p>{{ planet.sector }}</p>
        </div>
        <strong>{{ planet.bountyCount }} bounties</strong>
      </li>
    </ul>

    <div class="intel-block">
      <h3>Sector Intel</h3>
      <ul>
        <li v-for="group in store.sectorIntel" :key="group.sector">
          <span>{{ group.sector }}</span>
          <strong>{{ group.bounties.length }}</strong>
        </li>
      </ul>
    </div>
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

.planet-list,
.intel-block ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 0.6rem;
}

.planet-card,
.intel-block li {
  border: 1px solid rgba(113, 224, 245, 0.2);
  border-radius: 12px;
  padding: 0.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.65rem;
  animation: rise 360ms ease both;
}

.planet-card h3,
.intel-block h3 {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.97rem;
}

.planet-card p {
  color: var(--text-muted);
  font-size: 0.84rem;
}

.intel-block {
  margin-top: 1rem;
  padding-top: 0.8rem;
  border-top: 1px solid rgba(99, 234, 255, 0.2);
}

.intel-block li span {
  color: var(--text-muted);
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
