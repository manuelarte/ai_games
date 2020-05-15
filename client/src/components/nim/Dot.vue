<template>
    <div>
       <span class="dot" v-on:click="dotClicked"
             v-bind:class="{colored: selecteable && isSelected, clickable: selecteable}">{{ n }}</span>
    </div>
</template>

<script>
export default {
  name: 'Dot',
  props: {
    n: Number,
    selecteable: Boolean
  },
  data() {
      return {
          isSelected: false
      }
  },
  methods: {
    dotClicked: function() {
      this.isSelected = !this.isSelected;
      this.$emit('dot-selected', this.isSelected)
    }
  }
}
</script>

<style>
    .dot {
        height: 25px;
        width: 25px;
        background-color: #448aff;
        border-radius: 50%;
        display: inline-block;
        margin: 4px;
    }
    .colored {
        background-color: #ff5252;
    }
    .clickable {
        cursor: pointer
    }
</style>