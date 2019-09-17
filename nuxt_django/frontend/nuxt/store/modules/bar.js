const state = () => (
  { data: {} }
)

const mutations = {
  setData(state, val) {
    state.data = val
  }
}

const actions = {
  setData: ({commit}, data) => {
    commit('setData', data)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
}