<script >
import Header from '../components/header.vue';

export default {
    props:['basket'],
    components:{Header}
}
</script>

<template>
    <div>
        <Header :basket="basket"/>
        <h1>Доставка</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem saepe modi omnis nostrum, atque voluptates, molestiae error fugit non eligendi, nisi quas in quae eveniet pariatur? Debitis magni adipisci voluptatum.</p>
</div>


</template>
<style>

</style>