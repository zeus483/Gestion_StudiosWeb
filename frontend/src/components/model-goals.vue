<template>
    <div class="container">
        <div class="search-section">
            <h2>Search Model</h2>
            <div class="form-group">
                <label for="name-model">Name model:</label>
                <input type="text" id="name-model" class="form-field" v-model="modelName" @input="debounceFetchModelInfo" autocomplete="off"/>
                <ul v-if="showFilteredModels">
                    <li v-for="model in filteredModelsComputed" :key="model.id" @click="selectModel(model)">
                        {{ model.username }}
                    </li>
                </ul>
            </div>
            <div class="form-group">
                <label for="actual-goal">Actual goal:</label>
                <input type="text" id="actual-goal" class="form-field" v-model="actualGoal" disabled/>
            </div>
            <div class="form-group">
                <label for="new-goal">New goal:</label>
                <input type="text" id="new-goal" class="form-field" v-model="newGoal" />
            </div>
            <button class="btn primary" @click="setNewGoal">Set new goal</button>
            <button class="btn secondary" @click="goBack">Back</button>
        </div>
        <div class="table-section">
            <table>
                <thead>
                    <tr>
                        <th>Models</th>
                        <th>Goal</th>
                        <th>Actual Tokens</th>
                        <th>Tokens Faltantes</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="model in models" :key="model.id">
                        <td>{{ model.username }}</td>
                        <td>{{ model.token_goal }}</td>
                        <td>{{ model.tokens_generated }}</td>
                        <td>{{ model.tokens_faltantes }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            modelName: "",
            actualGoal: "",
            newGoal: "",
            models: [],
            selectedModel: null,
            timeout: null,
            filteredModels: [],
        };
    },
    computed: {
        filteredModelsComputed() {
            if (this.modelName.length >= 3) {
                return this.models.filter(model => model.username.toLowerCase().includes(this.modelName.toLowerCase()));
            }
            return [];
        },
        showFilteredModels() {
            return this.filteredModelsComputed.length > 0 && this.modelName.length > 0 && !this.selectedModel;
        }
    },
    created() {
        this.fetchModels();
    },
    methods: {
        async fetchModels() {
            try {
                const response = await fetch("http://192.168.1.172:8080/api/models-and-goals");
                if (!response.ok) throw new Error('Failed to fetch models');
                this.models = await response.json();
                this.refreshAutocomplete();
            } catch (error) {
                console.error("Error fetching models:", error);
            }
        },
        selectModel(model) {
            this.selectedModel = model;
            this.actualGoal = model.token_goal;
            this.modelName = model.username;
            this.filteredModels = [];
        },
        async setNewGoal() {
            if (!this.newGoal) {
                alert("Please enter a valid goal");
                return;
            }
            if (this.selectedModel) {
                const url = `http://192.168.1.172:8080/api/update_model/${this.selectedModel.id}`;
                try {
                    const response = await fetch(url, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({ token_goal: parseInt(this.newGoal) }),
                    });
                    if (!response.ok) throw new Error('Failed to update goal');
                    alert("Goal updated successfully");
                    this.newGoal = ""; // Clear the input after successful update
                    this.selectedModel = null;
                    this.modelName = "";
                    this.fetchModels(); // Refetch models to refresh the list with updated goals
                } catch (error) {
                    console.error("Error updating goal:", error);
                    alert(error.message);
                }
            } else {
                alert("No model selected");
            }
        },
        refreshAutocomplete() {
            if (this.modelName.length >= 3) {
                this.filteredModels = this.models.filter(model => model.username.toLowerCase().includes(this.modelName.toLowerCase()));
            } else {
                this.filteredModels = [];
            }
        },
        goBack() {
            // Implement back button functionality here
            window.location.href = 'http://192.168.1.172:8080/admin';
        }
    },
    watch: {
        modelName() {
            this.refreshAutocomplete();
        }
    }
};
</script>

<style>
:root {
    --primary-color: #6200ee;
    --secondary-color: #03dac6;
    --background-color: #f5f5f5;
    --text-color: #333;
    --border-color: #e0e0e0;
    --hover-color: #3700b3;
    --table-header-bg: #6200ee;
    --table-row-bg: #f5f5f5;
    --table-row-hover-bg: #e0e0e0;
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

.container {
    display: flex;
    flex-direction: column;
    padding: 20px;
    gap: 20px;
}

.search-section {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 20px;
    background-color: white;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    align-items: center;
}

h2 {
    color: var(--primary-color);
    margin-bottom: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 100%;
}

.form-field {
    padding: 10px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    font-size: 16px;
    width: 100%;
    shape-margin: 20%
    ;
}

.table-section {
    display: flex;
    flex-direction: column;
    background-color: white;
    padding: 20px;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid var(--border-color);
    padding: 12px;
    text-align: left;
}

th {
    background-color: var(--table-header-bg);
    color: var(--table-header-text);
}

td {
    background-color: var(--table-row-bg);
}

tr:nth-child(even) td {
    background-color: white;
}

tr:hover td {
    background-color: var(--table-row-hover-bg);
}

button {
    margin-top: 10px;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button.primary {
    background-color: var(--primary-color);
    color: white;
}

button.primary:hover {
    background-color: var(--hover-color);
}

button.secondary {
    background-color: var(--secondary-color);
    color: white;
}

button.secondary:hover {
    background-color: var(--hover-color);
}

ul {
    list-style-type: none;
    padding: 0;
    margin-top: 0;
    background: white;
    position: absolute;
    width: 100%;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

li {
    padding: 8px 16px;
    cursor: pointer;
}

li:hover {
    background-color: var(--hover-color);
    color: white;
}

@media (min-width: 768px) {
    .container {
        flex-direction: row;
        justify-content: space-between;
        gap: 40px;
    }
    .search-section {
        flex: 1;
    }
    .table-section {
        flex: 2;
    }
}
</style>
