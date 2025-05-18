<script>
	import { Calendar as CalendarPrimitive } from 'bits-ui';
	import { cn } from '$lib/utils.js';

	let { ref = $bindable(null), class: className, ...restProps } = $props();
</script>

<CalendarPrimitive.Heading bind:ref class={cn('font-large text-xl', className)} {...restProps} />
