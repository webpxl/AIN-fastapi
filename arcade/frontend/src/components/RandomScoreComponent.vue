<template>
    <section>
        <h2>ADD RANDOM SCORE</h2>
        <p>{{ player }} {{ randomScore }}</p>
        <div class="btn" @click="sendRandomScore(randomScore, player)">SEND SCORE</div>
    </section>
</template>

<script setup>
    import { ref } from 'vue';

    let randomScore = ref(0);
    let player = ref('___');
    setInterval(() => {
        randomScore.value = 10*(Math.floor(Math.random() * 100));
        // Fill player with a random sequence of 3 capital letters
        player.value = fixLetter() + fixLetter() + fixLetter();
    }, 100); // generate random score every x milliseconds

    const sendRandomScore = (score, name) => {
        fetch('http://localhost:8000/scores', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                player: name,
                score: score
            })
        }).then(() => {
            console.log('Score sent');
        });
    }

    const fixLetter = () => {
        return String.fromCharCode(65 + Math.floor(Math.random() * 26));
    }

</script>

<style scoped>
    section {
        width: 50%;
        padding: 48px;
        border: 1px solid #FFF;
        float: right;
    }

    h2 {
        color: #FFF;
        font-size: 2.6em;
        margin-bottom: 12px;
    }

    p {
        font-size: 2.4em;
        color: orange;
        padding-right: 48px;
        margin: 60px 0;
        text-align: center;
    }

    div.btn {
        background-color: #FFF;
        color: #000;
        padding: 12px;
        margin-top: 12px;
        cursor: pointer;
        text-align: center;
    }

    div.btn:hover {
        background-color: #DDD;
    }
</style>