<template>
  <div class="login-container">
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="login" class="login-form">
      <div class="input-group">
        <input type="text" id="username" v-model="credentials.username" placeholder="Nombre de Usuario" required>
      </div>
      <div class="input-group">
        <input type="password" id="password" v-model="credentials.password" placeholder="Contraseña" required>
      </div>
      <button type="submit" class="login-button">Iniciar Sesión</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      credentials: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    async login() {
  try {
    const response = await this.$http.post('http://192.168.1.172:8080/api/login', this.credentials);
    console.log('Login successful:', response.data);

    if (response.data.access) {
      // Guarda la información del usuario en el almacenamiento local
      localStorage.setItem('user_info', JSON.stringify(response.data.user_info));
      this.$store.dispatch('fetchUser', response.data.user_info); // Esta línea es opcional, dependiendo si quieres manejar el estado con Vuex

      // Redirige según el rol del usuario
      switch(response.data.user_info.role) {
        case 'Administrador':
          this.$router.push('/admin');
          break;
        case 'Modelo':
          this.$router.push('/modelo'); // Asegúrate de que esta es la ruta correcta para el rol 'Modelo'
          break;
        default:
          this.$router.push('/home');
          break;
      }
    } else {
      throw new Error('Access denied');
    }
  } catch (error) {
    console.error('Login failed:', error);
    alert('Inicio de sesión fallido: ' + error.message);
  }
}

  }
};
</script>


<style>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.login-form {
  display: flex;
  flex-direction: column;
  width: 300px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  background-color: white;
}

.input-group {
  display: flex;
  justify-content: center;  /* Alinea los elementos horizontalmente al centro */
  align-items: center;      /* Alinea los elementos verticalmente al centro */
  margin-bottom: 20px;
}


input {
  width: 100%;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 16px;
}

input:focus {
  border-color: #0056b3;
  outline: none;
}

.login-button {
  padding: 10px;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.login-button:hover {
  background-color: #0056b3;
}
</style>
