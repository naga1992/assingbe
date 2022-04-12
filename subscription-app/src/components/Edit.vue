<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="name">Location</label>
                <input
                    type="text"
                    class="form-control"
                    id="Location"
                    v-model="subscription.Location"
                    v-validate="'required'"
                    name="Lcoation"
                    placeholder="Enter Location"
                    :class="{'is-invalid': errors.has('subscription.Location') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid Location
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
                    Please provide a valid category.
                </div>
            </div>
            <div class="form-group">
                <label for="amount">subcategory</label>
                <input
                    type="text"
                    name="subcategory"
                    v-validate="'required'"
                    class="form-control"
                    id="amount"
                    v-model="subscription.subcategory"
                    placeholder="Enter subcategory"
                    :class="{'is-invalid': errors.has('subscription.subcategory') && submitted}">
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
    mounted() {
        axios.get('http://127.0.0.1:8000/api/metadata/' + this.$route.params.id)
            .then( response => {
                console.log(response.data)
                this.subscription = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`http://127.0.0.1:8000/api/metadata/${this.subscription.id}/`,
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