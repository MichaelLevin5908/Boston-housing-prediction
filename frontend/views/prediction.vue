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
            <label class="col-5 px-0" for="INDUS">INDUS</label>
            <input
              class="form-control"
              v-model.trim="housingData.INDUS"
              type="number"
              id="INDUS"
            />
          </div>
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="CHAS">CHAS</label>
            <input
              class="form-control"
              v-model.trim="housingData.CHAS"
              type="number"
              id="CHAS"
            />
          </div>
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="NOX">NOX</label>
            <input
              class="form-control"
              v-model.trim="housingData.NOX"
              type="number"
              id="NOX"
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
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="RAD">RAD</label>
            <input
              class="form-control"
              v-model.trim="housingData.RAD"
              type="number"
              id="RAD"
            />
          </div>
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="TAX">TAX</label>
            <input
              class="form-control"
              v-model.trim="housingData.TAX"
              type="number"
              id="TAX"
            />
          </div>
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="PTRATIO">PTRATIO</label>
            <input
              class="form-control"
              v-model.trim="housingData.PTRATIO"
              type="number"
              id="PTRATIO"
            />
          </div>
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="B">B</label>
            <input
              class="form-control"
              v-model.trim="housingData.B"
              type="number"
              id="B"
            />
          </div>
          <div class="form-group col-md-4">
            <label class="col-5 px-0" for="LSTAT">LSTAT</label>
            <input
              class="form-control"
              v-model.trim="housingData.LSTAT"
              type="number"
              id="LSTAT"
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
import { getAPI } from "@/axios";
export default {
  name: "Posts",
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
      APIResult: []
    };
  },
  methods: {
    predict() {
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