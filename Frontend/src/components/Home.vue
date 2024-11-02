<template>
    <div class="p-7 mt-4">
        <!-- Categories Section -->
        <div class="text-2xl mb-3 -mt-6">
            <h1>CATEGORIES</h1>
            <div class="grid grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3 p-2">
                <button v-for="category in categories" :key="category.name" :style="{ backgroundColor: category.color }"
                    class="category-item flex justify-between items-center xl:h-10 2xl:h-10 3xl:h-12   rounded-md transition-all duration-300">
                    <p class="ml-3 text-white">{{ category.name }}</p>
                    <span class="material-symbols-outlined size-10 mt-3">{{ category.icon }}</span>
                </button>
            </div>
        </div>
        <!-- Suggestion Carousel -->
        <div class="text-2xl h-full w-full mt-2">
            <h1>SUGGESTION</h1>
            <div class="swiper sliderWrapper">
                <swiper :slidesPerView="slidex" :grid="{ rows: rowx, fill: 'row' }" :spaceBetween="1"
                    :pagination="{ clickable: false }" :modules="[Grid , Pagination]" class="mySwiper">
                    <swiper-slide v-for="item in suggestion" :key="item.title">
                        <div
                            class="bg-zinc-800 flex flex-col m-2 flex-grow-0 items lg:flex-row rounded-md overflow-hidden 3xl:h-52 2xl:h-50">
                            <div class="flex-shrink-0 m-3">
                                <img class=" border-4 rounded-md xl:w-32 lg:h-40 2xl:h-40 border-zinc-600"
                                    src="/SneX.jpg" alt="" />
                                <div class="flex justify-center mt-0.5">
                                    <div
                                        class="flex justify-center content-center bg-sky-600/30 text-sky-600 text-md rounded-md translate-y-1 w-4/5">
                                        <h1 class="text-sm">{{ item.category }}</h1>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col mt-2 m-5 ml-2 mb-3 w-full">
                                <div class="text-sky-500 h-full font-semibold mt-2 text-2xl md:text-xl md:mb-0 ">
                                    {{ item.title }}
                                </div>
                                <div class="flex flex-wrap items-center md:translate-y-2 ">
                                    <div class="flex items-center text-med mr-6 ">
                                        <box-icon class="mt-0.5 md:size-5" name="notepad" color="white"></box-icon>
                                        <p class="ml-1 md:text-md md:mt-2">{{ item.pages }} pages</p>
                                    </div>
                                    <div class="flex items-center text-med">
                                        <box-icon class="mt-0.5 md:size-5" name="calendar" color="white"></box-icon>
                                        <p class="ml-1 md:text-md md:mt-2">{{ item.date }}</p>
                                    </div>
                                </div>
                                <div class="text-sky-600 text-sm font-sans mt-1 mb-3 ">
                                    <a class="md:text-md">@{{ item.publisher }}</a>
                                </div>
                                <div
                                    class="bg-zinc-600/50 flex justify-between px-4 py-2 rounded-md md:h-8 md:w-auto md:text-sm md:mr-8 ">
                                    <div class="flex items-center">
                                        <box-icon class="size-5" type="solid" name="heart-circle"
                                            color="white"></box-icon>
                                        <p class="ml-1 mt-0.5">{{ item.likes }}</p>
                                    </div>
                                    <div class="flex items-center">
                                        <box-icon class="size-5" type="solid" name="message-square-dots"
                                            color="white"></box-icon>
                                        <p class="ml-1 mt-0.5">{{ item.comments }}</p>
                                    </div>
                                    <div class="flex items-center">
                                        <box-icon class="size-5" type="solid" name="down-arrow-square"
                                            color="white"></box-icon>
                                        <p class="ml-1 mt-0.5">{{ item.downloads }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </swiper-slide>
                </swiper>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Grid, Pagination } from 'swiper/modules';

import 'swiper/swiper-bundle.css';
import 'swiper/css/grid';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import 'swiper/css/scrollbar';

const categories = ref([
  { name: "ENGINEERING", icon: "engineering", color: "#20948B" },
  { name: "LaWS", icon: "gavel", color: "#F52549" },
  { name: "MEDIC", icon: "medical_services", color: "#735DA5" },
  { name: "architecture", icon: "architecture", color: "#89ABE3" },
  { name: "unicore", icon: "auto_stories", color: "#DC6B19" },
  { name: "ict", icon: "code", color: "#1995AD" },
  { name: "business", icon: "handshake", color: "#F98866" },
  { name: "pharmacy", icon: "pill", color: "#7A2048" },
  { name: "education", icon: "school", color: "#008DDA" },
  { name: "languages", icon: "language", color: "#EA738D" },
  { name: "Alied HS", icon: "admin_meds", color: "#375E97" },
  { name: "science", icon: "science", color: "#E1B33D" },
  { name: "accounting", icon: "calculate", color: "#0E46A3" },
  { name: "dentistry", icon: "dentistry", color: "#D16D6A" },
  { name: "others", icon: "more_horiz", color: "#264E5B" },
]);

