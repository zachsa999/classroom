<script>
	import { Calendar as CalendarPrimitive } from "bits-ui";
	import { cn } from "$lib/utils.js";

	let { ref = $bindable(null), class: className, ...restProps } = $props();
</script>

<CalendarPrimitive.HeadCell
	bind:ref
	class={cn("text-muted-foreground w-8 rounded-md text-[0.8rem] font-normal", className)}
	{...restProps}
/>
