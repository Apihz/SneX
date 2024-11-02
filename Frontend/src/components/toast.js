import { defineStore } from 'pinia'

export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false,
    }),

    actions: {
        showToast(ms, message, classes) {
            this.ms = parseInt(ms);
            this.message = message;
            this.classes = classes;
            this.isVisible = true;
            console.log('Toast Triggered:', { ms, message, classes });
        
            setTimeout(() => {
                this.classes += ' -translate-y-28','-translate-x-30';
            }, 100000);
        
            setTimeout(() => {
                this.classes = this.classes.replace('-translate-y-28', '');
            }, 500);
        
            setTimeout(() => {
                this.isVisible = false;
            }, ms);
        },
        

        hideToast(){
            this.isVisible = false
        }
    }
})