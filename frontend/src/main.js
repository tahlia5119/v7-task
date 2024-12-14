import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router';
import GamePage from "./components/GamePage.vue"

const routes = [
    { path: "/", component: GamePage },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App);
app.use(router);
app.mount("#app");
