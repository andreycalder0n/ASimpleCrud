<template> //Layout de la ventana 
    <form>
        <div class="form-group">
            <label>Title</label>
            <input
                type="text"
                v-model="project.title"
                class="form-control"
                id="title"
            />
        </div> //Espacio correspondiente al titulo

        <div class="form-group">
            <label for="exampleFormControlTextarea1">Descripción</label>
            <textarea
                v-model="project.description"
                class="form-control"
                id="description"
                rows="5"
            ></textarea>
        </div> //Espacio correspondiente a la descripcion

        <div class="form-group">
            <label>Technology</label>
            <input
                type="text"
                v-model="project.technology"
                class="form-control"
                id="technology"
            />
        </div> //Espacio para agregar la tecnologia

        <div id="botones"> //Se agrega los botones de Guardar y editar
            <button id="btn_guardar" type="submit" class="btn btn-success" @click="insert()">Guardar</button>
            <button type="submit" class="btn btn-primary" @click="editar()">Editar</button>
        </div>
    </form>
</template>

<style scoped>
    #botones{
        margin-top: 20px;
    }
    #btn_guardar{
        margin-right: 5px;
    }
</style>

<script> //Javascript del la vista Projects
import { stringify } from 'postcss';


export default {
    data() {
        return {
            project: {
                title: "",
                description: "",
                technology: "",
            },
        };
        idx = undefined;
    },
    
    mounted() {
        if (this.$route.params.id != undefined) {
            this.idx = this.$route.params.id;
            this.consultarProject(this.idx);
        }
    },

    methods: {

        async insert() {
            const formdata = new FormData();

            formdata.append("title", this.project.title);
            formdata.append("description", this.project.description);
            formdata.append("technology", this.project.technology);

            let url = "http://127.0.0.1:8000/api/projects/";

            let response = await fetch(url, {
                method:"POST",
                body: formdata,
            });
        
        },

        async consultarProject(id){
            let response
            let url = "http://127.0.0.1:8000/api/projects/" + id + "/";
            try {
                response = await fetch(url);
                const datos = await response.json();
                this.project = datos;
            }
            catch(error) {
                alert("Error: " + " " + error);
            }
        },

        async editar() {
            const formdata = new FormData();

            formdata.append("title", this.project.title);
            formdata.append("description", this.project.description);
            formdata.append("technology", this.project.technology);

            alert(this.idx);

            let url = "http://127.0.0.1:8000/api/projects/" + id + "/";

            let response = await fetch(url, {
                method: "PUT",
                body: formdata,
            });

        },
    },
};


</script>
