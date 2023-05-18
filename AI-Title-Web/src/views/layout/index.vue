<template>
  <v-app class="app-container">

    <!--顶栏-->
    <v-app-bar
        :clipped-left="primaryDrawer.clipped"
        color="primary"
        app
    >
      <v-app-bar-nav-icon
          v-if="primaryDrawer.type !== 'permanent'"
          @click.stop="primaryDrawer.model = !primaryDrawer.model"
          style="color: white"
      ></v-app-bar-nav-icon>
      <v-toolbar-title style="color: white">{{ items[currentTab].text }}</v-toolbar-title>

      <v-spacer />

      <!--头像菜单-->
      <v-menu :absolute-y="200" offset-y auto  min-width="200" absolute max-height="350">
        <template v-slot:activator="{ on, attrs }">
          <v-avatar v-on="on" v-bind="attrs">
            <img
                src="https://cdn.sep.cc/avatar/be9cfff2b27afb56b75eccde7e6e5778?d=identicon"
                alt="Zerolouis"
            >
          </v-avatar>
        </template>
        <v-list dense >
          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="text-h6">
                Zerolouis
              </v-list-item-title>
              <v-list-item-subtitle>wxjjuju@163.com</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item-group
              v-model="currentMenu"
              color="primary"
          >
            <v-list-item
                v-for="(item, i) in menus"
                :key="i"
            >
              <v-list-item-icon>
                <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
              <v-spacer />
              <v-list-item-icon>
                <v-icon>mdi-menu-right</v-icon>
              </v-list-item-icon>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-menu>

    </v-app-bar>

    <!--侧边栏-->
    <v-navigation-drawer
        v-model="primaryDrawer.model"
        :clipped="primaryDrawer.clipped"
        :floating="primaryDrawer.floating"
        :mini-variant="primaryDrawer.mini"
        :permanent="primaryDrawer.type === 'permanent'"
        :temporary="primaryDrawer.type === 'temporary'"
        app
        overflow
    >
      <v-sheet
          color="grey lighten-4"
          class="pa-4"
          height="160"
      >
        <div class="logo-container">
          <v-img src="@/assets/logo.png" alt="smart-title" class="logo">
          </v-img>
          <div class="title-text">AI Title</div>
        </div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list shaped>
        <v-list-item-group
            v-model="currentTab"
            color="primary"
        >
          <v-list-item
              v-for="(item, i) in items"
              :key="i"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main class="main-content">
      <v-container fluid class="height-100pc">
        <transition name="slide-left" appear>
          <router-view class="main-router-view" :key="key"/>
        </transition>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: "Layout",
  data: () => ({
    drawer: null,
    items: [
      {text: '首页', icon:'mdi-bulletin-board',value: 'Dashboard'},
      {text: '生成标题', icon: 'mdi-view-dashboard', value: 'Generate'},
      {text: '标题补全', icon: 'mdi-file-edit-outline', value: 'Supply'},
      {text: '提交反馈', icon: 'mdi-tooltip-edit-outline', value: 'Feedback'},
      {text: '联系我们', icon: 'mdi-information-outline', value: 'Contact'}
    ],
    menus:[
      {text:'去首页',icon:'mdi-bulletin-board',value: 'Dashboard'},
      {text:'设置',icon:'mdi-cog', value: 'Setting'},
    ],
    primaryDrawer: {
      model: null,
      type: 'default (no property)',
      clipped: false,
      floating: false,
      mini: false,
    },
    currentTab: 0,
    currentMenu: 0,
    offset:true
  }),
  computed: {
    key() {
      return this.$route.path
    }
  },
  watch: {
    currentTab: {
      immediate: true,
      handler(newValue){
        this.$router.push({name: this.items[newValue].value})
      }
    },
    currentMenu(newValue,oldValue){
      if(newValue === undefined){
        this.currentMenu = oldValue
      }else {
        this.$router.push({name:this.menus[this.currentMenu].value})
      }
    }
  }
}
</script>

<style lang="scss" scoped>

.logo-container {

  justify-content: center;
  align-items: center;
  text-align: center;

  .logo {
    width: 60px;
    margin: 10px auto auto;
  }

  .title-text {
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px;
  }
}


.main-content {
  background-image: linear-gradient(135deg, #ffffff 10%, rgba(218, 224, 250, 0.83) 100%);
}

.slide-right-enter-active,
.slide-right-leave-active {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  width: 100%;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: hidden;
}

.slide-right-enter /* .fade-leave-active in below version 2.1.8 */
{
  opacity: 0;
  top: 0;
  transform: translateX(100%);
}

.slide-right-leave-to /* .fade-leave-active in below version 2.1.8 */
{
  opacity: 0;
  top: 0;
  transform: translateX(-100%);
}

.slide-left-enter-active,
.slide-left-leave-active {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  width: 100%;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: hidden;
}

.slide-left-enter /* .fade-leave-active in below version 2.1.8 */
{
  opacity: 0;
  top: 0;
  transform: translateX(-100%);
}

.slide-left-leave-to /* .fade-leave-active in below version 2.1.8 */
{
  display: none;
  opacity: 0;
  top: 0;
  transform: translateX(100%);
}
</style>
