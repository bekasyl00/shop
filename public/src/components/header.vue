<script >
console.log(23+2)
export default{
    props:['basket'],
    data(){
       
   return{
      showBasket:false
     
   }
    }
    

  
}

</script>



<template>
  <header>
    <img src="/img/logo.svg" alt="">
    <ul>
        <li><RouterLink to="/" active-class="active">Главная</RouterLink></li>
        <li><RouterLink to="/items" active-class="active">Товары</RouterLink></li>
        <li><RouterLink to="/dostavka" active-class="active">Доставка</RouterLink></li>
        <li><RouterLink to="/about" active-class="active">Про нас</RouterLink></li>
        <li><img src="/img/purchase.svg" alt="" @click="showBasket = !showBasket"></li>
    </ul>
    <div class="basket" v-if="showBasket">
        <div class="box"></div>
        <h3 v-if="basket.length == 0"> товаров нет</h3>
        <div class="itens" v-else>
        <div class="iten" v-for="el in basket" :key="el.slug">
           
                <img :src="'/img/' + el.image" :alt="el.title">
                <div class="pric">
                <h3>{{ el.title }}</h3>
               
               
                  <span>   {{el.price}}$</span>
            
                 </div>
                  
            </div>
           <RouterLink to="/order" > <button >Перейти к оплате</button></RouterLink>
        
        </div>
    </div>
  </header>
</template>

<style scoped>

.basket{
    position: absolute;
    top: 50px;
    right: 0px;
    padding: 5px;
    width: 250px;
    background: #B2BAC1;
    border-radius: 2px;
    z-index: 100;
}
.basket H3{
    color: #616569;
}
.basket .box{
    background: #B2BAC1;
    position: absolute;
    top: -7px;
    right: 10px;
    width: 15px;
    height: 15px;
    transform: rotate(45deg);
}
header {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 50px;
    
}
header ul {
    list-style: none;
   
}
header ul li {
    display: inline-block;
    margin-left: 25px;
    
    cursor: pointer;
}
header ul li .active {
    padding: 5px 15px;
    background: #B2BAC1;
    border-radius: 20px;
}
header ul li .active:hover {
    color: #fff;
    background: #616569;
}
header ul li a {
    position: relative;
    bottom: 10px;
}
.iten{
  max-width: 50px;
  margin-bottom: 8px;
  padding: 3px;
  background:#B2BAC1;
  margin-left:3px;
}
.span{
  font-weight: 600;

}

/* .itens{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap:wrap */
.iten{
  max-width: 150px;


  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap:wrap

}
.iten img{
  

  width: 60px
}


.iten h3{float:right;
  margin: 0px 0px 0px 0px;
  font-size: 12px;
}
.pric{margin-top: -65px;
  margin-left: 80px;
}


.iten button{
    width: 250px;
    height: 50px;
    border: 1px solid silver;
    background: rgb(237, 237, 237);
}
</style>