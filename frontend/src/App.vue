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
        <label for="INDUS">INDUS (Proportion of Non-Retail Business Acres):</label>
        <input type="text" id="INDUS" v-model="form.INDUS" required>
      </div>
      <div>
        <label for="CHAS">CHAS (Charles River Dummy Variable):</label>
        <input type="text" id="CHAS" v-model="form.CHAS" required>
      </div>
      <div>
        <label for="NOX">NOX (Nitric Oxide Concentration):</label>
        <input type="text" id="NOX" v-model="form.NOX" required>
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
      <div>
        <label for="RAD">RAD (Index of Accessibility to Radial Highways):</label>
        <input type="text" id="RAD" v-model="form.RAD" required>
      </div>
      <div>
        <label for="TAX">TAX (Property Tax Rate):</label>
        <input type="text" id="TAX" v-model="form.TAX" required>
      </div>
      <div>
        <label for="PTRATIO">PTRATIO (Pupil-Teacher Ratio):</label>
        <input type="text" id="PTRATIO" v-model="form.PTRATIO" required>
      </div>
      <div>
        <label for="LSTAT">LSTAT (Lower Status Population Percentage):</label>
        <input type="text" id="LSTAT" v-model="form.LSTAT" required>
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
        INDUS: '',
        CHAS: '',
        NOX: '',
        RM: '',
        AGE: '',
        DIS: '',
        RAD: '',
        TAX: '',
        PTRATIO: '',
        B: '',
        LSTAT: '',
      },
      prediction: ''
    };
  },
  methods: {
    async submitForm() {
      const response = await fetch('https://your-app-name.herokuapp.com/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.form),
      });
      if (response.ok) {
        const data = await response.json();
        this.prediction = `$${data.prediction}`;
      } else {
        console.error('Error:', response.statusText);
      }
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