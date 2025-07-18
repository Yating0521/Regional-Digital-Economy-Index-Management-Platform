<template>
  <div>
    <header>
      <h1>区域数字经济指数管理平台</h1>
    </header>
    <div class="description">
      <p style="font-size: 35px">区域数字经济综合指数可视化</p>
      <p style="font-size: 20px">基础设施、数字产业、产业融合、发展环境等多维数据展示</p>
    </div>
    <div class="button-container">
      <button class="button-style" @click="redirectToMainPage">点击进入平台</button>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    redirectToMainPage() {
      this.$router.push({ name: 'page' })
    }
  }
}
</script>

<style lang="less">
header {
  height: 1rem;
  width: 100%;
  background-color: rgba(0, 0, 255, 0.4);
  margin-top: -10px;

  h1 {
    font-size: 0.375rem;
    color: #fff;
    text-align: center;
    line-height: 1rem;
  }
}
.description {
  text-align: center;
  margin-top: 30px;
  //background-color: cornflowerblue;
  color: rgb(25, 25, 112, 0.6);
}
.button-container {
  display: flex;
  justify-content: center;
  margin-top: 40px;
}
.button-style {
  padding: 18px 100px;
  font-size: 25px;
  border: none;
  border-radius: 30px;
  background-color: rgb(41, 49, 113, 0.8);
  color: azure;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 0 10px 5px rgb(25, 25, 112, 0.6);
  letter-spacing: 4px;
}
.button-style:hover {
  background-color: rgb(25, 25, 112, 0.6);
  transform: scale(1.05); /* 鼠标悬浮时放大 */
}

</style>