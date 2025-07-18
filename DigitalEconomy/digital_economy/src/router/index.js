import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/page',
    name: 'page',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/HomePage.vue')
  },
  {
    path: '/indexpage',
    name: 'indexpage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/MainPage.vue')
  },
    {
    path: '/importpage',
    name: 'importpage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/ImportPage.vue')
  },
  {
  path:"/",
  redirect:"/indexpage"
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
