import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            username: null,  
            email: null,
            access: null,
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access');
                this.user.refresh = localStorage.getItem('user.refresh');
                this.user.id = localStorage.getItem('user.id');
                this.user.username = localStorage.getItem('user.username');  // Consistency here
                this.user.email = localStorage.getItem('user.email');
                this.user.isAuthenticated = true;

                this.refreshToken();
                console.log('Initiated user:', this.user);
            }
        },

        setToken(data) {
            console.log('SetToken:', data);

            this.user.access = data.access;
            this.user.refresh = data.refresh;
            this.user.isAuthenticated = true;

            localStorage.setItem('user.access', data.access);
            localStorage.setItem('user.refresh', data.refresh);
        },

        removeToken() {
            console.log('RemoveToken');

            this.user.refresh = null;
            this.user.access = null;
            this.user.isAuthenticated = false;
            this.user.id = null;
            this.user.username = null;  // Ensure this is consistently used
            this.user.email = null;

            localStorage.removeItem('user.access');
            localStorage.removeItem('user.refresh');
            localStorage.removeItem('user.id');
            localStorage.removeItem('user.username');  // Consistency here
            localStorage.removeItem('user.email');
        },

        setUserInfo(user) {  // Ensure 'user' is passed as a parameter
            console.log('SetUserInfo', user);

            this.user.id = user.id;
            this.user.username = user.username;  // Consistency here
            this.user.email = user.email;

            localStorage.setItem('user.id', user.id);
            localStorage.setItem('user.username', user.username);  // Consistency here
            localStorage.setItem('user.email', user.email);

            console.log('User', this.user);
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
            .then(response => {
                this.user.access = response.data.access;
                localStorage.setItem('user.access', response.data.access);
                axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
            })
            .catch(error => {
                console.log('Error refreshing token', error);
                this.removeToken();
            });
        }
    }
});
