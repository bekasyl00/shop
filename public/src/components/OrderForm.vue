
<script >
import axios from 'axios'
export default{
    props:['basket','deleteFromBasket'],
    data(){
      
      return{
        error:'',
        name:'',
        surnam:'',
        password:'',
        email:''
      
        
      }
    },
    computed:{
      getsum(){
        return this.basket.reduce((total,next)=>total+parseFloat(next.price),0)
      }
    },
    methods:{
      // timeu(){
      //   return new Date();
      // },
      sendata(){
        if(this.basket.length == 0 || this.getsum==0)
          this.error='Корзина пустая'
        else if(this.name.length < 2)
          this.error='Имя должен быть больше 2 букв'
        else if(this.name.length > 20)
          this.error='Имя должен быть меньше 20 букв'
        else if(this.surname.length < 2)
          this.error='Фамилия должен быть больше 2 букв'
        else if(this.surname.length > 20)
          this.error='Фамилия должен быть меньше 20 букв'
          // else if(this.date.length>1)
          // this.error='asd'
        // else if(this.email.includes('@') || this.email.includes('.'))
        //   this.error='Email неверного типа'
   


        else{
          this.error=''

          
         const data={
         
          'name': this.name,
          'surname': this.surname,
          'email': this.email,
          'phone': this.phone,
          'sum': this.getsum,
          'timer': new Date(),
          'basket': JSON.stringify(this.basket)
         }
   
  
         axios.post('http://127.0.0.1:8000/api/order-add/',data)
            .then(res => {
            this.error=res.data.result
            setTimeout(()=>{
              location.href=res.data.url
            })
          })

        }
      }
    }

  
}

</script>

<template>
<div class="body">
  <div>
      <h1>Оформление заказ
      </h1>
  <div class="data">
      <div class="basket" v-if="this.basket.length>0">
          
          <div class="iten" v-for="el in basket" :key="el.slug">
             
                  <img :src="'/img/' + el.image" :alt="el.title">
                  <div class="pric">
  
                    
                    <h3>{{ el.title }}</h3>
                    <span>   {{el.price}}$</span> </div>
              <button @click="deleteFromBasket(el.slug)">Удалить</button>
                  
                    
              
      </div>
      <span >Итого :{{ getsum }}$</span>
          </div>
          <div v-else>
              <h2>Товаров нет!</h2>
  </div>
      </div>
      <form >
        <p class="error">{{ error }}</p>
          <input type="text" v-model="name" placeholder="ваше имя">
          <input type="text" v-model="surname" placeholder="ваше фамилия">
          <input type="email" v-model="email" placeholder="ваше email">
          <input type="phone" v-model="phone" placeholder="Телефон">
          <!-- <input type="time" v-model="time" placeholder="time"> -->

          <button type="button" @click="sendata()">Купить</button>
  
  
      </form>
  
  </div>
</div>  
</template>

<style>

.body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  
}

/* Стили для контейнера заказа */
.data {
    max-width: 700px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
}

/* Стили для корзины товаров */
.basket {
    margin-bottom: 20px;
}

.iten {
    display: flex;
    align-items: center;
    justify-content: space-between; /* Добавляем выравнивание между элементами */
    margin-bottom: 10px;
    padding: 10px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 3px;
    background-color: #f9f9f9;
}

.iten img {
    max-width: 80px;
    margin-right: 10px;
}

.pric {
    display: flex;
    flex-direction: column;
}

.pric h3 {
    font-size: 18px;
    margin-right: 10px;
}

.pric span {
    font-size: 16px;
}

button {
    background-color: #e74c3c;
    color: white;
    border: none;
    border-radius: 3px;
    padding: 5px 10px;
    cursor: pointer;
}

button:hover {
    background-color: #c0392b;
}

/* Стили для формы заказа */
form {
    display: flex;
    flex-direction: column;
}

input {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

button[type="button"] {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 3px;
    padding: 10px;
    cursor: pointer;
}

button[type="button"]:hover {
    background-color: #2980b9;
}

.error {
    color: #e74c3c;
    margin-bottom: 10px;
}
</style>