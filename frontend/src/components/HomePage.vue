<template>
    <div class="home">
      <h1>Play game?</h1>
      <button @click="startNewGame">New Game</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage',
    methods: {
      startNewGame() {
        this.$router.push('/game');
      },
    },
  };
  </script>
  
  <style scoped>
  .home {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    text-align: center;
  }
  button {
    margin-top: 10px;
    padding: 10px 20px;
    font-size: 16px;
  }
</style>