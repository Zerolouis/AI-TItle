<template>
  <v-card
      class="mx-auto"
  >
    <v-card-title>
      个人资料
    </v-card-title>

    <v-divider inset></v-divider>

    <v-list two-line>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-camera-account
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>
            <v-avatar>
              <img
                  src="https://cdn.sep.cc/avatar/be9cfff2b27afb56b75eccde7e6e5778?d=identicon"
                  alt="Zerolouis"
              >
            </v-avatar>
          </v-list-item-title>
        </v-list-item-content>

        <v-list-item-icon>
          <v-icon>mdi-pencil</v-icon>
        </v-list-item-icon>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-account-box
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Zerolouis</v-list-item-title>
          <v-list-item-subtitle>用户名</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-icon>
          <v-icon>mdi-pencil</v-icon>
        </v-list-item-icon>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon color="indigo">
            mdi-lock
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>重置密码</v-list-item-title>
        </v-list-item-content>

        <v-list-item-icon>
          <v-icon>mdi-pencil</v-icon>
        </v-list-item-icon>
      </v-list-item>

      <v-divider inset></v-divider>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: "ContactCard"
}
</script>

<style lang="scss" scoped>
.title {
  position: relative;
  top: 100px;
  left: 100px;
}
</style>
