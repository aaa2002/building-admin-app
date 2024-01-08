<template>
  <v-app-bar>
    <v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Buy-A-House</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn :to="{ name: 'profile' }" v-if="activeUser.isAuthenticated" text
      ><v-icon class="mr-2" small>mdi-account</v-icon>
      Profile
    </v-btn>
    <v-btn v-if="activeUser.isAuthenticated" @click="logout" text>
      Log Out
    </v-btn>
    <v-btn v-if="!activeUser.isAuthenticated" :to="{ name: 'login' }" text>
      Log In
    </v-btn>
    <v-btn v-if="!activeUser.isAuthenticated" :to="{ name: 'signup' }" text>
      Register
    </v-btn>
  </v-app-bar>

  <v-navigation-drawer v-model="drawer" app>
    <v-list>
      <v-list-item class="drawer-item">
        <v-btn
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
          :to="{ name: 'home' }"
        >
          <v-icon class="mr-2">mdi-home</v-icon>
          <v-list-item-title>Home</v-list-item-title>
        </v-btn>
      </v-list-item>
      <v-list-item class="drawer-item" v-if="!activeUser.is_staff">
        <v-btn
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
          :to="{ name: 'home' }"
        >
          <v-icon class="mr-2">mdi-account-key</v-icon>
          <v-list-item-title>Admins</v-list-item-title>
        </v-btn>
      </v-list-item>
      <v-list-item class="drawer-item" v-if="activeUser.is_staff">
        <v-btn
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
          :to="{ name: 'home' }"
        >
          <v-icon class="mr-2">mdi-post-outline</v-icon>
          <v-list-item-title>My Posts</v-list-item-title>
        </v-btn>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-container>
    <router-view />
  </v-container>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.commit("removeToken");

      this.$router.push("/login");
    },
  },
};
</script>

<script setup>
import { ref } from "vue";
import { useStore } from "vuex";

const store = useStore();

const activeUser = ref(store.state.user);
const drawer = ref(false);

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};
</script>

<style lang="scss" scoped></style>
