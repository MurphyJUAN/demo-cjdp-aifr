<template>
    <div class="d-inline-flex">
        <div class="tri-state-toggle">

            <button @click="activeSwitch(0, '月')" :class="{ 'active': active_status[0] }" class="tri-state-toggle-button" id="toggle-button1">
                月
            </button>

            <button @click="activeSwitch(1, '週')" v-bind:class="{ 'active': active_status[1] }"  class="tri-state-toggle-button" id="toggle-button2">
                週
            </button>

            <button @click="activeSwitch(2, '日')" v-bind:class="{ 'active': active_status[2] }" class="tri-state-toggle-button" id="toggle-button3">
                日
            </button>

        </div>
    </div>
</template>

<script>
export default {
  name: 'Toggle',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      active_status: [false, false, true],
      select_mode: '日',
    };
  },
  methods: {
    activeSwitch(id, text) {
      console.log(this.active_status);
      this.$set(this.active_status, id, true);
      this.$emit('selectType', text);
      this.select_mode = text;
      for (let index = 0; index < this.active_status.length; index++) {
        if (index !== id) {
          this.$set(this.active_status, index, false);
        }
      }
    },
  },
};
</script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

    .tri-state-toggle {
        background: rgba(165,170,174,0.25);
        box-shadow: inset 0 2px 8px 0 rgba(165,170,174,0.25);
        border-radius: 24px;
        display: inline-block;
        overflow: hidden;
        display: inline-flex;
        flex-direction: row;
        transition: all 50ms ease;
    }

    .tri-state-toggle-button {
        border-radius: 22px;
        height: 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 3rem;
        background-color: transparent;
        border: 0px solid transparent;
        margin: 2px;
        color: #727C8F;
        cursor: pointer;
        transition: all 50ms ease;
    }

    .tri-state-toggle-button.active {
        background-image: linear-gradient(-180deg, #fff 0%, #FAFAFA 81%, #F2F2F2 100%);
        border: 1px solid rgba(207,207,207,0.6);
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.1);
        color: #6744B1;
        font-weight: 500;
        transition: all 50ms ease;
    }

    .tri-state-toggle-button:focus {
        outline: none;
    }

  </style>
