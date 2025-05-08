<script>
	import { PI_IP, REFRESH_TOKEN } from '$env/dynamic/private';
	import Tile from '$lib/Tile.svelte';
	import triggerRefresh from '$lib/refresh.js';
</script>

<div class="gradient-flow layout">
	<Tile>
		<h1>{new Date().toLocaleString()}</h1>
	</Tile>
	<Tile>
		<button class="refresh-button" on:click={triggerRefresh}>Refresh Display</button>
	</Tile>
</div>

<style>
	.layout {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		grid-template-rows: 1fr 1fr 1fr;
	}

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
		margin: 0;
		padding: 0;
		height: 100vh;

		background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
		background-size: 400% 400%;
		animation: gradientFlow 15s ease infinite;
		font-family:
			-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans',
			'Helvetica Neue', sans-serif;
	}
	.message {
		font-size: 4rem;
		color: #333;
		text-align: center;
		padding: 2rem;
		background-color: white;
		border-radius: 1rem;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		margin-bottom: 2rem;
	}

	.refresh-button {
		padding: 1rem 2rem;
		font-size: 1.2rem;
		background-color: #4caf50;
		color: white;
		border: none;
		border-radius: 0.5rem;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	.refresh-button:hover {
		background-color: #45a049;
	}

	.refresh-button:disabled {
		background-color: #cccccc;
		cursor: not-allowed;
	}

	.status {
		margin-top: 1rem;
		font-size: 1rem;
		color: #666;
	}
</style>
