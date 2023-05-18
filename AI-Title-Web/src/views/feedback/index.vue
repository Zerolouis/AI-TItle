<template>
  <v-container>
    <v-row>

      <v-col cols="12">
        <v-alert
            color="green"
            dismissible
            elevation="5"
            type="success"
            v-if="showTip"
        >提交成功</v-alert>
      </v-col>

      <v-col cols="12">
        <v-alert
            border="top"
            colored-border
            type="info"
            elevation="2"
        >
          若您遇上了什么问题，可以在这里提交反馈
        </v-alert>
      </v-col>

      <v-col cols="12">
        <Markdown />
      </v-col>
      <v-col cols="12">
        <div class="buttons">
          <v-btn large color="primary" :loading="loading" class="submit-button" @click="handleSubmit">
            提交
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Markdown from "@/views/feedback/components/Markdown.vue";

export default {
  name: "Feedback",
  components:{
    Markdown
  },
  data(){
    return{
      showTip: false,
      loading: false
    }
  },
  methods:{
    handleSubmit(){
      this.loading = true

      setTimeout(()=>{
        this.showTip = true
        this.loading = false
      },3000)

    }
  }
}
</script>

<style lang="scss" scoped>
.buttons {
  float: right;

  .submit-button {
    margin-right: 20px;
  }
}
</style>
