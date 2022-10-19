<template>
    <h3>Listado</h3>
    <div>
        <table class="table  table-sm" id="tabla">
            <thead class="table-dark">
                <tr>
                    <th scope="col">Id</th>
                    <th scope="col">Title</th>
                    <th scope="col">Description</th>
                    <th scope="col">Technology</th>
                    <th scope="col">Fecha</th>
                    <th colspan="2">Acciones</th>
                </tr>
            </thead>
            <tbody v-for="elemento in listado" :key="elemento.id">
                <tr>
                    <td>{{elemento.id}}</td>
                    <td>{{elemento.title}}</td>
                    <td>{{elemento.description}}</td>
                    <td>{{elemento.technology}}</td>
                    <td>{{elemento.created_ad}}</td>
                    <td><button class="btn btn-info btn-block" @click="this.$router.push(`/envio/${elemento.id}`)">Update</button></td>
                    <td><button type="submit" @click="deleteReg(elemento.id)" class="btn btn-danger btn-block">Del</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "envio",
    
    data() {
        return {
            listado: [],
        };
    },

    methods: {
        async listar() {

            let response
            let url = "http://127.0.0.1:8000/api/projects/";
            try {
                response = await fetch(url);
                const datos = await response.json();
                this.listado = datos;
            }
            catch (error) {
                alert("ERROR: " + " " + error)
            }
        },

        async deleteReg(id) {
            const elimina = confirm("¿Está seguro de eliminar este resgitro?")

            if(elimina) {
                let url = "http://127.0.0.1:8000/api/projects/" + id + "/";
                try {
                    let response = await fetch(url, {
                        method: "DELETE",
                        headers: {'content-type': 'application/json'},
                    });
                    
                    if (response.ok){
                        alert("Registro eliminado exitosamente " +  id)
                        this.$options.methods.listar.bind(this)(); //ejecutamos el metodo listar
                    }
                }
                catch (error) {
                    alert("ERROR: " + " " + error);
                } //try catch
            } //If elimina
        } //deleteReg
    }// se cierra methods
}; //export default
</script>

<style scoped>
    #tabla {
        color:aquamarine;
    }
</style>