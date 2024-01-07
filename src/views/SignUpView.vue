<template>
  <v-container>
    <v-snackbar v-model="snackbar" :timeout="timeout" color="green">
      Success

      <template v-slot:actions>
        <v-btn variant="text" @click="snackbar = false"> Close </v-btn>
      </template>
    </v-snackbar>

    <v-form @submit.prevent="submitForm">
      <v-text-field
        class="mb-4"
        v-model="form.name"
        label="Name"
        :rules="[(v) => !!v || 'Name is required']"
      ></v-text-field>
      <v-text-field
        class="mb-4"
        v-model="form.email"
        label="Email"
        :rules="emailRules"
      ></v-text-field>
      <v-text-field
        class="mb-4"
        v-model="form.password1"
        :rules="passwordRules"
        label="Password"
        type="password"
      ></v-text-field>
      <v-text-field
        class="mb-4"
        v-model="form.password2"
        :rules="passwordRules"
        label="Password"
        type="password"
      ></v-text-field>

      <v-btn type="submit" color="primary" :disabled="!isFormValid"
        >Sign Up</v-btn
      >
    </v-form>
  </v-container>
</template>

<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();

const passwordRules = [
  (v) => !!v || "Password is required",
  (v) => v.length >= 8 || "Password must be at least 8 characters",
  (v) => v === form.value.password1 || "Passwords must match",
];
const emailRules = [
  (v) => !!v || "E-mail is required",
  (v) => /.+@.+/.test(v) || "E-mail must be valid",
];

const isFormValid = computed(() => {
  return (
    emailRules.every((rule) => rule(form.value.email) === true) &&
    passwordRules.every((rule) => rule(form.value.password1) === true) &&
    passwordRules.every((rule) => rule(form.value.password2) === true)
  );
});

const snackbar = ref(false);
const form = ref({
  email: "",
  name: "",
  password1: "",
  password2: "",
});

const errors = ref([]);

const submitForm = () => {
  errors.value = [];

  if (form.value.email === "") {
    errors.value.push("Enter an email");
  }

  if (form.value.name === "") {
    errors.value.push("Enter a name");
  }

  if (form.value.password1 === "") {
    errors.value.push("Enter a password");
  }

  if (form.value.password1 !== form.value.password2) {
    errors.value.push("Passwords do not match");
  }

  if (errors.value.length === 0) {
    axios
      .post("/api/signup/", form.value)
      .then((response) => {
        console.log(response);
        if (response.data.message === "success") {
          console.log("Connected");
          console.log(form.value);
          form.value.email = "";
          form.value.name = "";
          form.value.password1 = "";
          form.value.password2 = "";
          snackbar.value = true;
          setTimeout(() => {
            router.push({ name: "login" });
          }, 2000);
        } else {
          console.log("Failed to post");
        }
      })
      .catch((error) => {
        console.log("Error", error);
      });
  }
};
</script>
