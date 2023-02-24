<template>
    <nav class="navbar navbar-expand-md" style="background-color: rgb(255, 255, 255);">
      <div class="mx-auto order-0">
        <a class="navbar-brand mx-auto" href="/">
          <img src="https://jerry914.github.io/nlp-judgement-frontend/static/img/dlogo.d370639.jpeg" alt="Logo" width="30" height="34" class="d-inline-block align-text-center">
          <!-- AI輔助親權判決預測網頁 -->
        </a>
      </div>
      <div class="navbar-collapse collapse order-3 dual-collapse2">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/" data-toggle="collapse" data-target=".dual-collapse2">Home</router-link>
            <div v-if="$route.name == 'HomePage'" class="underline"></div>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/userPredict" data-toggle="collapse" data-target=".dual-collapse2">Predict</router-link>
            <div v-if="$route.name == 'UserPredict'" class="underline"></div>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
a {
  color: #1F191B;
}
.underline {
  height: 4px;
  margin: auto;
  background-color: #F3BB5C;
  -webkit-transition: all .3s ease-Out;
  transition: all .3s ease-Out;
  border-radius: 10px;
}

</style>
