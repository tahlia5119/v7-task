<template>
  <div class="game">
    <GameGrid :grid="grid"></GameGrid>
  </div>
</template>

<script>
import GameGrid from './GameGrid.vue';
export default {
  name: 'GamePage',
  components: {
    GameGrid,
  },
  props: ['gridSize', 'blocks'],
  data() {
    return {
      grid: [[0,1,2],[4,8,2048],[8096, -1, 2]],
    };
  },
  methods: {
    // startNewGame() {
    //   if (this.localSize > 0 && this.localBlocks >= 0) {
    //     this.$router.push({ path: '/game', query: { gridSize: this.localSize, blocks: this.localBlocks } });
    //   } else {
    //     alert('Please enter valid values for size and blocks.');
    //   }
    // },
  },
};
</script>

<style scoped>
.game {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}
</style>
