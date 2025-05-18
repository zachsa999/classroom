<script>
	let { children } = $props();
</script>

<div>
	{@render children?.()}
</div>

<style>
	div {
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: whitesmoke;
		border-radius: 10px;
		padding: 10px;
		/* margin: 10px; */
	}
</style>
