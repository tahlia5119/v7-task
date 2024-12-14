<template>
    <div class="cell" :style="{ backgroundColor: getBackgroundColor }">
        <div class="number">
            <span>{{ this.number }}</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: "GridCell",
        props: {
            number: Number
        },
        computed: {
            getBackgroundColor () {
                // select colour based on value like the og game
                // there's probably a better way to  do this I'm sure
                const colourMap = {
                    "2": "#ffccff",
                    "4": "#ffb3ff",
                    "8": "#ff99ff",
                    "16": "#ff80ff",
                    "32": "#ff66ff",
                    "64": "#ff4dff",
                    "128": "#ff33ff",
                    "256": "#ff1aff",
                    "512": "#ff00ff",
                    "1024": "#e600e6",
                    "2048": "#cc00cc",
                };
                // grade the colours up to 2048, after that it's a constant colour
                if (this.number > 0 && Object.keys(colourMap).indexOf(String(this.number)) > -1) {
                    return colourMap[String(this.number)];
                } else if (this.number > 2048) {
                    return "#b300b3";
                } else if (this.number == -1) {
                    return "black"; // to match `-1` text as the blocking cell
                }
                return "#ffe6ff";
            }
        },
    };
</script>

<style scoped>
    .cell {
        width: 70px;
        height: 70px;
        border-radius: 14px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 1px;
        border-radius: 14px;
        border-style: solid;
        border-width: 1px;
    }
    .number {
        color: black;
    }
    span {
        display: inline-block;
        vertical-align: middle;
        line-height: normal;
    }
</style>