<template>
  <div class="map-wrap">
    <div class="map" ref="mapContainer"></div>
  </div>
</template>

<script setup>
import { Map, MapStyle, Marker, config } from "@maptiler/sdk";
import { shallowRef, onMounted, onUnmounted, markRaw, defineProps } from "vue";
import "@maptiler/sdk/dist/maptiler-sdk.css";

const props = defineProps({
    lat: {
      type: Number,
      required: true,
    },
    lng: {
      type: Number,
      required: true,
    },
});

const mapContainer = shallowRef(null);
const map = shallowRef(null);

onMounted(() => {
  config.apiKey = "dFjl4qDz69iuwgehaqfZ";

  const initialState = { lng: props.lng, lat: props.lat, zoom: 16 };

  map.value = markRaw(
    new Map({
      container: mapContainer.value,
      style: MapStyle.STREETS,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom,
    })
  );

  new Marker({ color: "#FF0000" })
    .setLngLat([props.lng, props.lat])
    .addTo(map.value);
}),
  onUnmounted(() => {
    map.value?.remove();
  });
</script>

<style scoped>
.map-wrap {
  position: relative;
  width: 95%;
  height: 30vh;
}

.map {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>
