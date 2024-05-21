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
      <div class="api-accounts">
        <h2>Chaturbate Models</h2>
        <div v-for="account in apiAccounts" :key="account.username" class="account-info">
          <span :class="{'online-dot': account.time_online !== -1, 'offline-dot': account.time_online === -1}"></span>
          <span>{{ account.username }}</span>
          <span>Tokens: {{ account.token_balance }}</span>
          <span>Followers: {{ account.num_followers }}</span>
        </div>
        <div class="total-tokens">
          <h3>Total Tokens: {{ totalTokens }}</h3>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      topModel: {
        tokens: 'name_model_top_tokens',
        followers: 'name_model_top_followers',
        hours: 'name_model_top_hours'
      },
      apiAccounts: [],
      totalTokens: 0
    };
  },
  mounted() {
    this.fetchApiAccounts();
    this.interval = setInterval(this.fetchApiAccounts, 150000); // Actualiza cada 150,000 milisegundos (2.5 minutos)
  },
  beforeUnmount() {
    clearInterval(this.interval);
  },
  methods: {
    goToCreateUser() {
      this.$router.push('/create-user');
    },
    goToCreateModel(){
      this.$router.push('/create-model');
    },
    goToGoals(){
      this.$router.push("/model-goals");
    },
    fetchApiAccounts() {
      axios.get('http://192.168.1.172:8080/api/accounts')
        .then(response => {
          const accountsWithApiToken = response.data.filter(account => account.api_token);
          const accountRequests = accountsWithApiToken.map(account => 
            axios.get(`http://192.168.1.172:8080/api/proxy?url=${encodeURIComponent(account.api_token)}`)
              .then(res => ({ ...res.data, api_token: account.api_token }))
          );
          Promise.all(accountRequests)
            .then(apiAccountsData => {
              this.apiAccounts = apiAccountsData;
              this.totalTokens = apiAccountsData.reduce((sum, account) => sum + account.token_balance, 0);
            })
            .catch(error => console.error('Error fetching API accounts:', error));
        })
        .catch(error => console.error('Error fetching accounts:', error));
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

.model-details, .api-accounts {
  border: 1px solid var(--border-color);
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  box-shadow: var(--box-shadow);
  margin-bottom: 20px;
}

.model-details h2, .api-accounts h2 {
  margin-top: 0;
  color: var(--text-color);
}

.account-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid var(--border-color);
}

.account-info:last-child {
  border-bottom: none;
}

.online-dot {
  width: 10px;
  height: 10px;
  background-color: #39ff14; /* Verde neón */
  border-radius: 50%;
  display: inline-block;
  margin-right: 10px;
}

.offline-dot {
  width: 10px;
  height: 10px;
  background-color: gray;
  border-radius: 50%;
  display: inline-block;
  margin-right: 10px;
}

.total-tokens {
  margin-top: 20px;
  font-weight: bold;
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
