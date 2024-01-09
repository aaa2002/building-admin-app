<template>
  <v-app-bar>
    <v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Buy-A-House</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
      :to="{ name: 'profile' }"
      v-if="this.$store.state.user.isAuthenticated"
      text
      ><v-icon class="mr-2" small>mdi-account</v-icon>
      Profile
    </v-btn>
    <v-btn v-if="this.$store.state.user.isAuthenticated" @click="logout" text
      >Log Out</v-btn
    >
    <v-btn
      v-if="!this.$store.state.user.isAuthenticated"
      :to="{ name: 'login' }"
      text
      >Log In</v-btn
    >
    <v-btn
      v-if="!this.$store.state.user.isAuthenticated"
      :to="{ name: 'signup' }"
      text
      >Register</v-btn
    >
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
      <v-list-item class="drawer-item" v-if="!this.$store.state.user.is_staff">
        <v-btn
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
          :to="{ name: 'home' }"
        >
          <v-icon class="mr-2">mdi-account-key</v-icon>
          <v-list-item-title>Admins</v-list-item-title>
        </v-btn>
      </v-list-item>
      <v-list-item class="drawer-item">
        <v-btn
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
          :to="{ name: 'apartments' }"
        >
          <v-icon class="mr-2">mdi-post-outline</v-icon>
          <v-list-item-title>My Posts</v-list-item-title>
        </v-btn>
      </v-list-item>
      <v-list-item class="drawer-item">
        <v-btn
          @click="toggleChatDialog"
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
        >
          <v-icon class="mr-2">mdi-chat</v-icon>
          <v-list-item-title>Chat</v-list-item-title>
        </v-btn>
      </v-list-item>
      <v-list-item class="drawer-item">
        <v-btn
          :to="{ name: 'add-building' }"
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
        >
          <v-icon class="mr-2">mdi-office-building</v-icon>
          <v-list-item-title>Add Apartment Building</v-list-item-title>
        </v-btn>
      </v-list-item>
      <v-list-item class="drawer-item">
        <v-btn
          :to="{ name: 'add-apartment' }"
          style="width: 100% !important; justify-content: flex-start"
          :elevation="0"
        >
          <v-icon class="mr-2">mdi-home-floor-a</v-icon>
          <v-list-item-title>Add Apartment</v-list-item-title>
        </v-btn>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-container>
    <router-view />
  </v-container>

  <ChatDialog v-model="chatDialogRef" @send-message="sendMessage" />
</template>

<script>
import axios from "axios";
export default {
  beforeCreate() {
    this.$store.dispatch("initStore");
    const token = this.$store.state.user.access;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },

  methods: {
    logout() {
      this.$store.commit("removeToken");

      this.$router.push("/login");
    },
  },
};
</script>

<script setup>
import { ref, computed } from "vue";
import socketIOClient from "socket.io-client";
import { useStore } from "vuex";
import ChatDialog from "@/components/ChatDialog.vue";

const store = useStore();

const currentUserid = computed(() => store.state.user.id);
const drawer = ref(false);
const message = ref("");
const chatDialogRef = ref(false);

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};

const toggleChatDialog = () => {
  chatDialogRef.value = !chatDialogRef.value;
};

const sendMessage = (sentMessage) => {
  message.value = sentMessage;
  if (message.value.trim() !== "") {
    // Emit a socket event for chat message
    console.log("Sending message from:", currentUserid.value);
    socket.emit("chat message", {
      message: message.value,
      user: currentUserid.value,
    });
    // Clear the input field
    message.value = "";
  }
};

// Connect to the Socket.IO server
const socket = socketIOClient("http://localhost:3000");

// Handle incoming chat messages
socket.on("chat message", (msg) => {
  console.log("Received message:", msg);
  // You can handle the incoming message as needed
  // For example, you may want to display it in the UI
});
</script>

<style lang="scss" scoped></style>
