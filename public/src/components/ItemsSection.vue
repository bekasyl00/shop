<template>
<div class="items">
  <div class="item" v-for="el in items" :key="el.slug">
    <img :src="'/img/' + el.image" :alt="el.title">
    <h3>{{ el.title }}</h3>
    <p>{{ el.desc }}</p>
    <div class="bottom">
      <span> <s>{{el.price*125/100}}$ </s>  {{el.price}}$</span>
 <!-- <img class="svg"  :src="'/img/' + el.korz" :alt= el.korz> -->
 <div >
      <img  class="svg"   :src="'/img/' + el.korz"  @click="el.korz=el.ptich" :alt="el.title" v-on:click="addtob(el)">
    </div>
   
    </div>


  </div>
  </div>
</template>
<script>
import axios from 'axios' ;


export default{
  props:['addtob'],
    data(){
        return{
            items:[ ],
           


            
        }
    

      },
     
  
  
  
   
    
    async mounted(){
        try{
          const res = await axios.get('http://127.0.0.1:8000/api/items/?format=json')
          this.items=res.data
        }catch(error){
          console.log(error)
        }
        }
      }
</script>
<style>
.items{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap:wrap
}
.item{
  max-width: 350px;
  margin-bottom: 100px;
  padding: 12px;
  background: #f4f4f4;
  margin-left: 20px;
}
.item img:first-child{
  
  height: 50%;
  width: 100%;
}
.span{
  font-weight: 600;

}
s{
  color: rgb(174, 171, 171);
}
h3{
  margin: 12px 0;
  font-size: 20px;
}
.item p{
margin: 10px 0;
font-size: 15px;
width: 90%;
}
.item .bottom{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
@media(min-width: 500px){
  .item{
    width: 40%;
    display: block;
    
    
  }}
</style>