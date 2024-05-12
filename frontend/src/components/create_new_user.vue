<template>
    <div class="form-container">
      <form @submit.prevent="createUser" class="user-form">
        <h2>Crear Usuario</h2>
        <div class="form-field">
          <input id="username" v-model="newUser.username" type="text" placeholder="Usuario" required>
        </div>
        <div class="form-field">
          <input id="password" v-model="newUser.password" type="password" placeholder="Contraseña" required>
        </div>
        <div class="form-field">
          <input id="confirmPassword" v-model="confirmPassword" type="password" placeholder="Confirmar Contraseña" required>
        </div>
        <div class="form-field">
          <select id="role" v-model="newUser.rol" required>
            <option value="">Seleccione un rol</option>
            <option value="Administrador">Administrador</option>
            <option value="Monitor">Monitor</option>
            <option value="Modelo">Modelo</option>
          </select>
        </div>
        <div class="form-field checkbox">
          <label for="isActive" class="checkbox-label">
            <input id="isActive" type="checkbox" v-model="newUser.is_active">
            Activo
          </label>
        </div>
        <transition name="submit-button" :key="buttonKey">
        <button type="submit" class="submit-button" :disabled="isLoading">Crear Usuario</button>
        </transition>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </template>

  
  
  
<script>
/* eslint no-unused-vars: "off" */
export default {
  data() {
    return {
      newUser: {
        username: '',
        password: '',
        rol: '',
        is_active: false
      },
      confirmPassword: '',
      error: '',
      isLoading: false
    };
  },
  mounted() {
    // Esto fuerza la re-renderización del botón, activando la animación
    this.buttonKey++;
  },
  methods: {
    async createUser() {
      if (this.newUser.password !== this.confirmPassword) {
        this.error = 'Las contraseñas no coinciden.';
        return;
      }
      if (this.newUser.password.length < 8) {
        this.error = 'La contraseña debe tener al menos 8 caracteres.';
        return;
      }
      this.isLoading = true;
      try {
        await this.checkUserExists();
        const payload = {
          username: this.newUser.username,
          hashed_password: this.newUser.password,
          rol: this.newUser.rol,
          is_active: this.newUser.is_active
        };
        await this.$http.post('http://192.168.1.172:8080/api/create_new_user', payload);
        alert('Usuario creado exitosamente');
        this.resetForm();
      } catch (error) {
        this.error = error.message || 'Error al crear el usuario: Algo salió mal.';
      }
      this.isLoading = false;
    },
    async checkUserExists() {
      try {
        await this.$http.get(`http://192.168.1.172:8080/api/user_id?users=${this.newUser.username}`);
        throw new Error('El nombre de usuario ya está en uso. Por favor, elija otro nombre de usuario.');
      } catch (error) {
        if (error.response && error.response.data && error.response.data.detail === "Username not found") {
          return; // El usuario no existe, continúa con la creación
        }
        throw error;
      }
    },
    resetForm() {
      this.newUser = { username: '', password: '', rol: '', is_active: false };
      this.confirmPassword = '';
      this.error = '';
    }
  }
};
</script>

<style>
.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('~@/assets/v1016-b-09.jpg');
  background-size: cover; /* Cubre todo el contenedor */
  background-position: center;
}

.user-form {
  padding: 20px;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 300px;
}

.form-field {
    display: flex;
    justify-content: center;  /* Alinea los elementos horizontalmente al centro */
    align-items: center;      /* Alinea los elementos verticalmente al centro */
    margin-bottom: 20px;
}

input[type="text"], input[type="password"], select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

input[type="checkbox"] {
  margin-right: 5px;
}

.checkbox-label {
  display: flex;
  align-items: center;
}
.submit-button {
    color: white;
    background-color: #007bff; /* Color principal del botón */
    border: none; /* Eliminar el borde si no es necesario */
    border-radius: 20px; /* Bordes redondeados */
    padding: 18px 36px;
    display: inline-block;
    font-family: "Lucida Console", Monaco, monospace;
    font-size: 14px;
    letter-spacing: 1px;
    cursor: pointer;
    box-shadow: inset 0 0 0 0 #D80286;
    -webkit-transition: ease-out 0.4s;
    -moz-transition: ease-out 0.4s;
    transition: ease-out 0.4s;
}

.submit-button:hover {
  background-color: #0056b3;
  box-shadow: inset 400px 0 0 0 #D80286;    
}
.submit-button-enter, .submit-button-enter-active, .submit-button-enter-to {
    transition: transform 0.4s ease-out;
  }
  
  .submit-button-enter {
    transform: translateX(-100%); /* Inicia fuera de la vista */
  }
  
  .submit-button-enter-to {
    transform: translateX(0); /* Termina en la posición normal */
  }

.error-message {
  color: red;
  text-align: center;
}
.submit-button-enter-active {
    
    transform: translateX(0);
  }
</style>
