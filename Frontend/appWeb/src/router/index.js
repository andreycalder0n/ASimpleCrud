import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/envio',
      name: 'envio',
      component: () => import('../views/envioView.vue')
    },
    {
      path: '/listar',
      name: 'listar',
      component: () => import('../views/listadoView.vue')
    }
  ]
})

export default router
