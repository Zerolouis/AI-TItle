<template>
  <v-container class="app-container">
    <v-row align="center">
      <!--描述文字输入框-->
      <v-col lg="6" cols="12">
        <v-card elevation="5" class="card-container" rounded>
          <v-card-title>
            描述文字
          </v-card-title>
          <!--分割线-->
          <v-divider></v-divider>
          <v-card-text class="text-container">
            <v-form>
              <v-textarea
                  v-model="form.text"
                  color="teal"
                  counter
                  row-height="15"
                  rows="10"
                  full-width
                  style="margin: 5px;height: 330px"
              >
              </v-textarea>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>

      <!--描述文字输入框-->
      <v-col lg="6" cols="12">
        <v-card elevation="5" class="card-container">
          <v-card-title>
            输入代码
          </v-card-title>
          <!--分割线-->
          <v-divider></v-divider>
          <!--代码输入区-->
          <v-card-text class="code-container">
            <CodeContent/>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row align="center" justify="end">
      <v-col cols="12" align-self="end">
        <div class="buttons">
          <v-btn large color="primary" class="submit-button" @click="handleSubmit">
            生成
          </v-btn>
          <v-btn large color="secondary" @click="handleClear">
            重置
          </v-btn>
        </div>
      </v-col>
    </v-row>


    <v-row>
      <v-col cols="8" lg="4">
        <v-card :loading="status.card" :disabled="status.card" elevation="5" rounded style="height: 400px">
          <v-card-title>
            生成标题
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row no-gutters align="center" justify="center">
                <!--结果1-->
                <v-col cols="8">
                  <v-text-field
                      v-model="result.title_1"
                      outlined
                      label="结果1"
                      clearable
                  ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-btn large color="teal" dark class="search" @click="handleSearch1">
                    搜索
                  </v-btn>
                </v-col>
                <!--结果2-->
                <v-col cols="8">
                  <v-text-field
                      v-model="result.title_2"
                      outlined
                      label="结果2"
                      clearable
                  ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-btn large color="teal" class="search" dark @click="handleSearch2">
                    搜索
                  </v-btn>
                </v-col>
                <!--结果3-->
                <v-col cols="8">
                  <v-text-field
                      v-model="result.title_3"
                      outlined
                      label="结果3"
                      clearable
                  ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-btn large color="teal" class="search" dark @click="handleSearch3">
                    搜索
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
      </v-col>


      <v-col cols="4" lg="2">
        <v-card style="min-height: 400px" elevation="5">
          <v-card-title>
            选择搜索引擎
          </v-card-title>
          <v-chip-group
              active-class="primary--text"
              column
              style="padding: 20px"
              mandatory
              v-model="current"
          >
            <v-chip
                v-for="tag in tags"
                :key="tag.value"
                :value="tag.value"
            >
              <svg-icon style="font-size: 25px" :icon-class="tag.svg" />
            </v-chip>
          </v-chip-group>
        </v-card>
      </v-col>

      <v-col cols="12" lg="4">
        <v-expand-transition>
        <v-card style="height: 400px" transition="scale-transition" elevation="5" :loading="status.card" :disabled="status.card">
          <v-card-title >
            结果预测图
          </v-card-title>
          <Chart v-if="status.chart"/>
        </v-card>
        </v-expand-transition>
      </v-col>


      <v-col cols="12" lg="2">
        <v-expand-transition>
        <v-card style="height: 400px;text-align: center;"  elevation="5" :loading="status.card" :disabled="status.card">
          <v-card-title>
            时间成本分析
          </v-card-title>
          <v-card-text v-if="status.chart">
            <div class="time-title">
              总计耗时:
            </div>
            <div class="time-text">
              {{ result.time }} S
            </div>
          </v-card-text>
        </v-card>
        </v-expand-transition>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import CodeContent from "@/views/smart-title/components/CodeContent.vue";
import Chart from "@/views/smart-title/components/Chart.vue";
import {mapState} from "vuex";

export default {
  name: "smart-title",
  components: {
    CodeContent,
    Chart
  },
  data() {
    return {
      form: {
        text: ''
      },
      tags:[{
        name:'必应',
        value:'www.bing.com/search?q=',
        svg:'biying'
      },{
        name:'百度',
        value: 'www.baidu.com/s?wd=',
        svg:'baidu'
      },{
        name:'搜狗',
        value: 'www.sogou.com/web?query=',
        svg:'sougou'
      }],
      current: 'www.bing.com/search?q='
      // status: {
      //   card: false,
      //   chart: false
      // }
    }
  },
  methods: {
    // 搜索第一条结果
    handleSearch1() {
      window.open('https://'+this.current+this.result.title_1)
    },
    // 搜索第二条结果
    handleSearch2() {
      window.open('https://'+this.current+this.result.title_2)
    },
    // 搜索第三条结果
    handleSearch3() {
      window.open('https://'+this.current+this.result.title_3)
    },
    handleSubmit() {
      this.$store.dispatch('result/syncDesc', this.form.text)
      this.$store.dispatch('result/submit')
    },
    handleClear() {
      this.form.text = ''
    }
  },
  computed: {
    ...mapState('result', ['result','status'])
  }
}
</script>

<style lang="scss" scoped>
.app-container {
  //margin-top: 20px;

  .card-container {
    height: 400px;
  }

  .text-container {
    padding: 0;
  }

  .code-container {
    padding: 0;
  }

  ::v-deep .CodeMirror {
    height: 334px;
  }

  .button-container {
    width: 200px;
  }

  .buttons {
    float: right;

    .submit-button {
      margin-right: 20px;
    }
  }

  .search {
    margin-bottom: 30px;
    margin-left: 20px;
  }

  .time-title {
    margin-top: 80px;
    font-size: 30px;
  }

  .time-text {
    font-size: 40px;
    margin-top: 40px;
  }
}
</style>
