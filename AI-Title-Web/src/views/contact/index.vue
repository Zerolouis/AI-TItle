<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-banner
            single-line
            @click:icon="alert"
        >
          <v-icon
              slot="icon"
              color="blue"
              size="36"
          >
            mdi-information-outline
          </v-icon>
          您可以通过以下方式联系我们

        </v-banner>
      </v-col>
      <v-col cols="5" lg="5" offset="1">
        <ContactCard1 />
      </v-col>
      <v-col cols="5 lg=5">
        <ContactCard2 />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ContactCard1 from "@/views/contact/components/ContactCard1.vue";
import ContactCard2 from "@/views/contact/components/ContactCard2.vue";

export default {
  name: "Contact",
  components: {
    ContactCard1,
    ContactCard2
  }
}
</script>

<style lang="scss" scoped>

</style>
