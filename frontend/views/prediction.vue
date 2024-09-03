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
            <div class="form-group col-md-4">
              <label class="col-5 px-0" for="CRIM">CRIM</label>
              <input
                class="form-control"
                v-model.trim="housingData.CRIM"
                type="number"
                id="CRIM"
              />
            </div>
            <div class="form-group col-md-4">
              <label class="col-5 px-0" for="ZN">ZN</label>
              <input
                class="form-control"
                v-model.trim="housingData.ZN"
                type="number"
                id="ZN"
              />
            </div>
            <div class="form-group col-md-4">
              <label class="col-5 px-0" for="RM">RM</label>
              <input
                class="form-control"
                v-model.trim="housingData.RM"
                type="number"
                id="RM"
              />
            </div>
            <div class="form-group col-md-4">
              <label class="col-5 px-0" for="AGE">AGE</label>
              <input
                class="form-control"
                v-model.trim="housingData.AGE"
                type="number"
                id="AGE"
              />
            </div>
            <div class="form-group col-md-4">
              <label class="col-5 px-0" for="DIS">DIS</label>
              <input
                class="form-control"
                v-model.trim="housingData.DIS"
                type="number"
                id="DIS"
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
          RM: "",
          AGE: "",
          DIS: ""
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
              RM: this.housingData.RM,
              AGE: this.housingData.AGE,
              DIS: this.housingData.DIS
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
  