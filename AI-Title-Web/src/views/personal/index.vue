<template>
  <v-container>
    <v-row>
      <v-col cols="8" offset="2">
        <Person />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Person from "@/views/personal/compontents/Person.vue";

export default {
  name: "Personal",
  components:{
    Person
  }
}
</script>

<style lang="scss" scoped>

</style>
