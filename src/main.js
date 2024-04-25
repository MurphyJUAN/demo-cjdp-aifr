// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'element-ui/lib/theme-chalk/index.css';
import Vue from 'vue';
import ElementUI from 'element-ui';
import Multiselect from 'vue-multiselect';
import axios from 'axios';
import VueAxios from 'vue-axios';
import App from './App';
import router from './router';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);


Vue.component('multiselect', Multiselect);
Vue.use(VueAxios, axios);
// Vue.prototype.$ajax = axios;
Vue.use(ElementUI);
Vue.config.productionTip = false;
// Vue.prototype.$globalApi = 'https://subtle-cricket-grown.ngrok-free.app';
Vue.prototype.$testApi = 'http://127.0.0.1:8000';
// Vue.prototype.$globalApi = 'http://140.114.80.46:5556';
// Vue.prototype.$globalApi = 'http://140.114.80.195:8080';
Vue.prototype.$globalApi = 'https://hssai-custodiAI.phys.nthu.edu.tw';
Vue.prototype.$globalApi = '';
Vue.prototype.$api = Vue.prototype.$globalApi;
// Vue.prototype.$api = Vue.prototype.$testApi;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
