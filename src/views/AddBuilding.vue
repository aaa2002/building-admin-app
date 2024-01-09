<template>
  <v-form @submit.prevent="addBuilding">
    <v-text-field
      v-model="formData.address"
      label="Address"
      required
    ></v-text-field>
    <v-btn type="submit">Add Building</v-btn>
  </v-form>
</template>

<script setup>
import { ref, computed } from "vue";
// import axios from "axios";
import { useStore } from "vuex";

const store = useStore();

const currentUserid = computed(() => store.state.user.id);
// const coordinates = ref({ lat: 0, lng: 0 });

const formData = ref({
  address: "",
  admin: currentUserid.value,
  neighborhood: "",
  lat: 0,
  lng: 0,
});

const setCoordinates = async (stringAddress) => {
    const resp = await fetch(`https://geocode.maps.co/search?q=${stringAddress}&api_key=659bf8b7560ad296056429efj2042ee`);
    const data = await resp.json();
    formData.value.lat = data[0].lat;
    formData.value.lng = data[0].lon;
    console.log(formData.value);
};

const addBuilding = () => {
  setCoordinates(formData.value.address);
  console.log(formData.value);
};
</script>

<style lang="scss" scoped></style>
