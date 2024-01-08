import { createRouter, createWebHistory } from "vue-router";
import RecommendedView from '../views/RecommendedView.vue';
import ApartmentView from '../views/ApartmentView.vue';
import SignUpView from '../views/SignUpView.vue';
import LoginView from '../views/LoginView.vue';
//import HomeView from '../views/HomeView.vue'

const routes = [
  { path: '/',  name: 'home' },
  { path: '/apartment/:id', name: 'apartment', component: ApartmentView },
  { path: '/apartments', name: 'apartments',component: RecommendedView },
  { path: '/signup', name: 'signup', component: SignUpView },
  { path: '/login', name: 'login', component: LoginView},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
