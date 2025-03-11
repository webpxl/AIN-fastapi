<script setup>
import RandomScoreComponent from '@/components/RandomScoreComponent.vue';
import HighscoreComponent from '../components/HighscoreComponent.vue'
import DeleteScoreComponent from '../components/DeleteScoreComponent.vue'
</script>

<template>
  <main>
    <HighscoreComponent />
    <RandomScoreComponent />
    <DeleteScoreComponent />
  </main>
</template>

<style scoped>
  main {
    background-color: #222;
    padding: 24px;
  }
</style>
