<template>
    <div class="admin-panel">   
      <aside class="sidebar">
        <h1 class = "welcome">Hello word</h1>
        <input type="text" placeholder="search a model" class="search-box">
        <button class="sidebar-button" @click="goToCreateUser">Create new user</button>
        <button class="sidebar-button">Create new Model</button>
        <button class="sidebar-button">Resumen 15na</button>
        <button class="sidebar-button">Metas Modelos</button>
        <button class="sidebar-button">Finanzas</button>
      </aside>
      <section class="content">
        <header class="header">
          <h1>Dulce Lujuria</h1>
          <input type="text" placeholder="Search..." class="search-box">
        </header>
        <div class="model-details">
          <h2>Top Model</h2>
          <p>Tokens: <span>{{ topModel.tokens }}</span></p>
          <p>Followers: <span>{{ topModel.followers }}</span></p>
          <p>Hour: <span>{{ topModel.hours }}</span></p>
        </div>
      </section>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        topModel: {
          tokens: 'name_model_top_tokens',
          followers: 'name_model_top_followers',
          hours: 'name_model_top_hours'
        }
      };
    },
    methods: {
      goToCreateUser() {
        this.$router.push('/create-user'); // Utiliza el nombre de la ruta o el path
      }
    }
  }
  
  </script>
<style>
.welcome {
    display: flex;
    flex-direction: column;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    background-color: white;
}
.admin-panel {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 200px;
  background-color: #f0f0f0;
  padding: 20px;
}

.sidebar-button {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #fff;
  border: 1px solid #ddd;
  cursor: pointer;
}

.sidebar-button:hover {
  background-color: #e9e9e9;
}

.search-box {
  padding: 8px;
  margin-bottom: 20px;
  width: calc(100% - 16px);
  box-sizing: border-box;
}

.content {
  flex-grow: 1;
  padding: 20px;
  background-color: #fff;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.model-details {
  border: 1px solid #ccc;
  padding: 20px;
}

.model-details h2 {
  margin-top: 0;
}
</style>
    