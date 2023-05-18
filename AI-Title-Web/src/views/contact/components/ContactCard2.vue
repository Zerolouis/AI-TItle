<template>
  <v-card
      max-width="375"
      class="mx-auto"
  >
    <v-img
        :src='require("@/assets/ocean-2203720.jpg")'
        height="300px"
        dark
    >
      <v-row class="fill-height">
        <v-card-title>
              <div class="text-h4 pt-12 title">
                站长
              </div>
        </v-card-title>
      </v-row>
    </v-img>

    <v-list two-line>
      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-phone
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>(+86) 18627427362</v-list-item-title>
          <v-list-item-subtitle>手机</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-icon>
          <v-icon>mdi-message-text</v-icon>
        </v-list-item-icon>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-wechat
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>vme50</v-list-item-title>
          <v-list-item-subtitle>微信</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-qqchat
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>1235223485</v-list-item-title>
          <v-list-item-subtitle>QQ</v-list-item-subtitle>
        </v-list-item-content>

      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-email
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>test@gmail.com</v-list-item-title>
          <v-list-item-subtitle>工作邮箱</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-map-marker
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>南通大学啬园校区</v-list-item-title>
          <v-list-item-subtitle>江苏省南通市狼山镇街道</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: "ContactCard"
}
</script>

<style lang="scss" scoped>
.title{
  position: relative;
  top: 100px;
  left: 100px;
}
</style>
