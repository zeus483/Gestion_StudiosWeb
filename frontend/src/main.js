import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from './router';
import createStore from './store';


// Configura axios
axios.defaults.baseURL = '/api';

const app = createApp(App);

// Proporciona axios a toda tu aplicación como $http
app.config.globalProperties.$http = axios;

// Asegúrate de usar el router
app.use(router);
app.use(createStore)

// Monta la aplicación en el elemento #app
app.mount('#app');