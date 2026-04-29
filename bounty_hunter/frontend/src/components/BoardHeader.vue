<script setup>
import { useBountyBoardStore } from '@/stores/bountyBoard'
const store = useBountyBoardStore()
</script>

<template>
  <header class="board-header">
    <div>
      <p class="eyebrow">Interstellar Intelligence Network</p>
      <h1>Galaxy Bounty Board</h1>
      <p class="subcopy">Browse live bounties and mapped planets across known sectors.</p>
    </div>
    <button class="refresh-btn" @click="store.loadBoard">Refresh Feed</button>
  </header>
</template>

<style scoped>
.board-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: end;
  margin-bottom: 1.25rem;
}

.eyebrow {
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent-cyan);
  font-size: 0.78rem;
  margin-bottom: 0.3rem;
}

h1 {
  font-family: 'Orbitron', sans-serif;
  font-size: clamp(1.8rem, 4vw, 3rem);
  letter-spacing: 0.03em;
}

.subcopy {
  color: var(--text-muted);
  margin-top: 0.35rem;
}

.refresh-btn {
  border: 1px solid rgba(64, 224, 208, 0.55);
  background: rgba(5, 27, 36, 0.6);
  color: #f4ffff;
  border-radius: 999px;
  padding: 0.65rem 1rem;
  cursor: pointer;
}

.refresh-btn:hover {
  background: rgba(14, 72, 91, 0.65);
}

@media (max-width: 720px) {
  .board-header {
    flex-direction: column;
    align-items: start;
  }
}
</style>
