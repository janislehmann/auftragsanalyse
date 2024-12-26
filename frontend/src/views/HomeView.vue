<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    
  </div>
  <Employee :name="employee.name" :surname="employee.surname" :team="employee.team" :position="employee.position" v-for="employee in employees" />
</template>

<script>
// @ is an alias to /src
import Employee from '@/components/Employee.vue';
export default {
  name: 'HomeView',
  components: {
    Employee
  },
  data() {
    return {
      employees: []
    }
  },
  methods: {
    async getEmployees() {
      const url = "http://127.0.0.1:8000/employees";
      const resp = await fetch(url).then(data => data.json());
      this.employees = resp
      console.log(this.employees)
    }
  },
  mounted() {
    this.getEmployees();
  }
}
</script>
