<template>
    <div class="w-full h-full ">
        <div class=" flex items-center ml-4 w-full xl:h-20 xl:text-4xl ">
            <h1>{{ title }} p</h1>
        </div>
        <div class=" xl:w-full xl:h-full p-4 ">
            <div class=" w-full h-full flex ">
                <div class="">
                    <div
                        class="flex justify-center items-center -mt-2 bg-emerald-600 rounded-xl shadow-xl shadow-black xl:w-64 xl:h-12">
                        <h1 class="xl:text-3xl">info</h1>
                    </div>
                    <div class="bg-zinc-800 min-h-screen h-fit pb-5 mt-3 rounded-xl xl:w-64  ">
                        <div class="ml-4">
                            <h1 class="text-start pt-3 xl:text-2xl">Document information :</h1>
                            <div class="ml-5 mt-1 space-y-1">
                                <div class="flex">
                                    <span class="material-symbols-outlined mr-3 ">folder</span>
                                    <p>Course : {{ course }}</p>
                                </div>
                                <div class="flex">
                                    <span class="material-symbols-outlined mr-3 ">auto_stories</span>
                                    <p>Number of pages : {{ numberOfPages }}</p>
                                </div>
                                <div class="flex">
                                    <span class="material-symbols-outlined mr-3 ">calendar_month</span>
                                    <p>Date published : {{ date }}</p>
                                </div>
                                <div class="flex">
                                    <span class="material-symbols-outlined mr-3 ">account_circle</span>
                                    <p>publisher : {{ publisher }}</p>
                                </div>
                            </div>
                        </div>
                        <div class=" ml-4 pr-3">
                            <h1 class="text-start pt-3 xl:text-2xl">details :</h1>
                            <p class="mt-1 ml-4 text-wrap">Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                                Perspiciatis voluptas optio rem aperiam sit quod tempora, iste quis vitae consectetur.
                                Placeat pariatur ipsa at sunt hic mollitia, cupiditate cumque deserunt. Lorem ipsum
                                dolor sit amet, consectetur adipisicing elit. Ducimus aut labore sit! Quis amet
                                veritatis temporibus deleniti officia sapiente et ullam culpa dolorum. Enim distinctio
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi, fuga accusamus. Ipsa
                                vitae eos dolores omnis? Temporibus sunt id ullam aliquam animi! Ratione ut commodi a
                                architecto quasi labore doloremque. praesentium ex voluptatum ut iusto. Lorem ipsum
                                dolor, sit amet consectetur adipisicing
                                elit. Ab obcaecati soluta quo eos minima libero eum commodi, aut, aperiam reiciendis
                                eius distinctio blanditiis eligendi in quos officiis porro magni vero?</p>
                        </div>
                    </div>
                </div>
                <div class="w-fit h-full ml-5 flex-rows grow   ">
                    <div class="">
                        <div class="flex justify-between items-center -mt-2 ">
                            <div class="flex items-center space-x-3">
                                <button class="bg-emerald-600 rounded-xl xl:text-2xl xl:w-52 xl:h-12">
                                    download by
                                </button>
                                <p class="xl:text-3xl">or</p>
                                <button class="bg-amber-500 rounded-xl xl:text-2xl xl:w-52 xl:h-12">
                                    snex points
                                </button>
                            </div>
                            <div class="space-x-1">
                                <button class="size-12 bg-rose-600 rounded-lg">
                                    <span class="material-symbols-outlined  ">favorite</span>
                                </button>
                                <button class="size-12 bg-sky-600 rounded-lg">
                                    <span class="material-symbols-outlined  ">chat</span>
                                </button>
                                <button class="size-12 bg-teal-600 rounded-lg">
                                    <span class="material-symbols-outlined  ">bookmark</span>
                                </button>
                                <button class="size-12 bg-indigo-500 rounded-lg">
                                    <span class="material-symbols-outlined  ">share</span>
                                </button>
                            </div>
                        </div>

                    </div>
                    <div>
                        <button class="flex justify-center items-center w-full h-12 bg-emerald-500 rounded-xl mt-3">
                            <span class="material-symbols-outlined  ">swap_horiz</span>
                            <p class="xl:text-2xl ml-3">uploading a file to unlock downloads</p>
                        </button>
                    </div>
                    <div class="w-full h-full mt-3">
                        <div class="rounded-xl">
                            <img class=" rounded-xl w-full h-full" src="/SneX.jpg" alt="">
                        </div>
                    </div>

                </div>
                <div class="w-68 ml-4 h-full   bg-zinc-800 rounded-xl p-3 -mt-2 shadow-lg shadow-zinc-700">
                    <p class="text-lg text-center">recommended for you</p>
                    <div>
                        <div v-for="item in recommendations" :key="item.title" class="py-2">
                            <div
                                class=" bg-zinc-700/50 rounded-xl flex-rows h-52 justify-center items-center  shadow-lg shadow-zinc-900">
                                <img class="w-full h-20 rounded-xl rounded-b-none " src="/SneX.jpg" alt="">
                                <div class="p-2">
                                    <h1 class="text-sky-600 max-h-12 text-lg ">{{ item.title }}</h1>
                                    <div class="flex mt-2 ">
                                        <span class="material-symbols-outlined mr-1"
                                            style="font-size: 18px;">folder</span>
                                        <p class="text-sm">Course : {{ item.course }}</p>
                                    </div>
                                    <div class="flex ">
                                        <span class="material-symbols-outlined mr-1"
                                            style="font-size: 18px;">favorite</span>
                                        <p class="text-sm">Likes : {{ item.likes }}</p>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const title = ref("Continuous charge distribution and gauss's law");
const course = ref("Physics");
const numberOfPages = ref(10);
const date = ref("2021-10-10");
const publisher = ref("John Doe");
const recommendations = ref([
    {
        title: "Continuous charge distribution and gauss's law",
        course: "Physics",
        likes: 10,
        publisher: "John Doe"
    },
    {
        title: "Continuous charge distribution and gauss's law",
        course: "Physics",
        likes: 10,
        publisher: "John Doe"
    },
    {
        title: "Continuous charge distribution and gauss's law",
        course: "Physics",
        likes: 10,
        publisher: "John Doe"
    },
    {
        title: "Continuous charge distribution and gauss's law",
        course: "Physics",
        likes: 10,
        publisher: "John Doe"
    },
    {
        title: "Continuous charge distribution and gauss's law",
        course: "Physics",
        likes: 10,
        publisher: "John Doe"
    },
    {
        title: "Continuous charge distribution and gauss's law",
        course: "Physics",
        likes: 10,
        publisher: "John Doe"
    },

]);



</script>

<style scoped>
.w-68 {
    width: 17rem;
}
</style>