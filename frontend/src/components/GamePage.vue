<template>
  <div class="game">
    <button @click="resetGame" class="button">Reset to Defaults?</button>
    <div class="input">
      <label for="numberOfBlocks">Number of blocks:</label>
      <input v-model="blocksInput" type="number" id="numberOfBlocks" />
    </div>
    <div class="input">
      <label for="gridSize">Grid Size:</label>
      <input v-model="gridSizeInput" type="number" id="gridSize" />
    </div>
    <button @click="updateGrid" class="button">Generate New Grid</button>
    <div class="grid">
      <GameGrid :grid="currentGrid"></GameGrid>
    </div>
    <div v-if="state === 'game_won'" class="win-message">
      <span>YOU WON! Can you keep going?</span>
    </div>
  </div>
</template>

<script>
import GameGrid from './GameGrid.vue';
export default {
  name: 'GamePage',
  components: {
    GameGrid,
  },
  data() {
    return {
      state: "running",
      gridSize: 4,
      blocks: 0,
      blocksInput: 0,
      gridSizeInput: 4,
      currentGrid: [],
      action: "new_game",
      error: "",
      wonHidden: true,
    };
  },
  methods: {
    async fetchData(gridSize = 4, blocks = 0) {
      try {
        const response = await fetch("http://localhost:8000/game", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            grid: this.currentGrid,
            size: gridSize,
            blocks: blocks,
            action: this.action,
          }),
        });

        const data = await response.json();
        if (!response.ok) {
          if (data.detail) {
            alert(data.detail);
          }
          return;
        }
        this.currentGrid = data.grid;
        this.state = data.state;

        if (this.state === "game_won") {
          console.log("YOU WON! KEEP GOING!");
        } else if (this.state === "game_over") {
          alert("GAME OVER.");
        }
        
      } catch (error) {
        console.error(error);
        alert("Something went wrong :(");
      }
    },
    handleKeyPress: function (e) {
      // ideally we'd also be able to use arrow keys but they currently only control
      // the scroll bar and I can't be bothered right now to figure that out
      const key = String(e.key);
      switch (key) {
        case "a":
          this.action = "left";
          break;
        case "w":
          this.action = "up";
          break;
        case "d":
          this.action = "right";
          break;
        case "s":
          this.action = "down";
          break;
        // ignore any other key events
        default:
          return;
      }
      this.fetchData(this.gridSize, this.blocks);
    },
    resetGame() {
      this.action = "new_game";
      this.gridSizeInput = 4;
      this.blocksInput = 0;
      this.fetchData();
    },
    updateGrid() {
      this.action = "new_game";
      this.fetchData(this.gridSizeInput, this.blocksInput);
    },
  },
  // event listener for keyboard events to update the grid
  mounted: function() {
    this.fetchData();
    window.addEventListener("keypress", this.handleKeyPress)
  },
};
</script>

<style scoped>
.game {
  display: flex;
  flex-direction: column;
  height: 100vh;
  align-items: center;
}
.input {
  margin: 5px 0;
  display: flex;
  align-items: center;
}
.button {
  width: 200px;
}

.input label {
  text-align: left;
  width: 130px;
}

.input input {
  width: 100px;
  text-align: center;
}

.grid {
  padding: 10px 0;
  width: 100%;
}

.win-message{
  padding: 10px 0;
  font-size: 30px;
}
</style>
