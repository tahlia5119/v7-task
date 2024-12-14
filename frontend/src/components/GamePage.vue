<template>
  <div class="game">
    <div class="grid">
      <div v-for="row in 6" :key="row" class="row">
        <div v-for="col in 6" :key="col" class="cell"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GamePage',
};
</script>

<style scoped>
.game {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.grid {
  display: grid;
  grid-template-columns: repeat(6, 50px);
  grid-template-rows: repeat(6, 50px);
  gap: 5px;
}
.cell {
  width: 50px;
  height: 50px;
  background-color: lightgray;
  border: 1px solid black;
}
</style>