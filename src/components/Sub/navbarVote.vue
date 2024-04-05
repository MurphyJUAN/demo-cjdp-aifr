<template>
    <div>
        <b-navbar variant="faded" type="light">
            <b-container class="bv-example-row">
                <b-navbar-brand href="#" class="bold-text">Vote Monitor</b-navbar-brand>
            </b-container>

        </b-navbar>
        <hr class="line">
    </div>
</template>

<script>
export default {
  name: 'NavbarVote',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
};
</script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .line {
    margin: 0;
  }
  .bold-text {
    font-weight: bold;
  }
  </style>
