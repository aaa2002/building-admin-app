<template>
  <div class="carousel">
    <div class="image-container" @click="openDialog">
      <img :src="currentImage" :alt="`Image ${currentIndex + 1}`" />
    </div>
    <div class="controls">
      <v-btn :elevation="0" @click="prevImage" :disabled="currentIndex === 0">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-btn
        :elevation="0"
        @click="nextImage"
        :disabled="currentIndex === images.length - 1"
      >
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </div>

    <v-dialog v-model="dialog" max-width="800">
      <v-img :src="currentImage" :alt="`Image ${currentIndex + 1}`" />
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, watch, defineProps } from "vue";

const props = defineProps({
  images: {
    type: Array,
    required: true,
  },
});

// Current index of the displayed image
const currentIndex = ref(0);

// Current image URL based on the currentIndex
const currentImage = ref(props.images[currentIndex.value]);

// Dialog state
const dialog = ref(false);

// Watch for changes in the currentIndex and update the currentImage
watch(
  () => currentIndex.value,
  () => {
    currentImage.value = props.images[currentIndex.value];
  }
);

// Function to navigate to the previous image
const prevImage = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  }
};

// Function to navigate to the next image
const nextImage = () => {
  if (currentIndex.value < props.images.length - 1) {
    currentIndex.value++;
  }
};

// Function to open the dialog
const openDialog = () => {
  dialog.value = true;
};
</script>

<style lang="scss" scoped>
.carousel {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.image-container {
  margin-bottom: 16px;
  width: 100%;
  height: 400px;
  cursor: pointer;
}

img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  transition: transform 0.5s ease-in-out;

  &:hover {
    transform: scale(1.05);
    transition: transform 0.5s ease-in-out;
  }
}

.controls {
  display: flex;
  gap: 16px;
}

button {
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
}
</style>
