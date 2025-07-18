import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "lib-flexible/flexible.js"
import $http from "@/api/index.js"
import * as echarts from 'echarts';
import geoJson from '@/utils/china.json'

const app=createApp(App)
app.config.productionTip = false;
app.use(store).use(router).mount('#app')
app.config.globalProperties.$http=$http
app.config.globalProperties.$echarts = echarts

echarts.registerMap('china', geoJson);