<script setup>
import LoginComponent from '@/components/LoginComponent.vue';
import ProtectedComponent from '@/components/ProtectedComponent.vue';
</script>

<template>
  <main>
    <LoginComponent />
    <ProtectedComponent />

    <nav>
      <img width="160px" src="@/assets/wizard.gif" alt="A wizard" />
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
