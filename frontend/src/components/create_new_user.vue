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
        <button type="submit" class="submit-button">Crear Usuario</button>
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
        error: ''
      };
    },
    methods: {
        async createUser() {
    try {
        // Verifica si el usuario ya existe
        await this.checkUserExists();
        // Si no existe, envía la solicitud para crear un nuevo usuario
        const payload = {
            username: this.newUser.username,
            hashed_password: this.newUser.password,
            rol: this.newUser.rol,
            is_active: this.newUser.is_active
        };
        await this.$http.post('http://localhost:8080/api/create_new_user', payload);
        alert('Usuario creado exitosamente');
        this.resetForm();
    } catch (error) {
        // Maneja errores específicos y genéricos
        this.error = error.message || 'Error al crear el usuario: Algo salió mal.';
    }
}
,
            async checkUserExists() {
    try {
        // Realiza una petición GET al servidor para verificar si el usuario existe
        await this.$http.get(`http://localhost:8080/api/user_id?users=${this.newUser.username}`);
        // Si la petición es exitosa y el usuario existe, lanza un error indicando que el usuario ya existe
        throw new Error('El nombre de usuario ya está en uso. Por favor, elija otro nombre de usuario.');
    } catch (error) {
        // Si el error es específicamente porque el usuario no fue encontrado, permite continuar con la creación
        if (error.response && error.response.data && error.response.data.detail === "Username not found") {
            return; // El usuario no existe, continúa con la creación
        }
        // Si es otro tipo de error, lánzalo nuevamente
        throw error;
    }
},

      resetForm() {
        this.newUser.username = '';
        this.newUser.password = '';
        this.newUser.rol = '';
        this.newUser.is_active = false;
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
  background-color: #f4f4f4;
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
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 4px;
  color: white;
  background-color: #007bff;
  cursor: pointer;
  font-size: 16px;
}

.submit-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  text-align: center;
}
</style>
