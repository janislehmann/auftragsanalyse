<template>
    <h1>Bitte Mitarbeiter Daten eingeben</h1>
    <label for="name">Vorname:</label>
    <input id="name" v-model="formData.name" placeholder="Vorname"/>
    <br/>

    <label for="surname">Nachname:</label>
    <input id="surname" v-model="formData.surname" placeholder="Nachname"/>
    <br/>

    <label for="team">Team zugehörigkeit:</label>
    <input id="team" v-model="formData.team" placeholder="Team"/>
    <br/>

    <label for="position">Position</label>
    <input id="position" v-model="formData.position" placeholder="Position"/>
    <br/>

    <button v-on:click="addEmployee()">Bestätigen</button>
</template>

<script>
export default {
    name: "DataInput",
    data() {
        return {
            formData: {
                name: "",
                surname: "",
                team: "",
                position: "",
            },
        };
    },

    methods: {
        async addEmployee(){
            const url = "http://127.0.0.1:8000/employees"
            const resp = await fetch(url, {method: "POST", 
                headers: {
                "Content-Type": "application/json"
                },
                body: JSON.stringify(this.formData),});
            
            if (resp.ok) {
                const result = await resp.json();
                console.log("Success", result)
            } else {
                console.error("Error", resp.status);
            }
        }
    }
}

</script>

<style scoped>
label {
    padding: 8px;
}
</style>