import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import bar from './modules/bar.js'
import plot from './modules/plot.js'
import pie from './modules/pie.js'
import cloud from './modules/cloud.js'
import pyramid from './modules/pyramid.js'
import sun from './modules/sun.js'
import matrix from './modules/matrix.js'


Vue.use(Vuex)

const store = () => new Vuex.Store({
  modules: {
    bar,
    plot,
    pie,
    cloud,
    pyramid,
    sun,
    matrix
  },
  actions: {
    // 下面是SSR正式部分
    async nuxtServerInit({ commit }, { req, app }) {
        var {data} = await axios.get('http://39.107.86.223:8000/charts/bar')
        commit('bar/setData', data)


        var {data} = await axios.get('http://39.107.86.223:8000/charts/plot')
        commit('plot/setData', data)


        var {data} = await axios.get('http://39.107.86.223:8000/charts/pie')
        commit('pie/setData', data)

        var {data} = await axios.get('http://39.107.86.223:8000/charts/pyramid')
        commit('pyramid/setData', data)

        var {data} = await axios.get('http://39.107.86.223:8000/charts/cloud')
        commit('cloud/setData', data)

        var {data} = await axios.get('http://39.107.86.223:8000/charts/matrix')
        commit('matrix/setData', data)

        var {data} = await axios.get('http://39.107.86.223:8000/charts/sun')
        commit('sun/setData', data)
        console.log(data)

        // const {data} = await axios.get('http://39.107.86.223:8000/charts/bar')
        // commit('charts/setData', data)



    }
  }
})


export default store
