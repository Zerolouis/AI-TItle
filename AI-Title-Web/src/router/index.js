import Router from 'vue-router'

import Layout from "@/views/layout"
import Login from "@/views/login"

export default new Router({
    routes: [
        {
            path: '/',
            component: Layout,
            redirect: '/login',
            children: [{
                path: 'dashboard',
                name: 'Dashboard',
                component: () => import('@/views/dashboard/index'),
                meta: {title: '生成标题'}
            }, {
                path: 'generate',
                name: 'Generate',
                component: () => import('@/views/smart-title/index'),
                meta: {title: '生成标题'}
            }, {
                path: 'supply',
                name: 'Supply',
                component: () => import('@/views/smart-title/supply.vue'),
                meta: {title: '补全标题'}
            }, {
                path: 'feedback',
                name: 'Feedback',
                component: () => import('@/views/feedback/index.vue'),
                meta: {title: '提交反馈'}
            }, {
                path: 'contact',
                name: 'Contact',
                component: () => import('@/views/contact/index.vue'),
                meta: {title: '联系我们'}
            },{
                path:'setting',
                name: 'Setting',
                component: () => import('@/views/personal/index.vue'),
                meta:{title: '设置'}
            }]
        },
        {
            path: '/login',
            component: Login,
            meta:{title:'登录'}
        }
    ]
})
