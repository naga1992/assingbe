<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="name">Location</label>
                <input
                    type="text"
                    class="form-control"
                    id="Location"
                    v-model="subscription.Location"
                    v-validate="'required'"
                    name="name"
                    placeholder="Enter Location"
                    :class="{'is-invalid': errors.has('subscription.Location') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid Location.
                </div>
            </div>
            <div class="form-group">
                <label for="currency">Department</label>
                <input
                    type="text"
                    name="Department"
                    class="form-control"
                    v-validate="'required'"
                    id="Department"
                    v-model="subscription.Department"
                    :class="{'is-invalid': errors.has('subscription.Department') && submitted}">
                </input>    
                <div class="invalid-feedback">
                    Please provide a valid Department.
                </div>
            </div>
            <div class="form-group">
                <label for="amount">category</label>
                <input
                    type="text"
                    name="category"
                    v-validate="'required'"
                    class="form-control"
                    id="category"
                    v-model="subscription.category"
                    placeholder="Enter amount"
                    :class="{'is-invalid': errors.has('subscription.category') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid category.
                </div>
            </div>
            <div class="form-group">
                <label for="description">subcategory</label>
                <textarea
                    name="subcategory"
                    class="form-control"
                    id="subcategory"
                    v-validate="'required'"
                    v-model="subscription.subcategory"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('subscription.subcategory') && submitted}"></textarea>
                <div class="invalid-feedback">
                    Please provide a valid subcategory.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            subscription: {
                Location: '',
                Department: '',
                category: '',
                subcategory: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.currency)
                axios
                    .post('http://127.0.0.1:8000/api/metadata/',
                        this.subscription
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>