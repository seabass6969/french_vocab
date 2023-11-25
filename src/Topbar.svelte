<script lang="ts">
	import { fly } from "svelte/transition";
	import StartNow from "./Components/StartNow.svelte";
	import Navbar from "./Components/Navbar.svelte";
	import { typewriter } from "./libs/animations";
	import Menubtn from "./Components/home/menubtn.svelte";
	import { emojiText, timeText } from "./libs/Timeutil";
	import { navbarOpen } from "./libs/homeVariable";
    let clientWidth: number = 0
    let startnow = () => {}
</script>

			<div class="topbar">
				<div class="topset">
					{#if clientWidth < 810}
						<Menubtn
							on:click={() => {
								navbarOpen.set(true)
							}}
						/>
						<img src="/favicon.svg" alt="" class="logo" />
						<div>
							<span class="title">Saullingo</span>
						</div>
					{/if}
				</div>
				<!-- <span class="streak">Day streak: {dayStreak}</span> -->
				<span class="welcome" 
					><span in:typewriter={{speed:0.9}}>Welcome! {timeText()}</span> <img src={emojiText()} alt="" class="welcomeemoji" />
					</span
				>
			</div>

<style lang="scss">
</style>

