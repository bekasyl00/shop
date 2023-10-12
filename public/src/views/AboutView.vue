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
<h1>Про нас</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam esse qui impedit magni ad perferendis officiis, incidunt hic consequuntur sit aspernatur cupiditate illum maxime voluptatem dolor ipsam? Nobis, quia obcaecati.</p>
    </div>


</template>
<style>

</style>