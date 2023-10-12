<script >
import Header from '../components/header.vue';
import MainSection from '../components/MainSection.vue';
export default {
    props:['basket'],
    components:{Header,MainSection}
}
</script>

<template>
    <div>
        <Header :basket="basket" />
<MainSection />
    </div>


</template>
<style>
*{margin: 0;
padding: 0;}

</style>