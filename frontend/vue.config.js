const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
      proxy: {
          '/api': {
              target: 'http://localhost:8000', // Asegúrate de que el puerto coincida con el de tu backend FastAPI
              changeOrigin: true,
              pathRewrite: { '^/api': '' },
          },
      }
  }
};