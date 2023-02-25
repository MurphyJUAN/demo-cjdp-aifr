// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import App from './App';
import router from './router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(VueAxios, axios);
// Vue.prototype.$ajax = axios;
Vue.use(ElementUI);
Vue.config.productionTip = false;

Vue.prototype.$testApi = 'http://127.0.0.1:8000';
Vue.prototype.$globalApi = 'https://demo-cjdp-aifr.herokuapp.com';
Vue.prototype.$api = Vue.prototype.$testApi;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
