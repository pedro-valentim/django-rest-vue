import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import VueMatchHeights from 'vue-match-heights';
 
Vue.use(VueMatchHeights);
Vue.use(VueMaterial);

new Vue({
    el: '#app',
    render: h => h(App)
});
