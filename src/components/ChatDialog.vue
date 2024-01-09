<template>
    <v-dialog width="1000">
      <template v-slot:default="{ isActive }">
        <v-card title="Dialog">
          <v-col class="mx-4 my-4">
            <v-container ref="chatContainer" class="chat-container container mb-4">
              <v-row v-for="message in messagesArray" :key="message.id">
                <v-col>
                  <v-card>
                    <v-card-title>{{ message.sender }}</v-card-title>
                    <v-card-text>{{ message.message }}</v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
  
            <v-container class="container">
              <v-row>
                <v-text-field v-model="message"></v-text-field>
                <v-btn @click="sendMessage" class="send-btn">Send</v-btn>
              </v-row>
            </v-container>
          </v-col>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text="Close Dialog" @click="isActive.value = false"></v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
  </template>
  
  <script setup>
  import { ref, defineEmits, onMounted, watch } from "vue";
  import axios from "axios";
  
  const message = ref("");
  const messagesArray = ref([]);
  const chatContainer = ref(null);
  
  const sendMessage = () => {
    emit("send-message", message.value);
    message.value = "";
    setTimeout(() => {
      fetchMessages();
    }, 100);
  };
  
  const emit = defineEmits(["send-message"]);
  
  const fetchMessages = () => {
    axios.get("http://localhost:3000/api/messages").then((res) => {
      messagesArray.value = res.data;
      scrollToBottom();
    });
  };
  
  const scrollToBottom = () => {
    // Use scrollIntoView to scroll to the bottom
    if (chatContainer.value) {
      chatContainer.value = chatContainer.value.scrollHeight;
    }
  };
  
  onMounted(() => {
    fetchMessages();
  });

  watch(messagesArray, () => {
    scrollToBottom();
  });
  </script>
  
  <style lang="scss" scoped>
  .chat-container {
    height: 300px;
    overflow-y: scroll;
    border: 1px solid #555;
  }
  
  .container {
    width: 800px;
  }
  
  .send-btn {
    margin-left: 10px;
    height: 56px;
    background-color: rgb(0, 174, 255);
    color: white;
  }
  </style>
  