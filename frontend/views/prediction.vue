<template>
  <div
    class="d-flex flex-column justify-content-center align-items-center"
    style="height: 80vh"
  >
    <div class="p-2">
      <h1 v-if="!APIResult.length">Enter Housing Data to Make Prediction</h1>
      <h1 v-else style="font-size:4rem">{{ APIResult }}</h1>
    </div>
    <div class="p-2">
      <form @submit.prevent>
        <div class="form-row" style="max-width:500px">
          <!-- Existing fields -->
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="CRIM">CRIM</label>
            <input
              class="form-control"
              v-model.trim="housingData.CRIM"
              type="number"
              id="CRIM"
            />
          </div>
          <!-- Add other fields here... -->
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="MEDV">MEDV</label>
            <input
              class="form-control"
              v-model.trim="housingData.MEDV"
              type="number"
              id="MEDV"
            />
          </div>
          <button
            @click="predict"
            type="button"
            class="btn btn-primary btn-lg btn-block"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Prediction",
  data() {
    return {
      housingData: {
        CRIM: "",
        ZN: "",
        INDUS: "",
        CHAS: "",
        NOX: "",
        RM: "",
        AGE: "",
        DIS: "",
        RAD: "",
        TAX: "",
        PTRATIO: "",
        LSTAT: ""
      },
      APIResult: ""
    };
  },
  methods: {
    predict() {
      axios
        .get("http://127.0.0.1:5000/predict", {
          params: {
            CRIM: this.housingData.CRIM,
            ZN: this.housingData.ZN,
            INDUS: this.housingData.INDUS,
            CHAS: this.housingData.CHAS,
            NOX: this.housingData.NOX,
            RM: this.housingData.RM,
            AGE: this.housingData.AGE,
            DIS: this.housingData.DIS,
            RAD: this.housingData.RAD,
            TAX: this.housingData.TAX,
            PTRATIO: this.housingData.PTRATIO,
            LSTAT: this.housingData.LSTAT,
          }
        })
        .then(response => {
          console.log("Received data successfully");
          this.APIResult = response.data;
          console.log(response.data);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style>
/* Add your custom styles here */
</style>


  