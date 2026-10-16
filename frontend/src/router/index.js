import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/manager/home'
    },
    {
      path: '/manager',
      name: 'layout',
      component: () => import('@/layouts/layouts.vue'),
      children: [
        {
          path: 'home',
          name: 'home',
          component: () => import('@/views/Home.vue')
        },
        {
          path: 'lab',
          name: 'lab',
          component: () => import('@/views/Lab.vue')
        },
        {
          path: 'equ',
          name: 'equ',
          component: () => import('@/views/Equ.vue')
        },
        {
          path: 'user',
          name: 'user',
          component: () => import('@/views/User.vue')
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/Register.vue')
    }
  ]
})

export default router
