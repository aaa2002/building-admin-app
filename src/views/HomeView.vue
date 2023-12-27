<template>
  <div>HOME</div>
</template>

<script setup>
import { ref } from "vue";

const accomodations = ref([]);

const fetchAccomodations = async () => {
  let response = [];
  try {
    response = await fetch("http://localhost:8000/accomodation");
  } catch (error) {
    console.log(error);
  }
  accomodations.value = await JSON.stringify(response);
};

const init = () => {
  fetchAccomodations();
};

init();
</script>

<style lang="scss" scoped></style>
