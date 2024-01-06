<template>
  <v-container>
    <v-card>
      <ImageCarroussel :images="images" />
      <v-card-title class="headline">{{ apartment.name }}</v-card-title>
      <v-card-subtitle class="caption"
        >Price: $ {{ apartment.price }}</v-card-subtitle
      >
      <v-card-text>{{ apartment.description }}</v-card-text>
      <Marker :options="{ position: center }" />

      <div class="map-wrapper">
        <MapComponent :lat="mockLat" :lng="mockLng" />
      </div>

      <v-card-actions>
        <v-btn color="primary">Contact</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { computed } from "vue";
import ImageCarroussel from "../components/ImageCarroussel.vue";
import MapComponent from "@/components/MapComponent.vue";

const route = useRoute();
const store = useStore();

const images = [
  "https://media.self.com/photos/630635c30b7f36ce816f374a/2:1/w_1280,c_limit/DAB03919-10470989.jpg",
  "https://chnapartments.com/assets/images/cache/kitchen-and-living-room-a4be940df9ffd81de9014c7fc0f53336.jpg",
  "https://www.bhg.com/thmb/dgy0b4w_W0oUJUxc7M4w3H4AyDo=/1866x0/filters:no_upscale():strip_icc()/living-room-gallery-shelves-l-shaped-couch-ELeyNpyyqpZ8hosOG3EG1X-b5a39646574544e8a75f2961332cd89a.jpg"
];
const mockLat = 46.77121;
const mockLng = 23.623634;

const apartment = computed(() =>
  store.state.apartments.find(
    (apartment) => apartment.id === Number(route.params.id)
  )
);
</script>

<style lang="scss" scoped>
.headline {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
}

.caption {
  font-size: 14px;
  color: grey;
}

.map-wrapper {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}
</style>
