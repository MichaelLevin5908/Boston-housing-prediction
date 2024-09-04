import { createRouter, createWebHistory } from 'vue-router';
import Prediction from './views/Prediction.vue';

const routes = [
  {
    path: '/',
    name: 'prediction',
    component: Prediction,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;