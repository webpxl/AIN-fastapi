<template>
    <section>
        <h2>DELETE SCORE</h2>
        <div class="inputbox">
            <input type="text" size="3" v-model="player" placeholder="___" />
        </div>
        <div class="btn" @click="deletePlayer(player)">DELETE SCORE</div>
    </section>
</template>

<script setup>
    import { ref } from 'vue';

    let player = ref('');

    const deletePlayer = (name) => {
        fetch(`http://localhost:8000/scores/${name}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            console.log('Score delete: ', response);
            player.value = '';
        });
    }

</script>

<style scoped>
    section {
        width: 50%;
        padding: 48px;
        border: 1px solid #FFF;
        float: right;
        margin-top: 48px;

        clear:both;
    }

    h2 {
        color: #FFF;
        font-size: 2.6em;
        margin-bottom: 12px;
    }

    div.inputbox {
        text-align: center;
    }

    input {
        font-size: 2.4em;
        color: white;
        padding-right: 48px;
        margin: 60px 0;
        text-align: center;
        background-color: transparent;
        padding: 8px;
        border: 2px solid #FFF;
        font-family: "Press Start 2P", serif;
        font-weight: 400;
        font-style: normal;
        text-transform: uppercase;
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
        background-color: #FDD;
    }
</style>