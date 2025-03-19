<template>
    <section>
      <!--
      {
        "PassengerId": 3,
        "Name": "Mrs. Elizabeth Taylor",
        "Sex": "female",
        "Age": 28,
        "Embarked": "C",
        "Pclass": 1,
        "Fare": 24.23,
        "SibSp": 2,
        "Parch": 0,
        "Ticket": "PC 1234",
        "Cabin": "653"
      }

      
      -->
      <form @submit.prevent="sendData()" class="passenger-form">
        <label for="id">Passenger ID:</label>
        <input name="id" v-model="passenger.PassengerId" type="text" required />
        
        <label for="name">Name:</label>
        <input name="name" v-model="passenger.Name" type="text" placeholder="Mr. Ben Lambrechts" required />

        <label for="age">Age:</label>
        <input name="age" v-model="passenger.Age" type="number" placeholder="26" required />

        <label for="sex">Sex:</label>
        <select name="sex" v-model="passenger.Sex">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>

        <label for="embarked">Embarked:</label>
        <select name="embarked" v-model="passenger.Embarked">
          <option value="Q">Queenstown</option>
          <option value="S">Southampton</option>
          <option value="C">Cherbourg</option>
        </select>

        <label for="class">Class:</label>
        <select name="class" v-model="passenger.Pclass">
          <option value=1>1</option>
          <option value=2>2</option>
          <option value=3>3</option>
        </select>

        <label for="fare">Fare:</label>
        <input name="fare" v-model="passenger.Fare" type="number" placeholder="23.48" required />

        <label for="sibsp">Siblings & spouses aboard:</label>
        <input name="sibsp" v-model="passenger.SibSp" type="number" placeholder="2" required />

        <label for="parch">Parents & children aboard:</label>
        <input name="parch" v-model="passenger.Parch" type="number" placeholder="2" required />

        <label for="ticket">Ticket:</label>
        <input name="ticket" v-model="passenger.Ticket" type="text" placeholder="ABC123" required />

        <label for="cabin">Cabin:</label>
        <input name="cabin" v-model="passenger.Cabin" type="text" placeholder="543" required />
        
        <button type="submit">Predict</button>        
      </form>

      <p class='error' v-if="message">{{ message }}</p>
    </section>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import axios from 'axios';
    
    const passenger = ref({});
    const message = ref('');

    const sendData = async () => {
        
        console.log("SENDING DATA", passenger.value);

        axios.post('http://localhost:8000/predict', passenger.value).then((response) => {
            console.log("GOT RESPONSE", response);
            if(response.status == 200) {
                console.log("Predicted survival value", response.data);
                if(response.data.prediction == 1) {
                    message.value = "Go ahead, everything is fine!";
                } else {
                    message.value = "It is not recommended to board the boat.";
                }
            }           
        }).catch((error) => {
            console.log("ERROR",error);       
            message.value = error.response.data.detail;
        });
    };
  </script>
  
  <style scoped>
  
  section {
    width: 50vw;
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

  label, input, select {
    display: inline-block;
    width: 50%;
    margin-bottom: 12px;
    padding: 8px;
    margin-top: 5px;
    font-family: "Press Start 2P", serif;
  }

  input, select {
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
  