<template>
    <div class="flex flex-col h-full w-full bg-zinc-900 ">
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
        <div class="flex flex-1 py-12 justify-center items-center">
            <form @submit.prevent="submitForm"
                class="bg-zinc-800 p-10  rounded-lg text-center space-y-3 font-norwester">
                <div class="text-3xl -mt-5 font-bold text-white">
                    CREATE YOUR <span class="text-sky-500"> ACCOUNT</span>
                </div>
                <div class="text-md text-white">
                    Create an account and start <span class="text-sky-500">exchanging notes!</span>
                </div>

                <!-- Email -->
                <div class=" text-left text-white space-y-1 pt-3">
                    <div>
                        <label>Email:</label>
                    </div>
                    <div>
                        <input v-model="form.email" placeholder="Eg:user123@gmail.com" type="email" class="peer w-96 h-10 rounded-lg border-2 border-zinc-700 bg-zinc-700 pl-3
                             placeholder:text-stone-500 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
                            disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                            invalid:border-pink-500 invalid:text-pink-600
                            focus:invalid:border-pink-500 focus:invalid:ring-pink-500">
                        <p class="invisible peer-invalid:visible text-pink-600 text-xs text-end mt-1 -mb-5">
                            Please provide a valid email address.
                        </p>
                        <p v-if="errors.email" class="text-rose-600 text-xs mt-1 -mb-3">{{ errors.email }}</p>
                    </div>
                </div>
                <!-- Username -->
                <div class=" text-left text-white space-y-1 ">
                    <div>
                        <label>Username:</label>
                    </div>
                    <div>
                        <input v-model="form.username" type="text" class="w-96 h-10 rounded-lg border-2 border-zinc-700 bg-zinc-700 pl-3
                            focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 ">
                        <p v-if="errors.username" class="text-rose-600 text-xs mt-1 -mb-3">{{ errors.username }}</p>

                    </div>
                </div>
                <!-- Password -->
                <div class="text-left text-white space-y-1">
                    <div>
                        <label>Password:</label>
                    </div>
                    <div>
                        <input v-model="form.password1" type="password" class="w-full h-10 rounded-lg border-2 pl-3 border-zinc-700 bg-zinc-700
                            focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 " 
                            :class="{'focus:border-pink-500 focus:ring-pink-500': errors.password1}">

                        <p v-if="errors.password1" class="text-rose-600 text-xs mt-1 -mb-3">{{ errors.password1 }}</p>

                    </div>
                </div>
                <!-- Confirm Password -->
                <div class="text-left text-white space-y-1">
                    <div>
                        <label>Confirm Password:</label>
                    </div>
                    <div>
                        <input v-model="form.password2" type="password" class="w-full h-10 rounded-lg border-2 pl-3 border-zinc-700 bg-zinc-700
                            focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 "
                            :class="{'focus:border-pink-500 focus:ring-pink-500': errors.password2}">
                        <p v-if="errors.password2" class="text-rose-600 text-xs mt-1 -mb-3">{{ errors.password2 }}</p>

                    </div>
                </div>
                <!-- Create account button -->
                <div class="pt-8">
                    <button class="w-full h-10 bg-blue-600 rounded-lg text-white font-bold hover:bg-blue-700
                               focus:none  focus:ring   focus:ring-white">
                        CREATE ACCOUNT
                    </button>
                </div>

                <!-- Sign up option -->
                <div class="text-white text-sm ">
                    Already have an account? <RouterLink :to="'/login'" class="text-sky-500 cursor-pointer">LOG IN HERE
                    </RouterLink>
                </div>

                <!-- Sign up option -->
                <div class="text-white text-sm">
                    By creating account, your agree to our <a class="text-sky-500 cursor-pointer">terms of
                        service</a><br>
                    and <a class="text-sky-500 cursor-pointer">privacy policy</a>
                </div>

            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import { useToastStore } from './toast.js';

const toastStore = useToastStore();

const error = ref([]);  // Initialize as an empty array

const form = ref({
    email: '',
    username: '',
    password1: '',
    password2: ''
});

const errors = ref({
    email: '',
    username: '',
    password1: '',
    password2: ''
});

const submitted = ref(false); // Flag to track if the form was successfully submitted
let trigger = false;

// Watch for changes in password fields, but only validate if form hasn't been submitted
watch([() => form.value.password1, () => form.value.password2], ([password1, password2]) => {
    if (!submitted.value) {
        validatePassword(password1, password2);
    }
});

const validatePassword = (password1, password2) => {
    // Reset password errors
    errors.value.password1 = '';
    errors.value.password2 = '';

    if (!password1) {
        errors.value.password1 = 'Password is required';
    }

    // Check if password2 (confirmation) is empty
    if (!password2) {
        errors.value.password2 = 'Please confirm your password';
    }

    // Check if password meets criteria
    if (password1 && password1.length < 8) { // Fix length validation
        errors.value.password1 = 'Password must be at least 8 characters long.';
        trigger = true;
    }

    // Check if passwords match
    if (password1 !== password2) {
        errors.value.password2 = 'Passwords do not match.';
        trigger = true;
    }
};

const submitForm = async () => {
    form.value.email = form.value.email.trim().toLowerCase();

    // Clear any previous error messages
    errors.value = {
        email: '',
        username: '',
        password1: '',
        password2: ''
    };

    let hasError = false;

    if (!form.value.email) {
        errors.value.email = 'Email is required';
        hasError = true;
    }

    if (!form.value.username) {
        errors.value.username = 'Username is required';
        hasError = true;
    }

    if (!form.value.password1) {
        errors.value.password1 = 'Password is required';
        hasError = true;
    }

    validatePassword(form.value.password1, form.value.password2);
    if (errors.value.password1 || errors.value.password2) {
        hasError = true;
    }

    if (!hasError) {
        try {
            const response = await axios.post('/api/signup/', form.value);
            if (response.status === 200) {
                toastStore.showToast(5000, 'Account created successfully. Please login.', 'bg-emerald-500');

                submitted.value = true;

                form.value.email = '';
                form.value.username = '';
                form.value.password1 = '';
                form.value.password2 = '';

                setTimeout(() => {
                    errors.value = {
                        email: '',
                        username: '',
                        password1: '',
                        password2: ''
                    };
                    submitted.value = false; 
                }, 100); 

            } else {
                toastStore.showToast(5000, 'Account creation failed. Please try again.', 'bg-rose-500');
            }
        } catch (err) {
            if (err.response && err.response.data && err.response.data.errors) {
                const serverErrors = err.response.data.errors;
                // Handle specific errors (e.g., username taken)
                for (const [key, value] of Object.entries(serverErrors)) {
                    errors.value[key] = value.join(', ');
                }
            } else {
                toastStore.showToast(5000, 'An unexpected error occurred. Please try again.', 'bg-rose-500');
            }
        }
    }
};
</script>
