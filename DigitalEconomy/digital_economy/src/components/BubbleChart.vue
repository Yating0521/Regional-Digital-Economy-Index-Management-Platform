<template>
  <div id="bubbleChart" style="width: 100%; height: 100%;margin-top: 25px;"></div>
</template>

<script>
import * as echarts from 'echarts';
import {mapGetters} from "vuex";

export default {
  data() {
    return {
      bubbleData: []
    };
  },
  computed: {
    ...mapGetters(['selectedYear']),
  },
  watch: {
    selectedYear: {
      immediate: true,
      handler(newYear) {
        this.getBubbleData(newYear).then(() => {
          this.initBubbleChart();
        });
      }
    }
  },

  methods: {
    async getBubbleData(year) {
      try {
        const res = await this.$http.get(`data/bubble/${year}`);
        this.bubbleData = res.data.bubbleData;
      } catch (error) {
        console.error(error);
      }
    },

    initBubbleChart() {
      let data = this.bubbleData;
      let bubbleChart = echarts.init(document.getElementById("bubbleChart"));
      window.onresize = () => {
        bubbleChart.resize();
      };
      bubbleChart.setOption({
        title: {
          text: '区域数字经济水平分布',  // 标题
          left: 'left',
          top: 8,
          textStyle: {
            color: '#333',
            fontSize: 17
          }
        },
        grid: {
          top: 80,  // 调整图表与顶部的距离
          bottom: 40,  // 调整图表与底部的距离
        },
        tooltip: {
          trigger: 'item',
          formatter: function (params) {
            return params.data.name + ': ' + params.data.value[1];
          }
        },

        xAxis: {
          type: 'category',
          data: ['一级地区', '二级地区', '三级地区', '其他地区'],
          axisLine: {
            lineStyle: {
              color: '#808080'  // 设置 x 轴线颜色
            },

          },

        },
        yAxis: {
          type: 'value',
          name: '得分',  // 纵坐标名称
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
            itemStyle: {
              color: function (params) {
                // 根据地区级别设置不同颜色
                const level = params.data.value[0];
                if (level === 0) {
                  return 'red';  // 一级地区
                } else if (level === 1) {
                  return 'green';  // 二级地区
                } else if (level === 2) {
                  return 'blue';  // 三级地区
                } else {
                  return 'gray';  // 其他地区
                }
              }
            }
          }
        ]
      });
    }
  }
}
</script>
