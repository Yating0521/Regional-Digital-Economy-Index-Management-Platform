<template>
  <div class="four-container">
    <div class="fourBorder border1"></div>
    <div class="fourBorder border2"></div>
    <div class="fourBorder border3"></div>
    <div class="fourBorder border4"></div>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "fourAngel",
};
</script>

<style lang="scss" scoped>
.four-container {
  width: 100%;
  height: 5.600rem;
  margin-top: .25rem;
  position: relative;
  box-sizing: border-box;
  background: rgba(75, 139, 247, 0.05);
  box-shadow: 1px 1px 16px #483D8B inset;
  .fourBorder {
    position: absolute;
    width: 10px;
    height: 10px;
  }

  .border1 {
    left: -1px;
    top: -1px;
    border-left: 2px solid #483D8B;
    border-top: 2px solid #483D8B;
  }

  .border2 {
    right: -1px;
    top: -1px;
    border-right: 2px solid #483D8B;
    border-top: 2px solid #483D8B;
  }

  .border3 {
    left: -1px;
    bottom: -1px;
    border-left: 2px solid #483D8B;
    border-bottom: 2px solid #483D8B;
  }

  .border4 {
    right: -1px;
    bottom: -1px;
    border-right: 2px solid #483D8B;
    border-bottom: 2px solid #483D8B;
  }
}
</style>
