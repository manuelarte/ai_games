<template>
  <div class="nim_main">
    <div class="spinner" v-if="isLoading">
      <md-progress-spinner class="md-accent" md-mode="indeterminate"></md-progress-spinner>
    </div>
    <div v-if="!isLoading && nimDto">
      <div class="turn">
        <h1 v-if="nimDto.human_turn === true">Your turn</h1>
        <h1 v-if="nimDto.human_turn === false">AI turn</h1>
        <h1 v-if="nimDto.winner === true">Your win!</h1>
        <h1 v-if="nimDto.winner === false">Your lose!</h1>
      </div>
      <div class="pile">
        <Pile v-for="index in nimDto.piles.length+1" v-bind:key="index" :number="nimDto.piles[index-1]" :pileNumber="index-1"
              :selecteable="pileSelected == null || index-1 == pileSelected"
            v-on:on-action="onAction"/>
        <!-- Check nimDto.winner is not set -->
        <md-button v-if="isValidAction()" class="md-fab md-mini" v-on:click="submitAction()">
            <md-icon>check</md-icon>
        </md-button>
      </div>

    </div>
  </div>
</template>

<script>
import Pile from '@/components/nim/Pile.vue'
import BackendService from "../services/api.service";

const backendService = new BackendService();

export default {
  name: 'NimMainComponent',
  components: {
    Pile
  },
  props: {
    nimDto: Object
  },
  data() {
    return {
      isLoading: true,
      isSubmittingAction: false,
      pileSelected: null,
      numberOfDots: null
    };
  },
  methods: {
    onAction: function (pileAndDots) {
      this.pileSelected = pileAndDots[0]
      this.numberOfDots = pileAndDots[1]
    },
    isValidAction: function() {
      return this.nimDto != null && this.numberOfDots > 0 && this.nimDto.piles[this.pileSelected] >= this.numberOfDots
    },
    startGame: function() {
      backendService.startGame().then(response => {
        this.nimDto = response.data
      })
      .catch(error => console.log("Error: " + error))
      .finally(() => this.isLoading = false)
    },
    submitAction: function() {
      this.isSubmittingAction = true
      backendService.submitAction(this.nimDto.id, this.pileSelected, this.numberOfDots).then(response => {
          this.nimDto = response.data
          this.pileSelected = null
          this.numberOfDots = null
          console.log(response.data)
          this.methodThatForcesUpdate()
        })
        .catch(error => console.log("Error: " + error))
        .finally(() => this.isSubmittingAction = false)
    },
    methodThatForcesUpdate() {
      // ...
      this.$forceUpdate();  // Notice we have to use a $ here
      // ...
    }
  },
  mounted () {
    if (this.nimDto == null) {
      this.startGame()
    } else {
      this.isLoading = false
    }

  }
};
</script>

<style>
  .nim_main {
      text-align: center;
  }
</style>