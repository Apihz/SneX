import { defineStore } from 'pinia';
import axios from 'axios';  

export const useDocumentStore = defineStore({
    id: 'document',

    state: () => ({
        documents: {
            id: null,
            name: null,
            file: null,
            category: null, 
            description: null,
            image: null,
            number_of_pages: null,

            uploaded_at: null,
            uploaded_by: null,
        },
    })

    

});