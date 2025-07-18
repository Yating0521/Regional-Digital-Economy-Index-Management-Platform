<template>
  <div class="display" style="width: 100%;height: 100%;align-items: center">
    <h2 style="text-align: center;font-size: 17px;">{{selectedYear}}{{selectedProvince}}{{buttonText}}</h2>
    <div class="box">
      <input type="text" v-model="textData" readonly class="square-textbox">
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
    return {
      textData:''
    }
  },
  computed: {
    ...mapGetters(['selectedYear','selectedProvince','buttonText']),
  },

  watch: {
    selectedYear: {
      immediate: true,
      handler(newYear) {
        this.getTextData(newYear,this.selectedProvince,this.buttonText)
        }
      },

    selectedProvince: {
      immediate: true,
      handler(newProvince) {
        this.getTextData(this.selectedYear,newProvince, this.buttonText)
      }
    },

    buttonText: {
      immediate: true,
      handler(newText) {
        this.getTextData(this.selectedYear,this.selectedProvince, newText)
      }
    }
  },

  methods: {
    async getTextData(year,province,name) {
      try {
        const res = await this.$http.get(`data/text/${year}/${province}/${name}`);
        this.textData = res.data.textData;
      } catch (error) {
        console.error(error);
      }
    },
  }
};



</script>

<style scoped>
.square-textbox {
  width: 125px; /* 设置文本框的宽度 */
  height: 100px; /* 设置文本框的高度，使其成为正方形 */
  padding: 10px; /* 设置内边距 */
  font-size: 50px; /* 设置字体大小 */
  font-weight: bold;
  font-family: Arial, sans-serif; /* 设置字体样式 */
  border: none; /* 设置边框样式 */
  border-radius: 5px; /* 设置边框圆角 */
  box-sizing: border-box; /* 设置盒模型为边框盒模型 */
  text-align: center;
  background-color: aliceblue;
  box-shadow: 0 0 10px 5px mediumslateblue;
}

.box{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
