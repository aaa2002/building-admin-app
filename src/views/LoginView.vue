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

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();

const form = ref({
  email: "",
  password: "",
});

const submitForm = () => {
  axios
    .post("/api/login", {
      email: form.value.email,
      password: form.value.password,
    })
    .then((response) => {
      console.log(response);
      if (response.data.message === "success") {
        store.commit("setUserInfo", response.data.user);

        router.push({ name: "home" });
      }
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style lang="scss" scoped></style>
