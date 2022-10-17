<script setup>
  import tituloComponent from "./components/tituloComponent.vue"; 
  import menuComponent from "./components/menuComponent.vue"; 
  import pieComponent from "./components/pieComponent.vue"; 
</script>

<script> 
  import { defineComponent } from "vue"; 
  export default defineComponent({ 
    name: "app", 
    components: {}, 
  }); 
</script>

<template> 
  <div class="container-xl" id="marco">  
    <div class="row" id="titulo"><tituloComponent /></div>
    <div class="row" id="central"> 
      <div id="menuNav"><menuComponent /></div> 
      <div id="contenido"><router-view /></div> </div> 
    <div class="row" id="pie"><pieComponent /></div> 
  </div> 
</template>

<style scoped>
  #marco { 
    display: flex; 
    flex-direction: column; 
    border: 2px solid rgb(160, 148, 148); 
    width: 1400px; height: 900px;
  } 
  #titulo { 
    border: 1px solid rgb(160, 148, 148); 
  } 
  #central { 
    border: 1px solid rgb(160, 148, 148); 
    width: 1318px; 
    height: 800px; 
  } 
  #menuNav { 
    border: 1px solid rgb(160, 148, 148); 
    width: 120px; 
  } 
  #contenido { 
    width: 1000px; 
  } 
  #pie { 
    width: 1318px; 
  } 
</style>
