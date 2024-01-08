<template>
  <v-container>
    <v-card v-if="apartment">
      <ImageCarroussel :images="images" />
      <v-card-title class="headline">{{ apartment.name }}</v-card-title>
      <v-card-subtitle class="caption">Price: $ {{ apartment.price }}</v-card-subtitle>
      <v-card-text>{{ apartment.description }}</v-card-text>
      <Marker :options="{ position: center }" />

      <!-- <div class="map-wrapper">
        <MapComponent :lat="apartment.building.lat" :lng="apartment.building.lng" />
      </div> -->

      <v-card-actions>
        <v-btn color="primary">Contact</v-btn>
      </v-card-actions>
    </v-card>
    <v-alert v-else-if="apartment === false" type="error">Apartment not found</v-alert>
    <v-alert v-else type="error">Error loading apartment data</v-alert>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      apartment: null,
      images:[]
      
    };
  },
  mounted() {
    this.getApartment();
  },
  methods: {
    getApartment() {
      const name = this.$route.params.name;
      axios
        .get(`api/apartments/${name}`)
        .then(response => {
          console.log('data', response.data.apartment);
          this.apartment = response.data.apartment;
          this.images.push(this.apartment.images)
        })
        .catch(error => {
          console.log('error', error);
          this.apartment = false; // Mark apartment as not found
        });
    }
  }
};
</script>

<!-- ... rest of the code remains unchanged ... -->
