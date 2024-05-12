<template>
    <div class="form-container">
      <form @submit.prevent="submitForm" class="model-form">
        <select v-model="selectedUsername" class="form-input">
          <option disabled value="">Seleccione un usuario</option>
          <option v-for="user in usernames" :key="user.username" :value="user.username">{{ user.username }}</option>
        </select>
  
        <input type="text" v-model.trim="name" placeholder="Nombre completo" class="form-input">
        <input type="email" v-model.trim="email" placeholder="Correo electrónico" class="form-input">
        <input type="tel" v-model.trim="phone" placeholder="Teléfono" class="form-input">
        
        <select v-model="typeAccount" class="form-input">
          <option disabled value="">Seleccione tipo de cuenta</option>
          <option value="Nequi">Nequi</option>
          <option value="Ahorro a la mano">Ahorro a la mano</option>
          <option value="Ahorros Bancolombia">Ahorros Bancolombia</option>
        </select>
  
        <input type="text" v-model.trim="numberAccount" placeholder="Número de cuenta" class="form-input">
        <input type="number" v-model.number="connectionHours" placeholder="Horas de conexión diarias" min="0" step="0.1" class="form-input">
    
        <button type="submit" class="form-button">Crear Modelo</button>
        <button type="button" @click="goBack" class="form-button back-button">Atrás</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        usernames: [],
        selectedUsername: '',
        name: '',
        email: '',
        phone: '',
        typeAccount: '',
        numberAccount: '',
        connectionHours: null
      }
    },
    mounted() {
      this.fetchUsernames();
    },
    methods: {
      fetchUsernames() {
        axios.get('http://192.168.1.172:8080/api/active-models')
          .then(response => {
            this.usernames = response.data.filter(user => user.role === 'Modelo');
          })
          .catch(error => console.error('Error fetching usernames:', error));
      },
      submitForm() {
        const userData = {
          username: this.selectedUsername,
          name: this.name,
          email: this.email,
          phone: this.phone,
          type_account: this.typeAccount,
          number_account: this.numberAccount,
          connection_hours: this.connectionHours
        };
        axios.post('http://192.168.1.172:8080/api/createModel', userData)
        .then(response => {
          alert('Modelo creado con éxito');
          console.log(response);
          window.location.href = 'http://192.168.1.172:8080/admin';
          // Aquí puedes añadir cualquier acción post-creación, como redireccionar
        })
        .catch(error => {
          console.error('Hubo un error al crear el modelo:', error);
          alert('Error al crear el modelo');
        });
      },
      goBack() {
        window.location.href = 'http://192.168.1.172:8080/admin';
      }
    }
  }
  </script>
  
<style>
.form-container {   
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-image: none; 
  background-color: #f9f9f9;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  width: 90%;
}

.model-form {
  display: flex;
  flex-direction: column;
}

.form-input {
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-button, .back-button {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  width: 100%;
}

.form-button {
  background-color: #4CAF50;
  color: white;
}

.back-button {
  background-color: #f44336;
  color: white;
}

.form-button:hover, .back-button:hover {
  opacity: 0.8;
}

/* Responsividad */
@media (max-width: 600px) {
  .form-container {
    width: 100%;
    margin: 0;
    padding: 10px;
    box-shadow: none;
  }

  .form-input, .form-button, .back-button {
    padding: 10px;
  }
}
</style>