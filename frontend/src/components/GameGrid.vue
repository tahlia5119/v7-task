<template>
    <div class="game-grid">
      <div v-for="(row, rowIndex) in grid" :key="rowIndex" class="grid-row">
        <GridCell
          v-for="(cell, colIndex) in row"
          :key="colIndex"
          :number="cell"
        />
      </div>
    </div>
  </template>

<script>
    import GridCell from './GridCell.vue';

    export default {
        name: "GameGrid",
        components: {
            GridCell,
        },
        props: {
            grid: {
                type: Array,
            },
        },
    }
</script>

<style scoped>
    .game-grid {
      display: flex;
      flex-direction: column;
      padding: 2px 0px;
      align-items: center;
    }

    .grid-row {
      display: flex;
    }
</style>
