<template>
    <section>
        <h2>HIGHSCORE</h2>
        <table>
            <tr v-for="(highscore, index) in highscores" :key="index">
                <td>{{  index+1 }}.</td><td>{{ highscore.player }}</td><td>{{ highscore.score }}</td>
            </tr>
        </table>
    </section>
</template>

<script setup>
    import { onMounted, ref } from 'vue';
    import axios from 'axios';
    
    let highscores = ref([]);
    onMounted(() => {

        setInterval(() => {
            loadHighscores();
        }, 500); // refresh highscores every x milliseconds    
        loadHighscores();
    });

    const loadHighscores = async () => {
        const response = await axios.get('http://localhost:8000/highscores');
        highscores.value = response.data;

        /*
        axios.get('http://localhost:8000/highscores').then(data => {
            highscores.value = data.data;
        }) // get highscores from FastAPI backend
        */
    }
</script>

<style scoped>
    section {
        width: 40%;
        padding: 48px;
        border: 1px solid #FFF;
        float: left;
    }

    h2 {
        color: #FFF;
        font-size: 2.6em;
        margin-bottom: 12px;
    }
    
    table {
        margin-top: 60px;
        margin-left: 60px;
    }

    td {
        font-size: 1.8em;
        color: #DDD;
        padding-right: 48px;
    }
    
</style>