<template>
    <v-app>
        <v-container>
      <v-form @submit.prevent="submitForm">
        <v-text-field v-model="form.name" label="Name"></v-text-field>
        <v-text-field v-model="form.email" label="Email"></v-text-field>
        <v-text-field v-model="form.password1" label="Password" type="password"></v-text-field>
        <v-text-field v-model="form.password2" label="Password" type="password"></v-text-field>
    <template v-if="errors">
        <div class="bg-red-300 text-white">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
    </template>

        <v-btn type="submit" color="primary">Sign Up</v-btn>
      </v-form>

      <router-view />
    </v-container>
  </v-app>
 </template>

<script>
import axios from 'axios';

export default {
    setup(){
    },

    data(){
        return{
            form:{
                email:'',
                name:'',
                password1:'',
                password2:'',
            },
            errors: [],
        }
    },

    methods: {
        submitForm(){
            this.errors=[]

            if (this.form.email ===''){
                this.errors.push("Enter a email")
            }

            if (this.form.name ===''){
                this.errors.push("Enter a name")
            }
            
            if (this.form.password1 ===''){
                this.errors.push("Enter a password")
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.push("Passwords do not match")
            }

            if (this.errors.length === 0){
                axios
                    .post('/api/signup/',this.form)
                    .then (response => {
                        if(response.data.message === 'success'){
                            console.log("Connected")
                            console.log(this.form)
                            this.form.email=''
                            this.form.name=''
                            this.form.password1=''
                            this.form.password2=''

                        }else{
                            console.log("failed to post")
                        }

                    })
                    .catch(error => {
                        console.log('error',error)
                    })
            }
        }
    }
}

</script>