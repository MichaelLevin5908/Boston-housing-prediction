<template>
  <div id="app">
    <h1>Housing Price Prediction</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="CRIM">CRIM (Crime Rate):</label>
        <input type="text" id="CRIM" v-model="form.CRIM" required>
      </div>
      <div>
        <label for="ZN">ZN (Residential Land Zone Proportion):</label>
        <input type="text" id="ZN" v-model="form.ZN" required>
      </div>
      <div>
        <label for="RM">RM (Average Number of Rooms):</label>
        <input type="text" id="RM" v-model="form.RM" required>
      </div>
      <div>
        <label for="AGE">AGE (Proportion of Old Units):</label>
        <input type="text" id="AGE" v-model="form.AGE" required>
      </div>
      <div>
        <label for="DIS">DIS (Distance to Employment Centers):</label>
        <input type="text" id="DIS" v-model="form.DIS" required>
      </div>
      <button type="submit">Predict</button>
    </form>
    <div v-if="prediction">
      <h2>Predicted House Price: {{ prediction }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        CRIM: '',
        ZN: '',
        RM: '',
        AGE: '',
        DIS: '',
      },
      prediction: ''
    };
  },
  methods: {
    async submitForm() {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.form),
      });
      const data = await response.json();
      this.prediction = `$${data.prediction}`;
    }
  }
}
</script>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 50px;
}

form {
  margin-bottom: 20px;
}

input {
  margin: 10px;
  padding: 5px;
  width: 80%;
  max-width: 300px;
}

button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

h2 {
  color: #4CAF50;
}
</style>

