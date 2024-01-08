<template>
  <v-app>
    <v-main>
      <HomeView />
    </v-main>
  </v-app>
</template>

<script setup>
import HomeView from './views/HomeView.vue'
</script>

<script>
import axios from 'axios'

export default {
  name:'App',
  setup(){
    return{
      HomeView,
    }
  },

  beforeCreate(){
    this.$store.commit('initStore')
    const token = this.$store.state.user.access
    
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }else{
      axios.defaults.headers.common['Authorization']=''
    }
  }
}

</script>
