<template>
  <v-app class="app-container">
      <router-view />
  </v-app>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style lang="scss">
.app-container{
  .bar-title{
    font-size: 20px;
  }
}
</style>
