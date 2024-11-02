<template>
    <aside v-if="userStore.user.isAuthenticated" :class="`bg-zinc-950 h-screen duration-300 sticky top-0 overflow-hidden ${sideBarWidth}`">
      <div
        @click="toggleSidebar"
        :class="{
          'flex justify-center bg-zinc-800 rounded mx-3': isMinimized,
        }"
        class="cursor-pointer flex justify-end p-2 my-4 transition-all duration-300"
      >
        <box-icon
          :class="{'rotate-180': isMinimized}"
          type="solid"
          name="chevrons-left"
          color="white"
        ></box-icon>
      </div>
      <div>
        <div class="flex items-center mb-4 transition-all duration-300">
          <div>
            <img
              :class="`rounded-full border-4 border-white ml-3 transition-all duration-300 ${
                isMinimized ? '3xl:size-14 size-12 mb-18' : '3xl:size-20 size-16'
              }`"
              src="/SneX.jpg"
              alt="Snex"
            />
          </div>
          <div v-if="!isMinimized" class="ml-5 3xl:text-3xl text-2xl font-norwester">
            {{ userStore.user.username }}
          </div>
        </div>
        <div v-if="!isMinimized" class="flex justify-center space-x-3 mt-7 text-center 3xl:text-xl ">
          <div>
            <h1>0</h1>
            <h2>Followers</h2>
          </div>
          <div>
            <h1>0</h1>
            <h2>Following</h2>
          </div>
          <div>
            <h1>0</h1>
            <h2>Snex Points</h2>
          </div>
        </div>
        <div class="flex flex-col space-y-2 text-2xl mt-7 ">
          <RouterLink :to="'/'" :class="navLinkClasses('/')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="home" :color="iconColor('/')"></box-icon>
            <span v-if="!isMinimized">HOME</span>
          </RouterLink>
          <RouterLink :to="'/profile'" :class="navLinkClasses('/profile')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="user" :color="iconColor('/profile')"></box-icon>
            <span v-if="!isMinimized">PROFILE</span>
          </RouterLink>
          <RouterLink :to="'/library'" :class="navLinkClasses('/library')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="book" :color="iconColor('/library')"></box-icon>
            <span v-if="!isMinimized">LIBRARY</span>
          </RouterLink>
          <RouterLink :to="'/recent'" :class="navLinkClasses('/recent')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="time" :color="iconColor('/recent')"></box-icon>
            <span v-if="!isMinimized">RECENT</span>
          </RouterLink>
          <RouterLink :to="'/saved'" :class="navLinkClasses('/saved')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="book-bookmark" :color="iconColor('/saved')"></box-icon>
            <span v-if="!isMinimized">SAVED</span>
          </RouterLink>
          <RouterLink :to="'/settings'" :class="navLinkClasses('/settings')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="cog" :color="iconColor('/settings')"></box-icon>
            <span v-if="!isMinimized">SETTINGS</span>
          </RouterLink>
          <RouterLink :to="'/upload'" :class="navLinkClasses('/upload')">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="cloud-upload" :color="iconColor('/upload')"></box-icon>
            <span v-if="!isMinimized">UPLOAD</span>
          </RouterLink>
          <a class="flex items-center bg-zinc-800 rounded-md mx-3 h-10 space-x-2 duration-300 hover:bg-zinc-900" href="">
            <box-icon class="ml-3 3xl:ml-4" type="solid" name="log-out" color="white"></box-icon>
            <span v-if="!isMinimized">LOG OUT</span>
          </a>
        </div>
      </div>
    </aside>
  </template>
  




<script setup>
import { ref, computed } from 'vue';
import { useRoute, RouterLink } from 'vue-router';
import { useUserStore } from './user';

const userStore = useUserStore();
const isMinimized = ref(false);
const route = useRoute();

const sideBarWidth = computed(() => {
    const width = window.innerWidth;
    if (isMinimized.value) {
        return width >= 1920 ? 'w-20' 
             : width >= 1536 ? 'w-18' 
             : 'w-18'; // Same minimized width for all screen sizes
    } else {
        return width >= 1920 ? 'w-72' 
             : width >= 1536 ? 'w-60' 
             : width >= 1280 ? 'w-58' 
             : width >= 1024 ? 'w-56' 
             : width >= 768 ? 'w-48' 
             : 'w-40';
    }
});



const toggleSidebar = () => {
  isMinimized.value = !isMinimized.value;
};

const navLinkClasses = (path) => {
    return `flex items-center rounded-md mx-3 3xl:h-12 h-10 space-x-2 duration-100 ease-out hover:bg-zinc-900 ${route.path === path ? 'bg-rose-700 hover:bg-rose-700' : 'bg-zinc-800'
        }`;
};

const iconColor = (path) => {
    return route.path === path ? 'rose' : 'white';
};
</script>



<style scoped>
.w-18 {
    width: 72px;
    transition: width 0.3s ease-in-out;
}

.w-64 {
    width: 256px;
    transition: width 0.5s ease-in-out
}

.mb-18 {
    margin-bottom: 92px;
}

.w-20 {
  width: 80px;
  transition: width 0.3s ease-in-out;
}
.w-72 {
  width: 288px;
  transition: width 0.3s ease-in-out;
}

</style>
