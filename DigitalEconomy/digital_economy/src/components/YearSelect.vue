<template>
  <div>
    <select class="selectstyle" v-model="selectedYear" @change="handleChange">
      <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
    </select>
  </div>
</template>

<script>

export default {
  data() {
    return {
      selectedYear: 2022, // 默认选中的年份
      availableYears: [2021, 2022] // 可用的年份
    };
  },
  methods: {
    handleChange() {
      this.$store.commit('setSelectedYear',this.selectedYear)
    }
  }
};
</script>
<style>
.selectstyle{
  width: 100px;
  height: 25px;
  text-align: center;
  border-radius: 5px;
  background-color: rgba(122, 155, 255, 0.3);
}
</style>