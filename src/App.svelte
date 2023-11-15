<script lang="ts">
function getRandomInt(min:number, max:number) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

	import {test, type vocab} from "./result";
    let list: vocab[] = []
    let output = test
    let lengths = output.length
    let randomNumber = getRandomInt(0,lengths-1)
    let reveal = false
    function random(){
        reveal = false
        randomNumber = getRandomInt(0,lengths-1)
    }
    function revealButton(){
        reveal = true
    }
    let higher = true
    let lower = true
    $: {
        output = test
        lengths = output.length
        randomNumber = getRandomInt(0,lengths-1)
    }
    function hard(){
        list.push(test[randomNumber])
        list = list
        random()
    }
    function easy(){
        random()
    }
</script>
<main>
<!-- Higher <input type="checkbox" name="" id="" bind:checked={higher}>
<br>
Lower<input type="checkbox" name="" id="" bind:checked={lower}>
<br> -->
<span class="number">{list.length}</span>
<br>
<span>Topic title: {output[randomNumber]["topic_name"]} <br> Theme: {output[randomNumber]["theme"]}</span>
<br>
{#if reveal == true}
{output[randomNumber]["french"]}
{/if}
<br>
{output[randomNumber]["english"]}
<br>
{#if reveal == false}
    <button on:click={revealButton}>reveal</button>
{:else}
    <button on:click={easy}>Easy</button>
    <button on:click={hard}>Hard</button>
{/if}
<table class="TableEnglish">
    <tr>
        <th>English</th>
        <th>French</th>
    </tr>
{#each list as a}
    <tr>
        <td>{a["english"]}</td>
        <td>{a["french"]}</td>
    </tr>
{/each}
</table>
</main>

<style>
    .TableEnglish {
        overflow-y: scroll;
        height: 50vh;
    }
</style>