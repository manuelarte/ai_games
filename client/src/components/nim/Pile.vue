<template>
    <div class="row">
        <Dot v-for="n in number" v-bind:key="n" :n="n" :selecteable="selecteable"
            v-on:dot-selected="onDotSelected"/>
    </div>
</template>

<script>
import Dot from '@/components/nim/Dot.vue'
export default {
  name: 'Pile',
    components: {Dot},
    comments: {
      Dot
  },
  props: {
    pileNumber: Number,
    number: Number,
    selecteable: Boolean
  },
  data() {
      return {
          numberOfDots: 0
      }
  },
  methods: {
    onDotSelected: function (value) {
        if (value) {
            this.numberOfDots += 1
        } else {
            this.numberOfDots -= 1
        }
        console.log("dots selected " + this.numberOfDots + ", in pileNumber " + this.pileNumber)
        this.$emit('on-action', [this.pileNumber, this.numberOfDots])
  }
}
}
</script>

<style>
    .row {
        display: block ruby;
    }
</style>