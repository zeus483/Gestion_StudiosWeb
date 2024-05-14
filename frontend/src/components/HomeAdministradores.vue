<template>
  <div class="admin-panel">   
    <aside class="sidebar">
      <h1 class="welcome-title">Dulce Lujuria</h1>
      <input type="text" placeholder="Search a model" class="search-box">
      <button class="sidebar-button" @click="goToCreateUser">Create New User</button>
      <button class="sidebar-button" @click="goToCreateModel">Create New Model</button>
      <button class="sidebar-button" @click="goToGoals">Model Goals</button>
      <button class="sidebar-button">Daily Register</button>
      <button class="sidebar-button">button off</button>
      <button class="sidebar-button">button off</button>
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
        <p>Hours: <span>{{ topModel.hours }}</span></p>
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
    },
    goToCreateModel(){
      this.$router.push('/create-model');
    },
    goToGoals(){
      this.$router.push("/model-goals")
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

:root {
  --primary-color: #6200ee;
  --secondary-color: #03dac6;
  --background-color: #f5f5f5;
  --text-color: #333;
  --sidebar-bg: #ffffff;
  --button-bg: #f7f7f7;
  --button-hover-bg: #e2e2e2;
  --border-color: #ccc;
  --header-bg: #6200ee;
  --header-text: white;
  --content-bg: #f9f9f9;
  --box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

* {
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  background-color: var(--background-color);
  color: var(--text-color);
}

.admin-panel {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: var(--sidebar-bg);
  padding: 20px;
  box-shadow: var(--box-shadow);
}

.welcome-title {
  font-size: 24px;
  color: var(--text-color);
  margin-bottom: 20px;
}

.sidebar-button {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background-color: var(--button-bg);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 16px;
}

.sidebar-button:hover {
  background-color: var(--button-hover-bg);
}

.search-box {
  padding: 8px;
  margin-bottom: 20px;
  width: calc(100% - 16px);
  border: 1px solid var(--border-color);
  border-radius: 8px;
}

.content {
  flex-grow: 1;
  padding: 20px;
  background-color: var(--content-bg);
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  background-color: var(--header-bg);
  padding: 10px;
  border-radius: 8px;
  color: var(--header-text);
}

.model-details {
  border: 1px solid var(--border-color);
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  box-shadow: var(--box-shadow);
}

.model-details h2 {
  margin-top: 0;
  color: var(--text-color);
}

/* Responsividad */
@media (max-width: 768px) {
  .admin-panel {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    padding: 10px;
  }

  .content {
    padding: 10px;
  }

  .header {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
