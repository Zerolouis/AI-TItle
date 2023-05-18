<template>
  <div v-loading="!show" style="min-height: 400px;height: 100%">
    <!--2.这里id对应new Vditor('vditor',{...})的第一个参数vidtor-->
    <div id="vditor" />
  </div>
</template>

<script>
import Vditor from 'vditor'
import 'vditor/dist/index.css'

export default {
  name: 'Markdown',
  data() {
    return {
      contentEditor: {}, // 3.声明一个变量,
      show: true
    }
  },
  mounted() {
    this.contentEditor = new Vditor('vditor', { // 4.刚刚声明的变量contentEditor被赋值为一个Vditor实例,
      height: '600px',
      placeholder: '您可以在这写下反馈或建议...',
      theme: 'classic',
      counter: {
        enable: true,
        type: 'markdown'
      },
      preview: {
        delay: 0,
        hljs: {
          style: 'monokai',
          lineNumber: true
        }
      },
      tab: '\t',
      typewriterMode: true,
      toolbarConfig: {
        pin: true
      },
      cache: {
        enable: false
      },
      mode: 'sv',
      toolbar: [
        'emoji',
        'headings',
        'bold',
        'italic',
        'strike',
        'link',
        '|',
        'list',
        'ordered-list',
        'check',
        'outdent',
        'indent',
        '|',
        'quote',
        'line',
        'code',
        'inline-code',
        'insert-before',
        'insert-after',
        '|',
        // 'record',
        'table',
        '|',
        'undo',
        'redo',
        '|',
        'edit-mode',
        // 'content-theme',
        'code-theme',
        'export',
        {
          name: 'more',
          toolbar: [
            'fullscreen',
            'both',
            'preview',
            'info',
            'help'
          ]
        }]
    })
  },
  methods:{
    handleSubmit(){

    }
  }
}
</script>

<style lang="scss" scoped>

</style>
