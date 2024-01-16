<template>
  <div class="search-wrapper">
    <v-text-field
      v-model="search"
      :loading="loading"
      density="compact"
      variant="solo"
      label="Search"
      append-inner-icon="mdi-magnify"
      single-line
      hide-details
      @click:append-inner="searchClick"
    ></v-text-field>
  </div>

  <div class="cards my-12">
    <v-card
      class="mb-8"
      v-for="apartment in apartments"
      v-bind:key="apartment.id"
    >
      <v-card-title>{{ apartment.name }}</v-card-title>
      <v-card-subtitle>$ {{ apartment.price }}</v-card-subtitle>
      <v-card-text>{{ apartment.description }}</v-card-text>
      <v-card-actions>
        <v-btn @click="openApartmentView(apartment.name)" text>More</v-btn>
        <v-btn text>Contact</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      apartments: [],
      image: null,
      latLon: { lat: 0, lon: 0 },
    };
  },

  mounted() {
    navigator.geolocation.getCurrentPosition((position) => {
      this.latLon.lat = position.coords.latitude;
      this.latLon.lon = position.coords.longitude;

      this.getApartments();
    });
  },

  methods: {
    getApartments() {
      // axios
      //   .get('api/apartments/')
      //   .then(response => {
      //     console.log('data',response.data)

      //     this.apartments=response.data
      //   })
      //   .catch(error => {
      //     console.log('error',error)
      //   })

      axios
        .post("api/apartments/", {lat: this.latLon.lat, lon: this.latLon.lon})
        .then((response) => {
          console.log("data", response.data);

          this.apartments = response.data;
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
  },
};
</script>

<script setup>
// import { useStore } from "vuex";
import { ref } from "vue";
import { useRouter } from "vue-router";

// const store = useStore();
const router = useRouter();
const loading = ref(false);
const search = ref("");

const searchClick = () => {
  loading.value = true;
  setTimeout(() => {
    loading.value = false;
  }, 1000);
};

// const accomodations = ref([]);

// const fetchAccomodations = async () => {
//   let response = [];
//   try {
//     response = await fetch("http://localhost:8000/accomodation");
//   } catch (error) {
//     console.log(error);
//   }
//   accomodations.value = await JSON.stringify(response);
// };

// const accomodations = computed(() =>
//   store.state.apartments.filter((apartment) =>
//     apartment.name.includes(search.value)
//   )
// );

const openApartmentView = (name) => {
  router.push({ name: "apartment", params: { name: name } });
};

// const init = () => {
//   fetchAccomodations();
// };

// init();
</script>

<style lang="scss" scoped>
.search-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 24px 0;
  background-color: white;
  position: sticky;
  top: 64px;
  z-index: 10;
}
</style>
