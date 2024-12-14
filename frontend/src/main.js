import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from "./components/HomePage.vue";
import GamePage from "./components/GamePage.vue"

const routes = [
    { path: "/", component: HomePage },
    { path: "/game", component: GamePage, props: (route) => ({ gridSize: parseInt(route.query.gridSize) || 6, blocks: parseInt(route.query.blocks) || 0 }) },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App);
app.use(router);
app.mount("#app");
