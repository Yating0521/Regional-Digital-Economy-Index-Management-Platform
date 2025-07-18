<template>
  <div class="row_list">
      <h3 style="font-size: 17px; color: #333; margin-top: 25px;">地区经济指数排名</h3>
    <div class="table-wrapper">
      <table class="ranking-table">
        <thead>
          <tr>
            <th>排名</th>
            <th>地区</th>
            <th>指数</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in rankData" :key="item.rank">
            <td>{{ item.rank }}</td>
            <td>{{ item.region }}</td>
            <td>{{ item.economic_index }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
      rankData: []
    };
  },
  computed: {
    ...mapGetters(['selectedYear'])
  },
  watch: {
    selectedYear: {
      immediate: true,
      handler(newYear) {
        this.getRankData(newYear);
      }
    }
  },

  methods: {
    async getRankData(year) {
      try {
        const res = await this.$http.get(`data/rank/${year}`);
        this.rankData = res.data.rankData;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
};
</script>

<style scoped>
.row_list {
  width: 100%;
}

.table-wrapper {
  height: 260px; /* 固定高度 */
  overflow: auto; /* 添加滚动条 */
  margin-top: 25px;
}

.ranking-table {
  width: 100%;
  border-collapse: collapse; /* 边框合并 */
}

.ranking-table th,
.ranking-table td {
  border: none;
  padding: 8px; /* 单元格内边距 */
  text-align: center; /* 文本居中 */
}

.ranking-table th {
  background-color: rgba(122, 155, 255, 0.6); /* 标题行背景色 */
  position: sticky;
  top: 0;
  z-index: 1;
}

.ranking-table tbody tr:nth-child(odd) {
  background-color: #fff; /* 奇数行背景色 */
}
</style>
