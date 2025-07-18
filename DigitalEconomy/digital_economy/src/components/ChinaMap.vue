<template>
  <div id="china-map" style="height: 100%;width: 100%"></div>
</template>

<script>
//import {inject, onMounted} from "vue";
import * as echarts from 'echarts';
import {mapGetters, mapActions} from 'vuex';

export default {
  data() {
    return {
      mapData: []
    };
  },
  computed: {
    ...mapGetters(['selectedYear'])
  },
  watch: {
    selectedYear: {
      immediate: true,
      handler(newYear) {
        this.getMapData(newYear).then(() => {
          this.initMap();
        });
      }
    }
  },
  methods: {
    ...mapActions(['updateSelectedProvince']),

    async getMapData(year) {
      try {
        const res = await this.$http.get(`data/map/${year}`);
        this.mapData = res.data.mapData;
      } catch (error) {
        console.error(error);
      }
    },

    initMap() {
      let data = this.mapData;
      let chinaMap = echarts.init(document.getElementById("china-map"));
      window.onresize = () => {
        chinaMap.resize();
      };

      chinaMap.on('click', (params) => {
        const selectedProvince = params.name; // 获取点击的省份名称
        this.updateSelectedProvince(selectedProvince); // 触发更新 Vuex store 中的省份信息
      });

      chinaMap.setOption({
        tooltip: {},
        dataRange: {
          show: false,
          min: 0,
          max: 100,
          text: ["High", "Low"],
          realtime: true,
          calculable: true,
          color: ["orangered", "#FF9B52", '#FAEBD7'],
        },
        geo: {
          map: "china",
          roam: false,
          label: {
            normal: {
              show: true,
              textStyle: {
                color: "#fff",
              },
            },
          },
          itemStyle: {
            normal: {
              borderColor: "#293171",
              borderWidth: "2.5",
              areaColor: "#0A0F33",
            },
            emphasis: {
              areaColor: null,
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              shadowBlur: 20,
              borderWidth: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
        series: [
          {
            type: "scatter",
            coordinateSystem: "geo",
          },
          {
            name: "数字经济发展指数",
            type: "map",
            geoIndex: 0,
            data: data,
            emphasis: {
              label: {
                show: true
              },
              itemStyle: {
                areaColor: '#7A9BFF'
              }
            },
            selectedMode: 'single', // 单选模式
          },
        ],
      });
    },
  },
}


</script>

<style scoped>
#china-map {
  width: 100%;
  height: 100%;
}
</style>
