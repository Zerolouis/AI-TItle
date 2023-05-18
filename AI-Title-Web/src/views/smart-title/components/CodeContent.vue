<template>
  <div>
    <div class="code-mirror">
      <!-- or to manually control the datasynchronization（或者手动控制数据流，需要像这样手动监听changed事件） -->
      <codemirror
          ref="myCm"
          :options="cmOptions"
          :value="code"
          @focus="onCmFocus"
          @input="onCmCodeChange"
          @ready="onCmReady"
      />
    </div>
  </div>
</template>

<script>
import {codemirror} from 'vue-codemirror'
import './settings'

export default {
  name: "CodeContent",
  components: {
    codemirror
  },
  data() {
    return {
      cmOptions: {
        // codemirror options
        tabSize: 4,
        mode: 'text/x-java',
        theme: 'eclipse',
        lineNumbers: true,
        line: true
        // more codemirror options, 更多 codemirror 的高级配置...
      },
      height: 800,
      codeOptions: [{
        value: 'text/x-c++src',
        label: 'C++'
      }, {
        value: 'text/x-java',
        label: 'JAVA'
      }, {
        value: 'text/x-csrc',
        label: 'C'
      }, {
        value: 'text/x-csharp',
        label: 'C#'
      }, {
        value: 'text/x-python',
        label: 'Python'
      }, {
        value: 'text/javascript',
        label: 'JavaScript'
      }]
    }
  }, mounted() {
    console.log('this is current codemirror object', this.codemirror)
    // you can use this.codemirror to do something...
  },
  methods: {
    onCmReady(cm) {
      console.log('the editor is readied!', cm)
    },
    onCmFocus(cm) {
      console.log('the editor is focus!', cm)
    },
    onCmCodeChange(newCode) {
      console.log('this is new code', newCode)
      this.code = newCode
      this.$store.dispatch('result/syncCode', this.code)
    }
  },
  computed: {
    code: {
      get() {
        return this.$store.state.result.code
      },
      set() {
        this.$store.dispatch('result/syncCode', this.code)
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
