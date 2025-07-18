// src/store/index.js
import {createStore} from 'vuex';

const store = createStore({
    state() {
        return {
            selectedYear: '2022', // 默认选择的年份为2022
            selectedProvince: "北京",
            buttonText: "数字经济发展指数"
        };
    },
    mutations: {
        setSelectedYear(state, year) {
            state.selectedYear = year
        },
        setSelectedProvince(state, province) {
            state.selectedProvince = province
        },
        setButtonText(state, text) {
            state.buttonText = text
        }
    },
    actions: {
        updateSelectedYear(context, year) {
            context.commit('setSelectedYear', year)
        },
        updateSelectedProvince(context, province) {
            context.commit('setSelectedProvince', province)
        },
        updateButtonText({commit}, text) {
            commit('setButtonText', text)
        }
    },
    getters: {
        selectedYear(state) {
            return state.selectedYear
        },
        selectedProvince(state) {
            return state.selectedProvince
        },
        buttonText(state){
            return state.buttonText
        }

    }
});

export default store;
