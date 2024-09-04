<template>
  <div class="container-fluid d-flex flex-column justify-content-center align-items-center" style="min-height: 100vh;">
    <div class="text-center mb-4">
      <h1 v-if="!APIResult.length" class="title">Enter Housing Data to Make Prediction</h1>
      <h1 v-else style="font-size:4rem">{{ APIResult }}</h1>
    </div>
    <div class="card p-4 shadow-sm" style="width: 100%; max-width: 700px;">
      <form @submit.prevent="predict">
        <div class="form-row">
          <div class="form-group col-md-6 d-flex">
            <label for="CRIM" class="label-width">CRIM</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.CRIM"
              type="number"
              id="CRIM"
              placeholder="Crime rate"
              required
            />
          </div>
          <div class="form-group col-md-6 d-flex">
            <label for="ZN" class="label-width">ZN</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.ZN"
              type="number"
              id="ZN"
              placeholder="Zoning"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6 d-flex">
            <label for="INDUS" class="label-width">INDUS</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.INDUS"
              type="number"
              id="INDUS"
              placeholder="Industry"
              required
            />
          </div>
          <div class="form-group col-md-6 d-flex">
            <label for="CHAS" class="label-width">CHAS</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.CHAS"
              type="number"
              id="CHAS"
              placeholder="Charles River dummy variable"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6 d-flex">
            <label for="NOX" class="label-width">NOX</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.NOX"
              type="number"
              id="NOX"
              placeholder="Nitric oxides concentration"
              required
            />
          </div>
          <div class="form-group col-md-6 d-flex">
            <label for="RM" class="label-width">RM</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.RM"
              type="number"
              id="RM"
              placeholder="Average number of rooms"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6 d-flex">
            <label for="AGE" class="label-width">AGE</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.AGE"
              type="number"
              id="AGE"
              placeholder="Age of buildings"
              required
            />
          </div>
          <div class="form-group col-md-6 d-flex">
            <label for="DIS" class="label-width">DIS</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.DIS"
              type="number"
              id="DIS"
              placeholder="Distance to employment centers"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6 d-flex">
            <label for="RAD" class="label-width">RAD</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.RAD"
              type="number"
              id="RAD"
              placeholder="Index of accessibility to highways"
              required
            />
          </div>
          <div class="form-group col-md-6 d-flex">
            <label for="TAX" class="label-width">TAX</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.TAX"
              type="number"
              id="TAX"
              placeholder="Property tax rate"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6 d-flex">
            <label for="PTRATIO" class="label-width">PTRATIO</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.PTRATIO"
              type="number"
              id="PTRATIO"
              placeholder="Pupil-teacher ratio"
              required
            />
          </div>
          <div class="form-group col-md-6 d-flex">
            <label for="LSTAT" class="label-width">LSTAT</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.LSTAT"
              type="number"
              id="LSTAT"
              placeholder="Lower status of the population"
              required
            />
          </div>
        </div>
        <div class="text-center">
          <button type="submit" class="btn btn-primary btn-lg btn-block mt-4 btn-submit">
            Submit
          </button>
        </div>
        <div v-if="loading" class="text-center mt-3">
          <div class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
        <div v-if="errorMessage" class="alert alert-danger mt-3" role="alert">
          {{ errorMessage }}
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { getAPI } from "@/axios";

export default {
  name: "PredictionPosts",
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
      APIResult: [],
      loading: false,
      errorMessage: null,
    };
  },
  methods: {
    predict() {
      this.loading = true;
      this.errorMessage = null;
      getAPI
        .get("/predict", {
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
          this.APIResult = response.data;
          console.log(response.data);
        })
        .catch(err => {
          this.errorMessage = "Failed to fetch prediction. Please try again.";
          console.error(err);
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>

<style>/* Custom styles */
/* Custom styles *//* Custom styles */
body {
  background-color: #f8f9fa;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}

.card {
  border-radius: 10px;
  border: none;
  width: 100%;
  max-width: 700px;
}

h1.title {
  font-weight: 300;
  color: #343a40;
  font-size: 2.5rem; /* Larger font size for the title */
  text-align: center; /* Center align the title */
  margin-bottom: 1.5rem;
}

.form-control {
  border-radius: 0.375rem;
  border: 1px solid #ced4da;
  font-size: 1.25rem; /* Larger font size for input text */
}

.form-control-lg {
  height: calc(1.5em + 1rem + 2px);
  font-size: 1.25rem;
  line-height: 1.5;
}

.label-width {
  min-width: 140px; /* Consistent label width */
  margin-right: 10px; /* Spacing between label and input */
  font-size: 1.25rem; /* Larger font size for labels */
}

.form-group {
  margin-bottom: 1rem; /* Increased spacing between form groups */
  display: flex;
  align-items: center; /* Vertically center labels with inputs */
  justify-content: center; /* Center-align the labels and inputs */
}

.form-group .form-control {
  flex-grow: 1; /* Make the input fields take up the remaining space */
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  width: 100%;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #004085;
}

.spinner-border {
  width: 3rem;
  height: 3rem;
}

.alert-danger {
  border-radius: 0.375rem;
}

.btn-submit {
  padding: 1rem 2rem;
  font-size: 1.5rem;
  margin-top: 20px; /* Add margin to space out from the form */
}

</style>