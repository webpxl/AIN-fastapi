<template>
    <section>
        <h2>The Secret</h2>
        <button @click="fetchSecret()">Reveal Secret</button>
        <p v-html="secret"></p>
    </section>
</template>

<script setup>
    import { onMounted, ref } from 'vue';
    import axios from 'axios';
    import { useAuthStore } from '@/stores/auth';
    
    const secret = ref('');
    const authStore = useAuthStore();

    const fetchSecret = async () => {
        const config = {
            headers: { Authorization: `Bearer ${authStore.token}` }
        };
        
        axios.get('http://localhost:8000/secret', config).then((response) => {
            console.log("GOT RESPONSE", response);
            if(response.status == 200) {
                secret.value = response.data.secret;
            }           
        }).catch((error) => {
            console.log("ERROR",error);
            if(error.status == 401) {
                secret.value = "[Not authorized]<br />You have no power here!";
            } else {
                secret.value = "Something went wrong";
            } 
        });
    };
    
</script>

<style scoped>
    section {
        width: 400px;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 5px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        float: left;
        margin-left: 32px;
        background-color: white;
    }

    h2 {
        color: black;
        font-size: 1.4em;
        margin-bottom: 12px;
    }

    p {
        margin-top: 32px;
    }

</style>