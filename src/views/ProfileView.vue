<template>
  <v-container>
    <v-card>
      <v-card-title class="headline">Profile</v-card-title>
      <v-card-text>
        <v-row>
          <v-col>
            <v-subheader>Name: </v-subheader>
            <v-body-1>{{ activeUser.name || "Oops! Problems" }}</v-body-1>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-subheader>Email: </v-subheader>
            <v-body-1>{{ activeUser.email || "Oops! Problems" }}</v-body-1>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-subheader>Role: </v-subheader>
            <v-body-1>{{ getUserRole() || "Oops! Problems" }}</v-body-1>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { useStore } from "vuex";

const store = useStore();
const activeUser = store.state.user;

const getUserRole = () => {
  if (activeUser.is_staff !== null) {
    return activeUser.is_staff === true ? "Admin" : "User";
  }
  return "Oops! Problems";
};
</script>

<style scoped></style>
