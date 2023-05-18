import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import {colors} from "vuetify/lib";

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#009688',
                secondary: '#3f51b5',
                accent: '#2196f3',
                error: '#f44336',
                warning: '#ff9800',
                info: '#607d8b',
                success: '#4caf50'
            },
            dark: {
                primary: colors.blue.lighten3,
            },
        },
    },
});
