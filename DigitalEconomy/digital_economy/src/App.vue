<template>
  <router-view/>
</template>
<script>
import {provide} from "vue"
import * as echarts from "echarts"
import axios from "axios"
export default {
  setup(){
    provide("echarts",echarts)
    provide("axios",axios)
  }
}
</script>

<style lang="less">
body{
  //background: rgba(255, 255, 255, 0.2)url("~@/assets/bg2.jpg") top center no-repeat;
  //background-size: cover;
  //overflow: hidden;
  background-color:lavender;
}
*{
  box-sizing:border-box;
}
</style>
