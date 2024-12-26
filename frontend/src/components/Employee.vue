<template>
    <p>Vorname: {{ name }}</p>
    <p>Nachname: {{ surname }}</p>
    <p>Team: {{ team }}</p>
    <p>Position: {{ position }}</p>
</template>


<script>
export default {
    name: "Employee",
    props: {
        name: String,
        surname: String,
        team: String,
        position: String
    }
}

</script>