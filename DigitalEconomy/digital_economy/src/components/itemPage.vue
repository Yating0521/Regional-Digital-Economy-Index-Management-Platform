<template>
  <four-angels>
    <div class="item">
    <slot></slot>
  </div>
  </four-angels>
</template>

<script>
import fourAngels from "@/components/FourAngels.vue";
export default{
components: {
    fourAngels,
  },
}
</script>

<style lang="less">
.item{
    height: 5.600rem;
    //border: 1px solid blue;
    margin: .25rem;
    //background-color:rgba(0,0,255,0.2);
}
</style>