<script lang="ts">
function getRandomInt(min:number, max:number) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

	import {test} from "./result";
    let output = test
    let lengths = output.length
    let randomNumber = getRandomInt(0,lengths-1)
    let reveal = false
    function random(){
        reveal = false
        randomNumber = getRandomInt(0,lengths-1)
    }
    let higher = true
    let lower = true
    $: {
        output = test.filter(t => t.higher == higher ).filter(t => t.foundation == lower)
        lengths = output.length
        randomNumber = getRandomInt(0,lengths-1)
    }
</script>

<main>
Higher <input type="checkbox" name="" id="" bind:checked={higher}>
<br>
Lower<input type="checkbox" name="" id="" bind:checked={lower}>
<br>
{#if reveal == true}
{output[randomNumber]["french"]}
{/if}
<br>
{output[randomNumber]["english"]}
<br>
<button on:click={()=> reveal = true}>reveal</button>
<button on:click={random}>random</button>
</main>
