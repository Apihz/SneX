<template>
    <div class="flex flex-col h-full w-full bg-zinc-900">
        <!-- Navbar -->
        <div class="Navbar bg-black w-full xl:h-16 border-b-4 border-white flex items-center justify-between">
            <div class="w-60"></div>
            <div class="flex items-center space-x-5">
                <div class="border rounded-md">
                    <img class="w-12 h-10 border rounded-md" src="/SneX.jpg" alt="">
                </div>
                <div class="xl:text-4xl">
                    STUDENT NOTES <span class="text-red-600">EXCHANGE</span>
                </div>
            </div>
            <div class="flex text-2xl mr-10 space-x-5">
                <div>About us ▼</div>
                <div>Contact us ▼</div>
            </div>
        </div>

        <!-- Centered Login Form -->
        <div class="flex flex-1 justify-center items-center">
            <form v-on:submit.prevent="submitForm"
                class="bg-zinc-800 py-8 px-7  rounded-lg text-center space-y-3 font-norwester">
                <div class="text-3xl font-bold text-white ">
                    WELCOME <span class="text-green-500"> BACK!</span>
                </div>
                <div class="text-lg text-white">
                    LOG IN INTO YOUR ACCOUNT
                </div>

                <!-- Email -->
                <div class=" text-left text-white space-y-1 pt-10">
                    <div>
                        <label>Email:</label>
                    </div>
                    <div>
                        <input v-model="form.email" placeholder="Eg:user123@gmail.com" type="email" class="w-96 h-10 rounded-lg border-2 border-zinc-700 bg-zinc-700 pl-3
                             placeholder:text-stone-500 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
                            disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                           ">
                        <p v-if="errors.email" class="text-rose-600 text-xs mt-1 -mb-3">{{ errors.email }}</p>
                    </div>
                </div>
                <!-- Password -->
                <div class="text-left text-white space-y-1">
                    <div>
                        <label>Password:</label>
                    </div>
                    <div>
                        <input v-model="form.password" type="password" class="w-full h-10 rounded-lg border-2 pl-3 border-zinc-700 bg-zinc-700
                            focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 ">
                        <p v-if="errors.password" class="text-rose-600 text-xs mt-1 -mb-3">{{ errors.password }}</p>

                    </div>
                </div>
                <!-- Trouble logging in -->
                <div class="text-blue-500 text-sm text-left pt-2 cursor-pointer">
                    Forgot password?
                </div>


                <!-- Log in button -->
                <div class="pt-4">
                    <button class="w-full h-10 bg-blue-600 rounded-lg text-white font-bold hover:bg-blue-700
                               focus:none  focus:ring   focus:ring-white">
                        LOG IN
                    </button>
                </div>
                <!-- Sign in options -->
                <div class="text-white">or sign in with</div>
                <div class="flex space-x-1.5 justify-center items-center w-full">
                    <div
                        class="text-white bg-zinc-700 rounded-lg h-10 flex justify-center items-center grow basis-0 hover:bg-zinc-600">
                        <button class="">Google</button>
                    </div>
                    <div
                        class="text-white bg-zinc-700 rounded-lg h-10 flex justify-center items-center grow basis-0 hover:bg-zinc-600">
                        <button class="">Facebook</button>
                    </div>
                    <div
                        class="text-white bg-zinc-700 rounded-lg h-10 flex justify-center items-center grow basis-0 hover:bg-zinc-600">
                        <button class="">Apple</button>
                    </div>
                </div>


                <!-- Sign up option -->
                <div class="text-white pt-4">
                    Don't have an account?
                    <RouterLink :to="'/signup'" class="text-sky-500 cursor-pointer">
                        Sign up here
                    </RouterLink>
                </div>



            </form>
        </div>
    </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router';
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from './user.js';

const userStore = useUserStore();
const router = useRouter();

const form = ref({
    email: '',
    password: '',
});

const errors = ref({
    email: '',
    password: ''
});
const submitForm = async () => {
    form.value.email = form.value.email.trim().toLowerCase();
    errors.value = {
        email: '',
        password: ''
    };
    let hasError = false;

    if (!form.value.email) {
        errors.value.email = 'Email is required';
        hasError = true;
    }

    if (!form.value.password) {
        errors.value.password = 'Password is required';
        hasError = true;
    }

    if (!hasError) {
        try {
            const response = await axios.post('/api/login/', form.value);

            // Set token and headers
            userStore.setToken(response.data);
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;

            // Fetch user info and redirect
            const userInfoResponse = await axios.get('/api/me');
            userStore.setUserInfo(userInfoResponse.data);

            router.push('/');  // Redirect to home on success

        } catch (error) {
            if (error.response && error.response.status === 404) {
                errors.value.email = 'Account with this email does not exist.';
            } else if (error.response && error.response.status === 401) {
                errors.value.password = 'Incorrect password.';
            } else {
                errors.value = ['An unexpected error occurred.'];
            }
        }
    }
};


</script>
