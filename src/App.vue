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

export default {
  name:'App',
  components:{
    HomeView
  },
}

</script>
