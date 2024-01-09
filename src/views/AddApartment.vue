<template>
  <v-form @submit.prevent="addApartment">
    <v-text-field v-model="formData.name" label="Name" required></v-text-field>
    <v-text-field
      v-model="formData.price"
      label="Price"
      required
    ></v-text-field>
    <v-text-field
      v-model="formData.description"
      label="Description"
      required
    ></v-text-field>
    <v-text-field v-model="formData.area" label="Area" required></v-text-field>
    <v-select
      v-model="formData.building"
      :items="buildings"
      item-title="address"
      item-value="id"
      label="Building"
    ></v-select>
    <v-file-input
      :accept="['.jpg', '.png', '.jpeg']"
      label="Click here to select an image"
      outlined
      v-model="formData.image"
    >
    </v-file-input>
    <v-btn type="submit">Add Apartment</v-btn>
  </v-form>
</template>

<script setup>
import { ref /*, computed*/ } from "vue";
import axios from "axios";

const buildings = ref([]);

const formData = ref({
  name: "",
  price: 0.0,
  description: "",
  area: 0.0,
  image: null,
  building: "",
});

const addApartment = () => {
  axios.post("http://localhost:8000/api/add/apartment/", formData.value);
};

const init = () => {
  axios.get("http://localhost:8000/api/buildings/").then((resp) => {
    console.log(resp.data);
    buildings.value = resp.data;
    console.log(buildings.value);
  });
};

init();
</script>

<style lang="scss" scoped></style>
