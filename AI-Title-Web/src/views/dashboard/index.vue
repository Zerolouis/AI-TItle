<template>
  <v-container class="dashboard">
    <v-row>
      <v-col cols="12" lg="2">

      </v-col>
      <v-col cols="12" lg="8">
        <v-row>
          <v-col cols="12">
            <div class="title-header">
              欢迎使用AI-title！
            </div>
            <div class="title-text">
              为了提高程序员问答论坛中的问题贴的质量，我们的团队开发了“AI-title：程序员问答论坛标题小助手”。本作品在原有的方法Code2Que的基础上额外考虑了双模态信息，在底层技术上采用了基于Transformer的架构并使用了预训练模型T5。我们的方法使现有自动化标题生成方法更实用、更值得信赖，和同类作品相比有较大的竞争力。
            </div>
          </v-col>
          <v-col cols="12">
            <v-card outlined>
              <v-card-text>
                <div class="technical">
                  <v-icon size="45">
                    mdi-vuejs
                  </v-icon>
                  <div class="tech-container">
                    <div class="tech-header">前端</div>
                    <div class="tech-text">VUE 2</div>
                  </div>
                  <v-icon size="45">
                    mdi-language-python
                  </v-icon>
                  <div class="tech-container">
                    <div class="tech-header">后端</div>
                    <div class="tech-text">Python</div>
                  </div>
                </div>

              </v-card-text>

              <v-card-text>
                我们的作品主要面向企业软件开发人员、高校编程相关专业学生和编程爱好者，你也可以提交反馈帮助我们改善
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12">
            <v-row>
              <v-col cols="6">
                <v-card elevation="1">
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title style="font-size: 40px">
                        1235
                      </v-list-item-title>
                      <v-list-item-subtitle>解决问题数量 - 总计</v-list-item-subtitle>
                    </v-list-item-content>

                    <v-icon class="count-icon" size="40">
                      mdi-sync
                    </v-icon>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="6">
                <v-card elevation="1">
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title style="font-size: 40px">
                        12
                      </v-list-item-title>
                      <v-list-item-subtitle>解决问题数量 - 24H</v-list-item-subtitle>
                    </v-list-item-content>

                    <v-icon class="count-icon" size="40">
                      mdi-clock-time-eight-outline
                    </v-icon>
                  </v-list-item>
                </v-card>
              </v-col>
              <v-col cols="12">
                <v-card elevation="2">
                  <v-card-title >
                    <v-icon>
                      mdi-information
                    </v-icon>
                    <div class="text-h5">公告</div>
                  </v-card-title>
                  <v-card-text>
                    <div style="font-size: 16px">
                      AI-Title 已经正式上线，您可以查看左侧导航栏选择您所需要的功能<p />
                      若在使用过程中遇到问题，您可以提交反馈或与我们联系
                    </div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>

      </v-col>

    </v-row>
  </v-container>
</template>

<script>

export default {
  name: "Dashboard",
  components: {}
}
</script>

<style lang="scss" scoped>
.dashboard {
  .title-header {
    font-size: 35px;
    font-weight: bold;
  }

  .title-text {
    color: rgba(0, 0, 0, 0.5);

  }

  .technical {
    display: flex;

    .tech-container{
      margin-left: 10px;
      margin-right: 30px;
    }
    .tech-header{
      font-weight: bold;
      font-size: 15px;
    }
    .tech-text{
      font-size: 13px;
    }
  }

}
</style>
