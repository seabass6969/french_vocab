<script lang="ts">
      import Topbar from './Topbar.svelte';

	import { fly } from "svelte/transition";
	import StartNow from "./Components/StartNow.svelte";
	import Navbar from "./Components/Navbar.svelte";
	import { typewriter } from "./libs/animations";
	import { navbarOpen } from './libs/homeVariable';
    let clientWidth: number = 0
    let startnow = () => {}
</script>
<svelte:window bind:innerWidth={clientWidth} />
{#if $navbarOpen == true}
	<Navbar />
{/if}
	<div class="full">
		{#if clientWidth > 810}
			<Navbar />
		{/if}
		<main transition:fly={{ y: -200, duration: 400 }}>
            <Topbar/>
			<div class="maincontent">
			</div>
		</main>
	</div>
	<div class="backgroundblur">
		<StartNow on:click={startnow}/>
		<!-- <StartNow on:click={startnow}/> -->
	</div>
<style lang="scss">
</style>
