import { createApp } from 'vue'
import App from './App.vue'
import Vue from 'vue'
import axios from 'axios';
axios.defaults.baseURL = '/api'
Vue.prototype.$http = axios;

createApp(App).mount('#app')
