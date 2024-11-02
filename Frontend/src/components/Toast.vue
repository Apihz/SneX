<template>
    <div v-if="store.isVisible" class="transition ease-in-out delay-500 duration-50000 -translate-x-10 px-6 py-6 fixed top-10 mt-16 translate-y-3 right-12 rounded-lg
    bg-emerald-500 text-white text-center">
        {{ store.message }}
    </div>
</template>

<script setup>
// Importing the store from Pinia
import { useToastStore } from './toast.js';

// Directly use the store
const store = useToastStore();
</script>

<style lang="scss" scoped>
/* Add styles here if needed */
</style>
