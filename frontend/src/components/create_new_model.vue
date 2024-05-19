<template>
  <div class="form-container">
    <form @submit.prevent="submitForm" class="model-form">
      <div class="form-row">
        <div class="form-column">
          <select v-model="selectedUsername" class="form-input" :class="{'input-error': !selectedUsername}">
            <option disabled value="">Seleccione un usuario</option>
            <option v-for="user in usernames" :key="user.username" :value="user.username">{{ user.username }}</option>
          </select>
        </div>
        <div class="form-column">
          <input type="text" v-model.trim="name" placeholder="Nombre completo" class="form-input" :class="{'input-error': !name}">
        </div>
      </div>

      <div class="form-row">
        <div class="form-column">
          <input type="email" v-model.trim="email" placeholder="Correo electrónico" class="form-input" :class="{'input-error': !email}">
        </div>
        <div class="form-column">
          <input type="tel" v-model.trim="phone" placeholder="Teléfono" class="form-input" :class="{'input-error': !phone}">
        </div>
      </div>

      <div class="form-row">
        <div class="form-column">
          <select v-model="typeAccount" class="form-input" :class="{'input-error': !typeAccount}">
            <option disabled value="">Seleccione tipo de cuenta</option>
            <option value="Nequi">Nequi</option>
            <option value="Ahorro a la mano">Ahorro a la mano</option>
            <option value="Ahorros Bancolombia">Ahorros Bancolombia</option>
          </select>
        </div>
        <div class="form-column">
          <input type="text" v-model.trim="numberAccount" placeholder="Número de cuenta" class="form-input" :class="{'input-error': !numberAccount}">
        </div>
      </div>

      <div class="form-row">
        <div class="form-column">
          <input type="number" v-model.number="connectionHours" placeholder="Horas de conexión diarias" min="0" step="0.1" class="form-input" :class="{'input-error': !connectionHours}">
        </div>
      </div>

      <div class="form-row">
        <div class="form-column">
          <button type="submit" class="form-button">Crear Modelo</button>
        </div>
        <div class="form-column">
          <button type="button" @click="goBack" class="form-button back-button">Atrás</button>
        </div>
      </div>
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
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

:root {
  --primary-color: #4CAF50;
  --secondary-color: #f44336;
  --background-color: #f5f5f5;
  --input-border: #ccc;
  --input-focus-border: #4CAF50;
  --input-error-border: #f44336;
  --button-hover-opacity: 0.8;
  --box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  --border-radius: 8px;
}

body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  background-color: var(--background-color);
}

.form-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: white;
  box-shadow: var(--box-shadow);
  border-radius: var(--border-radius);
  width: 90%;
}

.model-form {
  display: flex;
  flex-direction: column;
}

.form-row {
  display: flex;
  justify-content: space-between;
}

.form-column {
  width: 48%;
}

.form-input {
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid var(--input-border);
  border-radius: var(--border-radius);
  transition: border-color 0.3s;
}

.form-input:focus {
  border-color: var(--input-focus-border);
  outline: none;
}

.input-error {
  border-color: var(--input-error-border);
}

.form-button, .back-button {
  padding: 12px;
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  margin-top: 10px;
  font-size: 16px;
  transition: opacity 0.3s;
  width: 100%;
}

.form-button {
  background-color: var(--primary-color);
  color: white;
}

.back-button {
  background-color: var(--secondary-color);
  color: white;
}

.form-button:hover, .back-button:hover {
  opacity: var(--button-hover-opacity);
}

/* Responsividad */
@media (max-width: 600px) {
  .form-container {
    width: 100%;
    padding: 10px;
    box-shadow: none;
  }

  .form-row {
    flex-direction: column;
  }

  .form-column {
    width: 100%;
  }

  .form-input, .form-button, .back-button {
    padding: 10px;
  }
}
</style>
