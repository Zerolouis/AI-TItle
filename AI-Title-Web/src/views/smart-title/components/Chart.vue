<template>
<v-container>
  <div style="height: 350px;width: 100%;margin-bottom: 50px" ref="chart"></div>
</v-container>
</template>

<script>
import {mapState} from "vuex";
import * as echarts from 'echarts';
let Echarts = require('echarts/lib/echarts') // 基础实例

export default {
  name: 'Chart',
  data(){
    return{
      option:{
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: '结果预测图',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center',
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: 1048, name: 'Search Engine' },
              { value: 735, name: 'Direct' },
              { value: 580, name: 'Email' },
              { value: 484, name: 'Union Ads' },
              { value: 300, name: 'Video Ads' }
            ]
          }
        ]
      }
    }
  },
  computed:{
    ...mapState('result',['result'])
  },
  watch:{
    result:{
      deep: true, // 深度监视
      immediate:true,
      handler(newValue){
        this.option.series[0].data = newValue.logit
        // this.clearChart()
        this.initChart()
      }
    }
  },
  methods:{
    initChart(){
      this.chart = Echarts.init(this.$refs.chart)
      this.chart.setOption(this.option)
    },
    // clearChart(){
    //   this.chart.clear()
    // }
  },
  mounted() {
    this.initChart()
  }
}
</script>

<style lang="scss" scoped>

</style>
