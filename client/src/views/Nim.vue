<template>
  <div class="nim_view">
    <div class="md-layout md-gutter">
      <div class="md-layout-item medium">
        <NimMain :nimDto="nimDto" />
      </div>
      <div class="md-layout-item md-xsmall">
        <md-card>
          <md-card-content>
            <md-button class="md-raised md-primary" v-on:click="startGame">New Game</md-button>
            <div>
              Difficulty
              <md-button disabled>Easy</md-button>
              <md-button class="md-accent md-raised" disabled>Medium</md-button>
              <md-button disabled>Hard</md-button>
            </div>
          </md-card-content>
        </md-card>
      </div>
    </div>

  </div>
</template>

<script>
import Vue from 'vue'
// @ is an alias to /src
import BackendService from "../services/api.service";
import NimMain from '@/components/NimMain.vue'
import { MdButton } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(MdButton)

const backendService = new BackendService();

export default {
  name: 'Home',
  data() {
    return {
      nimDto: null,
      difficulty: "medium"
    }
  },
  components: {
    NimMain
  },
  methods: {
    startGame: function() {
      backendService.startGame()
        .then(response => {
          this.nimDto = response.data
        })
        .catch(error => console.log("Error: " + error))
    }
  }
}
</script>
