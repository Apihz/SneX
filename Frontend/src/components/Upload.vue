<template>
    <div class="w-full h-full">
        <h1 class="mt-2 ml-2 flex justify-center xl:text-4xl">UPLOAD AND PUBLISH YOUR DOCUMENT HERE</h1>
        <div class="h-5/6 w-full">
            <div class="bg-zinc-800 flex mx-40 h-full rounded-2xl mt-5">
                <div class="w-1/2">
                    <div class="flex justify-center">
                        <h1 class="text-center bg-zinc-700 rounded-md text-sky-500 px-4 text-3xl mt-5 -mb-6">upload</h1>
                    </div>
                    <div 
                        class="h-3/4 m-8 bg-zinc-700 border-white border-4 border-dashed rounded-xl"
                        @drop.prevent="handleDrop"
                        @dragover.prevent
                        @dragenter.prevent
                    >
                        <div class="flex-rows justify-center items-center content-center h-full">
                            <h1 class="text-center text-2xl">{{ dragMessage }}</h1>
                            <div class="card flex flex-col gap-6 items-center justify-center">
                                <input 
                                    type="file" 
                                    ref="fileInput" 
                                    @change="handleFileSelect" 
                                    class="hidden" 
                                    accept=".pdf,.doc,.docx,.txt"
                                />
                                <button 
                                    v-if="!selectedFile" 
                                    @click="$refs.fileInput.click()"
                                    class="bg-sky-500 hover:bg-sky-600 px-4 py-2 rounded-lg mt-4"
                                >
                                    Select File
                                </button>
                                <div v-if="selectedFile" class="text-center mt-4">
                                    <p>{{ selectedFile.name }}</p>
                                    <p class="text-sm text-gray-400">{{ formatFileSize(selectedFile.size) }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-center">
                        <div class="-mt-3">
                            <button 
                                @click="removeFile"
                                class="bg-rose-700 hover:bg-rose-700/90 flex justify-center items-center space-x-3 h-10 w-40 rounded-lg"
                                :disabled="!selectedFile"
                            >
                                <span class="material-symbols-outlined">block</span>
                                <h1 class="text-2xl">remove</h1>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="w-1/2">
                    <div class="flex justify-center">
                        <h1 class="text-center text-3xl mt-5 -mb-6">preview</h1>
                    </div>
                    <div class="h-3/4 m-8 bg-zinc-700 rounded-xl p-4">
                        <!-- Preview content -->
                        <div v-if="previewUrl" class="h-full">
                            <iframe 
                                v-if="isPreviewable" 
                                :src="previewUrl" 
                                class="w-full h-full"
                            ></iframe>
                            <div v-else class="flex items-center justify-center h-full">
                                <p>Preview not available for this file type</p>
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-center">
                        <div class="-mt-3">
                            <button 
                                @click="uploadFile"
                                class="bg-emerald-600 hover:bg-emerald-600/90 flex justify-center items-center space-x-3 h-10 w-40 rounded-lg"
                                :disabled="!selectedFile"
                            >
                                <span class="material-symbols-outlined">check_circle</span>
                                <h1 class="text-2xl">confirm</h1>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const fileInput = ref(null)
const selectedFile = ref(null)
const previewUrl = ref(null)
const dragMessage = ref('Drag files here!')

const isPreviewable = computed(() => {
    if (!selectedFile.value) return false
    const type = selectedFile.value.type
    return type.startsWith('image/') || type === 'application/pdf' || type === 'text/plain'
})

const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes'
    const k = 1024
    const sizes = ['Bytes', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
}

const handleFileSelect = (event) => {
    const file = event.target.files[0]
    if (file) {
        handleFile(file)
    }
}

const handleDrop = (event) => {
    const file = event.dataTransfer.files[0]
    if (file) {
        handleFile(file)
    }
}

const handleFile = (file) => {
    selectedFile.value = file
    if (file.type.startsWith('image/') || file.type === 'application/pdf') {
        previewUrl.value = URL.createObjectURL(file)
    } else if (file.type === 'text/plain') {
        const reader = new FileReader()
        reader.onload = (e) => {
            previewUrl.value = e.target.result
        }
        reader.readAsText(file)
    }
}

const removeFile = () => {
    selectedFile.value = null
    previewUrl.value && URL.revokeObjectURL(previewUrl.value)
    previewUrl.value = null
    if (fileInput.value) {
        fileInput.value.value = ''
    }
}

const uploadFile = async () => {
    if (!selectedFile.value) return

    const formData = new FormData()
    formData.append('file', selectedFile.value)

    try {
        const response = await fetch('http://127.0.0.1:8000/api/files/upload/', {
            method: 'POST',
            body: formData
        })

        if (response.ok) {
            alert('File uploaded successfully!')
            removeFile()
        } else {
            throw new Error('Upload failed')
        }
    } catch (error) {
        console.error('Error uploading file:', error)
        alert('Failed to upload file. Please try again.')
    }
}
</script>