<template>
  <div class="button">
    <button class="custom-button" @click="handleClick">
      <slot></slot>
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    handleClick(event) {
      let text = event.target.textContent
      this.$store.commit('setButtonText', text)
    }
  }
}
</script>

<style scoped>
.custom-button {
  background-color: rgb(41, 49, 113, 0.8);
  color: azure;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  border: none;
  margin: .20rem;
  width: 140px; /* 按钮的宽度 */
  height: 30px; /* 按钮的高度 */
  box-shadow: 0 0 10px 5px rgb(25, 25, 112, 0.6);
}

.button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}
</style>
