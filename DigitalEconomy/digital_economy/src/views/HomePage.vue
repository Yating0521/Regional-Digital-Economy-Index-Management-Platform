<template>
  <div>
    <header>
      <h1>区域数字经济指数管理平台</h1>
    </header>
    <section class="container">
      <!-- 左 -->
      <section class="itemLeft">
        <itemPage>
          <RadarChart/>
        </itemPage>
        <itemPage>
          <!--          <h3>区域数字经济水平分布</h3>-->
          <BubbleChart/>
        </itemPage>
      </section>
      <!-- 中 -->
      <section class="itemCenter">
        <!-- 上 -->
        <section class="itemUpper">
          <section class="itemUpperLeft">
            <!-- 左侧内容 -->
            <ButtonOne>数字经济发展指数</ButtonOne>
            <ButtonOne>基础设施指数</ButtonOne>
            <ButtonOne>数字产业指数</ButtonOne>
          </section>
          <!-- 中 -->
          <section class="itemUpperCenter">
            <!-- 中间内容 -->
            <TextComponent/>
          </section>
          <!-- 右 -->
          <section class="itemUpperRight">
            <!-- 右侧内容 -->
            <ButtonOne>产业融合指数</ButtonOne>
            <ButtonOne>发展环境指数</ButtonOne>
          </section>
        </section>
        <!-- 中 -->
        <section class="itemMiddle">
          <YearSelect/>
        </section>
        <!-- 下 -->
        <section class="itemBottom">
          <ChinaMap/>
        </section>
      </section>
      <!-- 右 -->
      <section class="itemRight">
        <itemPage>
          <CrossAnalysisChart/>
        </itemPage>
        <itemPage>
          <RankingChart/>
        </itemPage>
      </section>
    </section>
  </div>
</template>

<script>
import itemPage from "@/components/itemPage.vue";
import RadarChart from "@/components/RadarChart.vue";
import CrossAnalysisChart from "@/components/CrossAnalysisChart.vue";
import RankingChart from "@/components/RankingChart.vue";
import ChinaMap from "@/components/ChinaMap.vue";
import {inject} from "vue";
import YearSelect from "@/components/YearSelect.vue";
import BubbleChart from "@/components/BubbleChart.vue";
import ButtonOne from "@/components/ButtonOne.vue";
import TextComponent from "@/components/TextComponent.vue";

export default {
  components: {
    ButtonOne,
    YearSelect,
    itemPage,
    RadarChart,
    CrossAnalysisChart,
    RankingChart,
    BubbleChart,
    TextComponent,
    ChinaMap
  },

  setup() {
    let $echarts = inject("echarts")
    console.log($echarts)
    let $http = inject("axios")
    console.log($http)

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

.container {
  //最大最小宽度
  min-width: 1200px;
  max-width: 2048px;
  margin: 0 auto;
  padding: .125rem 0 0;
  //background-color:gray;
  display: flex;

}

//左中右分布
.itemLeft, .itemRight {
  flex: 3;
  margin-left: 10px;
  margin-right: 10px;
}

.itemCenter {
  flex: 4.5;
  display: flex;
  flex-direction: column;
  //border: 1px solid blue;
  margin: .25rem;
  //background-color: grey;
}

.itemUpper {
  flex: 2.5;
  //background-color: rgba(0, 0, 255, 0.4);
  display: flex;
  .itemUpperLeft {
  flex: 0.7;
  //background-color: rgba(255, 0, 0, 0.4);
}

.itemUpperCenter {
  flex: 1;
  //background-color: rgba(0, 255, 0, 0.4);
}

.itemUpperRight {
  flex: 0.7;
  //background-color: rgba(0, 0, 0, 0.4);
}
}

.itemBottom {
  flex: 6.5;
  //background-color: rgba(0, 0, 255, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
}

.itemMiddle {
  flex: 0.5;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>