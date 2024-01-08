<template>
  <v-container>
    <v-form @submit.prevent="submitForm">
      <v-tooltip width="200px" location="start">
        <template v-slot:activator="{ props }">
          <v-text-field
            v-bind="props"
            class="mb-4"
            v-model="form.email"
            label="Email"
          ></v-text-field>
        </template>
        <span>Enter your email here</span>
      </v-tooltip>
      <v-text-field
        class="mb-4"
        v-model="form.password"
        label="Password"
        type="password"
      ></v-text-field>

      <v-btn type="submit" color="primary"
        >Log In</v-btn
      >
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data(){
    return{
      form:{
        email:'',
        password:'',
      },
      errors:[]
    }
  },

  methods:{
    async submitForm(){
      await axios
        .post('/api/login/',this.form)
        .then(response =>{
          this.$store.commit('setToken',response.data)
          axios.defaults.headers.common['Authorization']="Bearer " + response.data.access
        })
        .catch(error =>{
          console.log('error',error)
        })

      await axios
        .get('/api/me/')
        .then(response =>{
            this.$store.commit('setUserInfo',response.data)
            this.$router.push('/')
        })
        .catch(error =>{
          console.log('error', error)
        })
    }
  }
}
</script>

<style lang="scss" scoped></style>
