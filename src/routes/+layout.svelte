<script>
	import '../app.pcss';

	let { children } = $props();
	let time = new Date();
	let hours = time.getHours();
	let minutes = time.getMinutes();
	let todayMins = hours * 60 + minutes;
	let starttime = 650;
	let endtime = 720;
</script>

<div class="gradient-flow m-0 h-screen w-full p-0">
	{@render children?.()}
	{#if todayMins >= starttime && todayMins <= endtime}
		<div
			class="fire-gradient absolute bottom-0 left-0 right-0 h-[35px] w-full bg-red-500 text-center text-white"
		>
			Food should be cooking: {endtime - todayMins} mins remaining
		</div>
	{/if}
</div>

<style>
	@keyframes gradientFlow {
		0% {
			background-position: 0% 50%;
		}
		50% {
			background-position: 100% 50%;
		}
		100% {
			background-position: 0% 50%;
		}
	}

	.gradient-flow {
		background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
		background-size: 400% 400%;
		animation: gradientFlow 15s ease infinite;
		font-family:
			-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu,
			Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
</style>
