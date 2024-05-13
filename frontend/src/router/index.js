import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '@/components/LoginForm';
import HelloWorld from "@/components/HelloWorld";
import HomeAdministradores from '@/components/HomeAdministradores';
import create_new_user from '@/components/create_new_user';
import create_new_model from '@/components/create_new_model';
import goals from "@/components/model-goals";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: LoginForm
    },
    {
        path : "/",
        name : "home",
        component : HelloWorld
    },
    {
      path : "/admin",
      name : "admin",
      component : HomeAdministradores,
      meta: { requiresAuth: true, role: 'Administrador' }
    },
    {
      path : "/create-user",
      name : "new_user",
      component : create_new_user,
      meta: { requiresAuth: true, role: 'Administrador' }
    },
    {
      path : "/create-model",
      name : "new-model",
      component : create_new_model
    },
    {
      path : "/model-goals",
      name : "model-goals",
      component : goals
    }
    // Agrega más rutas según sea necesario
  ]
});
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const user = JSON.parse(localStorage.getItem('user_info'));
  
  if (requiresAuth && !user) {
    next('/login');
  } else if (requiresAuth && user.role !== to.meta.role) {
    next('/home');  // o cualquier otra ruta de fallback segura
  } else {
    next();
  }
});

export default router;
