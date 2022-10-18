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