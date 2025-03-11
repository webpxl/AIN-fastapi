<template>
    <section>
      <form @submit.prevent="fetchToken()" class="login-form" v-if="!authStore.token">
        <label for="email">Username:</label>
        <input v-model="username" type="text" required />
        
        <label for="password">Password:</label>
        <input v-model="password" type="password" required />
        
        <button type="submit">Login</button>        
      </form>

      <p class='error' v-if="!authStore.token && message">{{ message }}</p>
      <p v-if="authStore.token != ''">Got token: '{{ authStore.token }}'</p>
    </section>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import axios from 'axios';
    import { useAuthStore } from '@/stores/auth';
    
    const username = ref('');
    const password = ref('');
    const message = ref('');
    const authStore = useAuthStore();

    const fetchToken = async () => {
        const params = new URLSearchParams();
        // header type: application/x-www-form-urlencoded
        params.append('username', username.value);
        params.append('password', password.value);
        axios.post('http://localhost:8000/token', params).then((response) => {
            console.log("GOT RESPONSE", response);
            if(response.status == 200) {
                setToken(response.data.access_token);
            }           
        }).catch((error) => {
            console.log("ERROR",error);       
            message.value = error.response.data.detail;     
            setToken('');

        });
    };

    const setToken = (tokenString) => {
        authStore.token = tokenString;
    }
  </script>
  
  <style scoped>
  section {
    width: 500px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    float: left;
    background-color: white;
  }
  .login-form {
    display: flex;
    flex-direction: column;
  }
  label {
    margin-top: 10px;
  }
  input {
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  button {
    margin-top: 15px;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }

  p.error {
    color: red;
    margin-top: 10px;
  }
  </style>
  