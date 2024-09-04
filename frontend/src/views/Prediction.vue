<template>
  <div class="container-fluid d-flex flex-column justify-content-center align-items-center" style="min-height: 100vh;">
    <div class="text-center mb-4">
      <h1 v-if="!APIResult.length">Enter Housing Data to Make Prediction</h1>
      <h1 v-else style="font-size:4rem">{{ APIResult }}</h1>
    </div>
    <div class="card p-4 shadow-sm" style="width: 100%; max-width: 700px;">
      <form @submit.prevent="predict">
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="CRIM">CRIM</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.CRIM"
              type="number"
              id="CRIM"
              placeholder="Crime rate"
              required
            />
          </div>
          <div class="form-group col-md-6">
            <label for="ZN">ZN</label>
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
          <div class="form-group col-md-6">
            <label for="INDUS">INDUS</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.INDUS"
              type="number"
              id="INDUS"
              placeholder="Industry"
              required
            />
          </div>
          <div class="form-group col-md-6">
            <label for="CHAS">CHAS</label>
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
          <div class="form-group col-md-6">
            <label for="NOX">NOX</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.NOX"
              type="number"
              id="NOX"
              placeholder="Nitric oxides concentration"
              required
            />
          </div>
          <div class="form-group col-md-6">
            <label for="RM">RM</label>
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
          <div class="form-group col-md-6">
            <label for="AGE">AGE</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.AGE"
              type="number"
              id="AGE"
              placeholder="Age of buildings"
              required
            />
          </div>
          <div class="form-group col-md-6">
            <label for="DIS">DIS</label>
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
          <div class="form-group col-md-6">
            <label for="RAD">RAD</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.RAD"
              type="number"
              id="RAD"
              placeholder="Index of accessibility to highways"
              required
            />
          </div>
          <div class="form-group col-md-6">
            <label for="TAX">TAX</label>
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
          <div class="form-group col-md-6">
            <label for="PTRATIO">PTRATIO</label>
            <input
              class="form-control form-control-lg"
              v-model.trim="housingData.PTRATIO"
              type="number"
              id="PTRATIO"
              placeholder="Pupil-teacher ratio"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-12">
            <label for="LSTAT">LSTAT</label>
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

<style>
/* Custom styles */
body {
  background-color: #f8f9fa;
  position: center;
}

.card {
  border-radius: 10px;
  border: none;
}

h1 {
  font-weight: 300;
  color: #343a40;
}

.form-control {
  border-radius: 0.375rem;
  border: 1px solid #ced4da;
}

.form-control-lg {
  height: calc(1.5em + 1rem + 2px);
  font-size: 1.25rem;
  line-height: 1.5;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
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


.btn-submit {
  padding: 1rem 2rem; 
  font-size: 1.5rem; 
} 

}
</style>