const suggestion = ref([
  {
    title: "Thermodynamics Notes for Engineering",
    category: "ENGINEERING",
    pages: 10,
    date: "14/10/2024",
    publisher: "apihzz",
    likes: 63,
    comments: 124,
    downloads: 432,
  },
  {
    title: "Physics Notes for Engineering",
    category: "ENGINEERING",
    pages: 15,
    date: "15/10/2024",
    publisher: "science_guru",
    likes: 45,
    comments: 98,
    downloads: 320,
  },
  {
    title: "Mathematics Notes for Engineering",
    category: "ENGINEERING",
    pages: 20,
    date: "16/10/2024",
    publisher: "math_whiz",
    likes: 80,
    comments: 210,
    downloads: 590,
  },
  {
    title: "Thermodynamics Notes for Engineering",
    category: "ENGINEERING",
    pages: 10,
    date: "14/10/2024",
    publisher: "apihzz",
    likes: 63,
    comments: 124,
    downloads: 432,
  },
  {
    title: "Physics Notes for Engineering",
    category: "ENGINEERING",
    pages: 15,
    date: "15/10/2024",
    publisher: "science_guru",
    likes: 45,
    comments: 98,
    downloads: 320,
  },
  {
    title: "Mathematics Notes for Engineering",
    category: "ENGINEERING",
    pages: 20,
    date: "16/10/2024",
    publisher: "math_whiz",
    likes: 80,
    comments: 210,
    downloads: 590,
  },
  {
    title: "Thermodynamics Notes for Engineering",
    category: "ENGINEERING",
    pages: 10,
    date: "14/10/2024",
    publisher: "apihzz",
    likes: 63,
    comments: 124,
    downloads: 432,
  },
  {
    title: "Physics Notes for Engineering",
    category: "ENGINEERING",
    pages: 15,
    date: "15/10/2024",
    publisher: "science_guru",
    likes: 45,
    comments: 98,
    downloads: 320,
  },
  {
    title: "Mathematics Notes for Engineering",
    category: "ENGINEERING",
    pages: 20,
    date: "16/10/2024",
    publisher: "ath_whiz",
    likes: 80,
    comments: 210,
    downloads: 590,
  },
]);

// Row and Slide counts
const rowx = ref(window.innerWidth >= 2000 ? 3 : 2);
const slidex = ref(3);

const updateRows = () => {
  const width = window.innerWidth;

  if (width >= 2560) {
    rowx.value = 3;
    slidex.value = 4;
  } else if (width >= 1920) {
    rowx.value = 3;
    slidex.value = 4;
  } else if (width >= 1440) {
    rowx.value = 2;
    slidex.value = 3;
  } else if (width >= 1280) {
    rowx.value = 2;
    slidex.value = 3;
  } else if (width >= 1024) {
    rowx.value = 2;
    slidex.value = 3;
  } else if (width >= 768) {
    rowx.value = 1;
    slidex.value = 2;
  } else if (width >= 480) {
    rowx.value = 1;
    slidex.value = 1;
  } else {
    rowx.value = 1;
    slidex.value = 1;
  }
};

// Hook into the lifecycle
onMounted(() => {
  window.addEventListener("resize", updateRows);
  updateRows(); // Call initially to set the right number of rows/slides based on current width
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", updateRows);
});
</script>

<style scoped>
.category-item {
    transition: background-color 0.3s ease;
}

.category-item:hover {
    filter: brightness(1.2);
}

.text-med {
    font-size: 1.1rem;
}

.sliderWrapper {
    padding-bottom: 30px;
    /* Create space for the bullets within the swiper container */

    :global(.swiper-pagination-bullets) {
        position: relative;
        display: flex;
        justify-content: center;
        bottom: -0px;
        width: 100%;
    }

    :global(.swiper-pagination-bullet) {
        background-color: #4e4d4d;
        margin: 0 5px;
        /* Space between bullets */
        opacity: 1;
        border-radius: 0.5rem;
    }

    :global(.swiper-pagination-bullet-active) {
        background-color: #1c5aa7;
    }
}
</style>
