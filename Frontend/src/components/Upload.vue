<template>
    <div class="w-full h-full ">
        <h1 class="mt-2 ml-2 flex justify-center xl:text-4xl ">UPLOAD AND PUBLISH YOUR DOCUMENT HERE</h1>
        <div class="h-5/6 w-full">
            <div class="bg-zinc-800 flex mx-40 h-full rounded-2xl mt-5  ">
                <div class="w-1/2 ">
                    <div class="flex justify-center  ">
                        <h1 class="text-center bg-zinc-700 rounded-md text-sky-500 px-4 text-3xl mt-5 -mb-6">upload</h1>
                    </div>
                    <div class=" h-3/4 m-8 bg-zinc-700 border-white border-4 border-dashed   rounded-xl">
                        <div class="flex-rows justify-center items-center content-center h-full">
                            <h1 class="text-center text-2xl">Drag files here!</h1>
                            <div class="card flex flex-col gap-6 items-center justify-center">

                            </div>
                        </div>
                    </div>
                    <div class="flex justify-center">
                        <div class="-mt-3">
                            <button class="bg-rose-700 hover:bg-rose-700/90  flex justify-center items-center space-x-3 h-10 w-40 rounded-lg">
                                <span class="material-symbols-outlined ">block</span>
                                <h1 class="text-2xl">remove</h1>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="w-1/2 ">
                    <div class="flex justify-center ">
                        <h1 class="text-center text-3xl mt-5 -mb-6">preview</h1>
                    </div>
                    <div class=" h-3/4 m-8 bg-zinc-700 rounded-xl">
                    </div>
                    <div class="flex justify-center">
                        <div class=" -mt-3">
                            <button class="bg-emerald-600 hover:bg-emerald-600/90 flex justify-center items-center space-x-3 h-10 w-40 rounded-lg">
                                <span class="material-symbols-outlined ">check_circle</span>
                                <h1 class="text-2xl">confirm</h1>
                            </button>
                        </div>
                    </div>

                </div>
            </div>

        </div>
        <div class="h-1/5"></div>
    </div>
</template>

<script setup>

</script>

<style></style>