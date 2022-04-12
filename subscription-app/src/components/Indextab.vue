<template>
    <div class="pt-5">
        <div v-if="subscriptions && subscriptions.length">
           
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Location</th>
      <th scope="col">Department</th>
      <th scope="col">category</th>
       <th scope="col">Subcategory</th>
         <th scope="col">Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="subscription of subscriptions" v-bind:key="subscription.id">
      <th scope="row">{{ subscription.id }}</th>
      <td>{{ subscription.Location }}</td>
      <td>{{ subscription.Department }}</td>
       <td>{{ subscription.category }}</td>
        <td>{{ subscription.subcategory }}</td>
        <td> <router-link :to="{name: 'edit', params: { id: subscription.id }}" class="btn btn-sm btn-primary">Edit</router-link>
         <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteSubscription(subscription)">Delete</button>
        </td>
    
    </tr>
   
  </tbody>
</table>
        <p  v-if="subscriptions.length == 0">No subscriptions</p>
    </div>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            subscriptions: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteSubscription: function(subscr) {
            if (confirm('Delete ' + subscr.Location)) {
                axios.delete(`http://127.0.0.1:8000/api/metadata/${subscr.id}`)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/metadata/')
                .then( response => {
                    console.log(response)
                    this.subscriptions = response.data
                });
        }
    },
}
</script>