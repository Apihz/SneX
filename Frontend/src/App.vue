<template>
  <div class="flex flex-col h-screen w-full">
    <!-- Conditionally render NavBar and Sidebar -->
    <NavBar v-if="!isAuthRoute" class="flex-none" />
    <div class="flex flex-1">
      <Sidebar v-if="!isAuthRoute" class="flex-none" />
      <main :class="isAuthRoute ? 'w-full h-full' : 'flex-1 overflow-hidden'">
        <RouterView />
        <Toast />
      </main>
    </div>
    
  </div>

  
</template>

<script setup>
import { computed, onBeforeMount } from 'vue';
import { useRoute } from 'vue-router';
import NavBar from './components/NavBar.vue';
import Sidebar from './components/Sidebar.vue';
import Toast from './components/Toast.vue';

import { useUserStore } from './components/user';
import axios from 'axios';

const route = useRoute();

const isAuthRoute = computed(() => {
  return route.path === '/login' || route.path === '/signup';
});

const userStore = useUserStore();

onBeforeMount(() => {
  userStore.initStore();

  const token = userStore.user.access

  if(token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  }else {
    axios.defaults.headers.common['Authorization'] = "";

  }
});

</script>

<style scoped>
</style>
