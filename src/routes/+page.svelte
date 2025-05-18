<script>
	import {
		PUBLIC_N8N_PROD_URL,
		PUBLIC_N8N_TEST_URL,
		PUBLIC_N8N_USER,
		PUBLIC_N8N_PASS
	} from '$env/static/public';
	import Tile from '$lib/Tile.svelte';
	import triggerRefresh from '$lib/refresh.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Calendar } from '$lib/components/ui/calendar/index.js';
	import { getLocalTimeZone, today } from '@internationalized/date';
	import * as Table from '$lib/components/ui/table/index.js';
	import { onMount } from 'svelte';
	import { dev } from '$app/environment';

	let value = $state(today(getLocalTimeZone()));
	let jsonData = $state(null); // Store for the JSON response
	let isLoading = $state(false);

	const sheetsRequest = new Request(
		dev ? PUBLIC_N8N_TEST_URL : PUBLIC_N8N_PROD_URL,
		{
			method: 'POST',
			headers: {
				Authorization: 'Basic ' + btoa(`${PUBLIC_N8N_USER}:${PUBLIC_N8N_PASS}`),
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				action: 'getSheetsData',
				options: {
					// grading || assignments
					sheet: 'assignments',
					pageName: 'Teacher',
					range: 'A6:J50',
					includeHeaders: true
				}
			})
		}
	);

	async function getSheetsData() {
		isLoading = true;
		try {
			const response = await fetch(sheetsRequest);
			const data = await response.json();
			jsonData = data; // Store the data
			console.log('Sheets data:', jsonData);
			return data;
		} catch (error) {
			console.error('Failed to get sheet data:', error);
			return null;
		} finally {
			isLoading = false;
		}
	}

	let students = [
		'Joel',
		'James',
		'Ellie',
		'Chris',
		'Breanna',
		'Josh',
		'Kimberly',
		'Layla'
	];

	let jobs = [
		'Boys Bathroom',
		'Girls Bathroom',
		'Hall/Pad',
		'Trash/Boards',
		'Floor',
		'Sports/Table',
		'library',
		'Neatness'
	];

	async function refreshData() {
		console.log('Data refresh clicked');
		await getSheetsData();
	}

	const sleepSeconds = 500;

	onMount(() => {
		const interval = setInterval(() => {
			console.log(`sleeping for ${sleepSeconds} s`);
			getSheetsData();
		}, sleepSeconds * 1000);

		// Cleanup on component destroy
		return () => clearInterval(interval);
	});
</script>

<div class="grid grid-cols-[250px_1fr_1fr] gap-5 p-5">
	<!-- First, let's add the JSON display at the top -->
	<div class="col-span-3">
		<Tile>
			<div class="mb-2 flex items-center justify-between">
				<h4 class="scroll-m-20 text-xl font-semibold tracking-tight">
					JSON Response Preview
				</h4>
				<Button variant="outline" onclick={refreshData} disabled={isLoading}>
					{#if isLoading}
						Refreshing...
					{:else}
						Refresh Data
					{/if}
				</Button>
			</div>
			<pre class="max-h-60 overflow-x-auto rounded-md bg-gray-100 p-4 text-sm">
				{#if jsonData}
					{JSON.stringify(jsonData, null, 2)
						.split('\n')
						.slice(0, 20)
						.join('\n')}
				{:else if isLoading}
					Loading data...
				{:else}
					No data available
				{/if}
			</pre>
		</Tile>
	</div>

	<!-- <div class="flex flex-row justify-between"> -->
	<div></div>
	<!-- <Tile> -->
	<!-- <h4>{value}</h4> -->
	<!-- </Tile> -->
	<Tile>
		<h1
			class="scroll-m-20 p-5 text-4xl font-extrabold tracking-tight lg:text-5xl"
		>
			Class 3 TRCS
		</h1>
	</Tile>
	<!-- <Tile> -->
	<div class="my-auto ml-auto p-5">
		<Button on:click={triggerRefresh}>Refresh Display</Button>
	</div>
	<!-- </Tile> -->
	<!-- </div> -->
	<!-- <div> -->
	<Tile><Calendar type="single" bind:value class="rounded-md border" /></Tile>
	<Tile>
		<div class="w-full text-left">
			<h4 class="scroll-m-20 text-center text-xl font-semibold tracking-tight">
				Jobs
			</h4>
			<ul class="list-none p-0">
				{#each students as student}
					<li class="py-1">{student}</li>
				{/each}
			</ul>
		</div>
	</Tile>
	<div></div>
	<Tile>
		<Table.Root>
			<Table.Header>
				<Table.Row>
					<Table.Head class="">Job</Table.Head>
					<Table.Head class="text-right">Student</Table.Head>
				</Table.Row>
			</Table.Header>
			<Table.Body>
				{#each jobs as job, i}
					<Table.Row>
						<Table.Cell class="font-medium">{jobs[i]}</Table.Cell>
						<Table.Cell class="overflow-visible text-center">
							{#if jobs[i] == 'Sports/Table'}
								<div class="h-full w-full scale-125 rounded bg-red-500">
									{students[i]}
								</div>
							{:else}
								{students[i]}
							{/if}
						</Table.Cell>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>
	</Tile>
	<!-- </div> -->
</div>
