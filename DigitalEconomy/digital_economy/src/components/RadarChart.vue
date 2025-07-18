<template>
  <div id="radarChart" style="width: 100%; height: 100%;margin-top: 25px;"></div>
</template>

<script>
// import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import {mapGetters} from "vuex";

export default {
  data() {
    return {
      radarData: []
    };
  },

  computed: {
    ...mapGetters(['selectedYear', 'selectedProvince']),
  },

  // mounted() {
  //   this.getRadarData(2022, "北京").then(() => {
  //   this.initRadarChart()
  //   });
  // },
  watch: {
    selectedYear: {
      immediate: true,
      handler(newYear) {
        this.getRadarData(newYear, this.selectedProvince).then(() => {
          this.initRadarChart();
        });
      }
    },
    selectedProvince: {
      immediate: true,
      handler(newProvince) {
        this.getRadarData(this.selectedYear, newProvince).then(() => {
          this.initRadarChart();
        });
      }
    }
  },

  methods: {
    async getRadarData(year, province) {
      try {
        const res = await this.$http.get(`data/radar/${year}/${province}`);
        this.radarData = res.data.radarData;
      } catch (error) {
        console.error(error);
      }
    },

    initRadarChart() {
      let data = this.radarData;
      let name= this.selectedYear+this.selectedProvince;
      let radarChart = echarts.init(document.getElementById("radarChart"));
      window.onresize = () => {
        radarChart.resize();
      };
      radarChart.setOption({
        title: {
          text: '数字经济指数多维分析',  // 标题
          left: 'left',
          top: 8,
          textStyle: {
            color: '#333',
            fontSize: 17
          }
        },
        tooltip: {},
        radar: {
          center: ['50%', '60%'], // 雷达图位置
          radius: '70%', // 缩小雷达图大小

          indicator: [
            {name: '数字经济发展指数', max: 100},
            {name: '基础设施', max: 100},
            {name: '数字产业', max: 100},
            {name: '产业融合', max: 100},
            {name: '发展环境', max: 100}
          ],
          name: {
            textStyle: {
              color: '#4B0082', // 指标字体的颜色
              fontWeight: 'bold'
            },
          },
          splitArea: {
            show: true,
            areaStyle: {
              color: ['rgba(119,234,223, 0)', 'rgba(122, 155, 255, 0.5)', 'rgba(100,175,233, 0)', 'rgba(122, 155, 255, 0.5)', 'rgba(66,139,212, 0)'],//分割区域的背景色
              shadowColor: 'rgba(0, 0, 0, 0.2)',//分割区域阴影
              shadowBlur: 10
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              width: 1,
              color: '#8470FF'//网格颜色
            }
          },
        },

        series: [{
          name:name,
          type: 'radar',
          data: data,

          areaStyle: {
            normal: {
              color: 'rgb(70, 130, 180,0.8)' // 设置颜色和透明度
            }
          },
        }],
      })
    }
  }
}

</script>

<style scoped>

</style>


