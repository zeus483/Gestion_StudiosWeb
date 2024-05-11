<template>
  <div class="admin-panel">   
    <aside class="sidebar">
      <h1 class="welcome-title">Hello word</h1>
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
      this.$router.push('/create-user');
    }
  }
}
</script>

<style>
.welcome-title {
  font-size: 24px;
  color: #333;
}

.admin-panel {
  display: flex;
  height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.sidebar {
  width: 250px;
  background-color: #ffffff;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.sidebar-button {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #f7f7f7;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.sidebar-button:hover {
  background-color: #e2e2e2;
}

.search-box {
  padding: 8px;
  margin-bottom: 20px;
  width: calc(100% - 16px);
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.content {
  flex-grow: 1;
  padding: 20px;
  background-color: #f9f9f9;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.model-details {
  border: 1px solid #ddd;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
}

.model-details h2 {
  margin-top: 0;
  color: #333;
}
</style>
