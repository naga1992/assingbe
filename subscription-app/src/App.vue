<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">MetaData</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add metadata</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>
