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
      :items="['b1', 'b2']"
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
// name
// price
// description
// area
// image
// building
import { ref /*, computed*/ } from "vue";
//   import { useStore } from "vuex";

//   const store = useStore();

//   const currentUserid = computed(() => store.state.user.id);

const formData = ref({
  name: "",
  price: 0.0,
  description: "",
  area: 0.0,
  image: null,
  building: "",
});

const addApartment = () => {
  console.log(formData.value);
};
</script>

<style lang="scss" scoped></style>
