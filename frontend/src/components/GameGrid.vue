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
                required: true,
            },
        },
    }
</script>

<style scoped>
    .game-grid {
      display: flex;
      flex-direction: column;
      border-style: solid;
      border-width: 2px;
      border-radius: 10px;
      padding: 2px;
    }

    .grid-row {
      display: flex;
    }
</style>
