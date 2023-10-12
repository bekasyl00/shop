<script >
import Header from '../components/header.vue';
import HeadSection from '../components/HeadSection.vue';
import ItemsSection from '../components/ItemsSection.vue';
export default {
    props:['basket','addtob'],
    components:{Header,HeadSection,ItemsSection}
}
</script>

<template>
    <div>
        <HeadSection />
        <Header :basket="basket"/>
        <ItemsSection :addtob="addtob"/>

    </div>


</template>
<style>


</style>