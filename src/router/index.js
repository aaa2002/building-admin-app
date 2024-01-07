import { createRouter, createWebHistory } from "vue-router";
import RecommendedView from '../views/RecommendedView.vue';
import ApartmentView from '../views/ApartmentView.vue';
import SignUpView from '../views/SignUpView.vue';

const routes = [
  { path: '/', component: RecommendedView, name: 'home' },
  { path: '/apartment/:id', name: 'apartment', component: ApartmentView },
  { path: '/apartments', name: 'apartments' },
  { path: '/signup', name: 'signup', component: SignUpView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
