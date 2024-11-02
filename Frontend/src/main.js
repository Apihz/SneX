import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import 'boxicons';
import { createWebHistory, createRouter } from 'vue-router';
import Home from './components/Home.vue';
import 'material-design-icons-iconfont/dist/material-design-icons.css';
import axios from 'axios';
import { createPinia } from 'pinia';


axios.defaults.baseURL = 'http://127.0.0.1:8000/';

const routes = [
    { path: '/', component: Home },
    { path: '/library', component: () => import('./components/Library.vue')},
    { path: '/recent', component:  () => import('./components/Recent.vue')},
    { path: '/saved', component:  () => import('./components/Saved.vue')},
    { path: '/settings', component:  () => import('./components/Settings.vue')},
    { path: '/profile', component:  () => import('./components/Profile.vue')},
    { path: '/upload', component:  () => import('./components/Upload.vue')},
    { path: '/login', component:  () => import('./components/Login.vue')},
    { path: '/signup', component:  () => import('./components/Signup.vue')},
];

const pinia = createPinia();

const router = createRouter({
    history: createWebHistory(),
    routes,
});

const app = createApp(App);

app.use(router);
app.use(pinia);

app.mount('#app');
