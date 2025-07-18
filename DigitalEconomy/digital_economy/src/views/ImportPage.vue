<template>
  <div class="row_list">
    <header>
      <h1>数据导入</h1>
    </header>
    <select v-model="selectedTable" style="margin-right: 20px;">
        <option value="infrastructure">基础设施数据</option>
        <option value="digital_industry">数字产业数据</option>
        <option value="industry_integration">产业融合数据</option>
        <option value="development_environment">发展环境数据</option>
        <option value="GDP">各省GDP</option>
        <option value="indicators">数字经济发展指数指标汇总</option>
        <option value="index">数字经济发展指数</option>
    </select>
    <button @click="openFileInput" style="margin-top: 20px;">导入数据</button>
    <input type="file" ref="fileInput" style="display: none;" @change="handleFileUpload">
    <div class="table-wrapper">
      <table class="ranking-table">
        <thead>
          <tr>
            <th>年份</th>
            <th>地区</th>
            <th>基础设施</th>
            <th>数字产业</th>
            <th>产业融合</th>
            <th>发展环境</th>
          </tr>
        </thead>
        <tbody>
        <tr v-for="item in Data" :key="item.rank">
          <td>{{ item.year }}</td>
          <td>{{ item.region }}</td>
          <td>{{ item.infrastructure }}</td>
          <td>{{ item.digital_industry }}</td>
          <td>{{ item.industry_integration }}</td>
          <td>{{ item.development_environment }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      Data: []
    };
  },
  created(){
    this.getData()
  },
  methods: {
    getData() {
      this.$http.get('data/indicators')
        .then(response => {
          this.Data = response.data;
        })
        .catch(error => {
          console.error('Error', error);
        });
    },
     openFileInput() {
      this.$refs.fileInput.click(); // 打开文件选择框
    },
    handleFileUpload(event) {
      const file = event.target.files[0]; // 获取用户上传的文件
      if (!file) return;

      const formData = new FormData();
      formData.append('file', file);

      // 发送文件到后端进行处理
      this.$http.post('data/import', { tableName: this.selectedTable })
    .then(() => {
      console.log('File uploaded successfully');
    })
    .catch(error => {
      console.error('Error uploading file:', error);
    });
    }
  }
};
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

.row_list {
  width: 100%;
}

.table-wrapper {
  height: 860px; /* 固定高度 */
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
