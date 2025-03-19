<script setup>
import FormComponent from '@/components/FormComponent.vue';
</script>

<template>
  <main>
    <FormComponent />

    <nav>
      <img width="320px" src="@/assets/ship.png" alt="A ship" />
    </nav>
  </main>
</template>

<style scoped>
  main {
    background-color: #C8DAE6;
    padding: 24px;
  }

  nav {
    position: fixed;
    bottom: -5px;
    right: 150px;
  }
</style>
