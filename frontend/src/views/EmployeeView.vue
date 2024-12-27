<template>
    <div class="container mt-4">
        <h2>Mitarbeiter</h2>
        <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#addcanvas">Add</button>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Vorname</th>
                    <th>Nachname</th>
                    <th>Team</th>
                    <th>Position</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="employee in employees" class="clickableRow">
                    <td>{{ employee.name }}</td>
                    <td>{{ employee.surname }}</td>
                    <td>{{ employee.team }}</td>
                    <td>{{ employee.position }}</td>
                    <td>
                        <div class="dropdown">
                            <button class="btn btn-link" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                                    <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
                                </svg>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#" data-bs-toggle="offcanvas" data-bs-target="#updatecanvas" @click="openEditCanvas(employee)">Bearbeiten</a></li>
                                <li><a class="dropdown-item" href="#" @click="deleteEmployee(employee.id)">Löschen</a></li>
                            </ul>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>


    <div class="offcanvas offcanvas-end" tabindex="-1" id="addcanvas">
        <div class="offcanvas-header">
            <h5 id="addcanvasLabel">Mitarbeiter hinzufügen</h5>
            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
        </div>
        <div class="offcanvas-body">
            <form>
                <div class="mb-3">
                    <label for="name" class="form-label">Vorname</label>
                    <input type="text" class="form-control" id="name" v-model="formData.name">
                </div>
                <div class="mb-3">
                    <label for="surname" class="form-label">Nachname</label>
                    <input type="text" class="form-control" id="surnmae" v-model="formData.surname">
                </div>
                <div class="mb-3">
                    <label for="team" class="form-label">Team</label>
                    <input type="text" class="form-control" id="team" v-model="formData.team">
                </div>
                <div class="mb-3">
                    <label for="position" class="form-label">Position</label>
                    <input type="text" class="form-control" id="position" v-model="formData.position">
                </div>
                <button type="submit" class="btn btn-primary" @click="addEmployee">Bestätigen</button>
            </form>
        </div>
    </div>


    <div class="offcanvas offcanvas-end" tabindex="-1" id="updatecanvas">
        <div class="offcanvas-header">
            <h5 id="updatecanvasLabel">Mitarbeiter bearbeiten</h5>
            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
        </div>
        <div class="offcanvas-body">
            <form>
                <div class="mb-3">
                    <label for="name" class="form-label">Vorname</label>
                    <input type="text" class="form-control" id="name" v-model="formData.name" >
                </div>
                <div class="mb-3">
                    <label for="surname" class="form-label">Nachname</label>
                    <input type="text" class="form-control" id="surnmae" v-model="formData.surname">
                </div>
                <div class="mb-3">
                    <label for="team" class="form-label">Team</label>
                    <input type="text" class="form-control" id="team" v-model="formData.team">
                </div>
                <div class="mb-3">
                    <label for="position" class="form-label">Position</label>
                    <input type="text" class="form-control" id="position" v-model="formData.position">
                </div>
                <button type="submit" class="btn btn-primary" @click="updateEmployee">Bestätigen</button>
            </form>
        </div>
    </div>


</template>

<script>

// @ is an alias to /src
export default {
    name: 'HomeView',
    
    data() {
        return {
            employees: [],
            showModal: true,
            formData: {
                id: "",
                name: "",
                surname: "",
                team: "",
                position: "",
            },
        }
    },
    methods: {
        async getEmployees() {
            const url = "http://127.0.0.1:8000/employees";
            const resp = await fetch(url).then(data => data.json());
            this.employees = resp
            console.log(this.employees)
        },
        async addEmployee(){
            const url = "http://127.0.0.1:8000/employees"
            const resp = await fetch(url, {method: "POST", 
                headers: {
                "Content-Type": "application/json"
                },
                body: JSON.stringify(this.formData),
            });
            
            if (resp.ok) {
                const result = await resp.json();
                console.log("Success", result)
            } else {
                console.error("Error", resp.status);
            }
        },
        openEditCanvas(employee) {
            this.formData = { ...employee };
        },

        async updateEmployee() {
            const url = `http://127.0.0.1:8000/employees/${this.formData.id}`
            const resp = await fetch(url, {method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(this.formData),
            });
        },

        async deleteEmployee(employeeid) {
            const url = `http://127.0.0.1:8000/employees/${employeeid}`
            const resp = await fetch(url, {method: "DELETE", 
                headers: {
                    "Content-Type": "application/json"
                },
            });
            location.reload()
        }
    },
    mounted() {
        this.getEmployees();
    }
}
</script>