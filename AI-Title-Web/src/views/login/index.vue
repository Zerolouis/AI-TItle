<template>
  <div id="app">
      <v-app id="inspire">
        <v-main>
          <v-container
              class="fill-height"
              fluid
          >
            <v-row
                align="center"
                justify="center"
            >
              <v-col
                  cols="12"
                  sm="8"
                  md="4"
              >
                <v-card class="elevation-12">
                  <v-toolbar
                      color="primary"
                      dark
                      flat
                  >
                    <v-toolbar-title>AI-Title 登录</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-btn
                            :href="source"
                            icon
                            large
                            target="_blank"
                            v-on="on"
                        >
                          <v-icon>mdi-code-tags</v-icon>
                        </v-btn>
                      </template>
                      <span>Source</span>
                    </v-tooltip>
                  </v-toolbar>
                  <v-card-text>
                    <v-form>
                      <v-text-field
                          label="用户名"
                          name="login"
                          prepend-icon="mdi-account"
                          type="text"
                      ></v-text-field>

                      <v-text-field
                          id="password"
                          label="密码"
                          name="password"
                          prepend-icon="mdi-lock"
                          type="password"
                      ></v-text-field>
                    </v-form>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn color="secondary" @click="handleLogin">注册</v-btn>
                    <v-btn color="primary" @click="handleLogin" :loading="loading">登录</v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-main>
      </v-app>

  </div>
</template>

<script>
export default {
  name: "index",
  props:{
    source: String
  },
  data(){
    return{
      loading:false
    }
  },
  methods:{
    handleLogin(){
      this.loading = true
      setTimeout(()=>{
        this.$router.push({
          path:'/dashboard'
        })
      },1000)

    }
  }
}
</script>

<style lang="scss" scoped>
#inspire{
  background: url("@/assets/stars-7827129.jpg") no-repeat center;
  background-size: cover;
}
</style>
