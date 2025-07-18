<template>
  <div id="CrossChart" style="width: 100%; height: 100%;margin-top: 25px;"></div>
</template>

<script>
import * as echarts from 'echarts';
import {mapGetters} from "vuex";

export default {
  data() {
    return {
      crossData: []
    };
  },
  computed: {
    ...mapGetters(['selectedYear']),
  },
  watch: {
    selectedYear: {
      immediate: true,
      handler(newYear) {
        this.getCrossData(newYear).then(() => {
          this.initCrossChart();
        });
      }
    }
  },

  methods: {
    async getCrossData(year) {
      try {
        const res = await this.$http.get(`data/cross/${year}`);
        this.crossData = res.data.crossData;
      } catch (error) {
        console.error(error);
      }
    },

    initCrossChart() {
      let data = this.crossData;
      let crossChart = echarts.init(document.getElementById("CrossChart"));
      crossChart.setOption({
        title: {
          text: '数字指数与GDP交叉分析',  // 标题
          left: 'left',
          top:8,
          textStyle: {
            color: '#333',
            fontSize: 17
      }
        },
        grid: {
          top: 70,  // 调整图表与顶部的距离
          bottom: 50,  // 调整图表与底部的距离
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c}'  // 提示框格式，{b}表示省份名称，{c}表示数字经济发展指数
        },
        xAxis: {
          type: 'value',
          name: 'GDP(亿元)',
          nameLocation: 'center',
          nameGap: 28, // 调整名称与轴线的距离
          nameTextStyle: {
            padding: [0, 0, 0, 290] // 自定义名称与轴线的间距，上下左右依次为：上、右、下、左
          },
          min: 0,
          max: 150000,
          splitLine: {
              show: true,
              lineStyle: {
                width: 1,
                color: 'rgb(132, 112, 255,0.5)'//网格颜色
              }
            },
        },
        yAxis: {
          type: 'value',
          name: '得分',  // 纵坐标名称
          min: 0,
          max: 100,
          nameTextStyle: {
            fontWeight: 'bold'
          },
          splitLine: {
              show: true,
              lineStyle: {
                width: 1,
                color: 'rgb(132, 112, 255,0.5)'//网格颜色
              }
            },
        },
        series: [
          {
            type: 'scatter',
            data: data,
            symbolSize: 25,  // 所有气泡大小相同

          }
        ]
      });
    }
  }
}
</script>
