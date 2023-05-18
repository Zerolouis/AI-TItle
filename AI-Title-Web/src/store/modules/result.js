import axios from "axios";

export default {
    namespaced: true,
    state: {
        desc: '',
        code: '',
        incomplete_title: '',
        result:{
            logit: [
                {
                    name: 'C#',
                    value: 0
                },
                {
                    name: 'Java',
                    value: 0
                },
                {
                    name: 'JS',
                    value: 0
                },
                {
                    name: 'Python',
                    value: 0
                }
            ],
            prediction: 'Java',
            time: 0,
            title_1: '',
            title_2: '',
            title_3: ''
        },
        status:{
            card: false,
            chart: false
        }
    },
    actions: {
        // 提交到后端
        submit(context) {
            var value = {
                desc: context.state.desc,
                code: context.state.code,
            }
            context.commit('SUBMIT', value)
        },
        // 同步代码
        syncCode(context, value) {
            context.commit('SYNC_CODE', value)
        },
        // 同步文字描述
        syncDesc(context, value) {
            context.commit('SYNC_DESC', value)
        },
        // 文本
        clear(context) {
            context.commit('CLEAR')
        },
        // 同步状态
        syncStatus(context,value) {
            context.commit(value)
        },
        supply(context){
            var value = {
                desc: context.state.desc,
                code: context.state.code,
                incomplete_title: context.state.incomplete_title
            }
            context.commit('SUPPLY',value)
        },
        syncSupply(context,value){
            context.commit('SYNC_SUPPLY',value)
        }
    },
    mutations: {
        SYNC_SUPPLY(state,value){
            state.incomplete_title = value
        },
        SUPPLY(state,value){
            // 开始加载
            state.status.card = true
            state.status.chart = false
            axios({
                method: 'post',
                url: 'http://127.0.0.1/co',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: value
            }).then((res) => {
                console.log(res.data)
                state.result = res.data
                state.status.card = false
                state.status.chart = true
            })
        },
        SUBMIT(state, value) {
            // 开始加载
            state.status.card = true
            state.status.chart = false
            // 发送请求
            axios({
                method: 'post',
                url: 'http://127.0.0.1/so',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: value
            }).then((res) => {
                console.log(res.data)
                state.result = res.data
                state.status.card = false
                state.status.chart = true
            })
        },
        SYNC_CODE(state, value) {
            state.code = value
        },
        SYNC_DESC(state, value) {
            state.desc = value
        },
        SYNC_STATUS(state,value){
          state.status.card = value
        },
        CLEAR(state) {
            state.desc = ''
            state.code = ''
        }
    }
}
