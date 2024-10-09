<script>
    import { Button, Modal } from 'flowbite-svelte';
    import { ExclamationCircleOutline } from 'flowbite-svelte-icons';
	import { createEventDispatcher } from 'svelte';
    export let open = false;
    const dispatch=createEventDispatcher();

</script>
  
<Modal bind:open={open} size="xs" autoclose outsideclose>
    <div class="text-center">
        <ExclamationCircleOutline class="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200" />
        <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400"><slot>Are you sure to do this?</slot></h3>
        <Button color="red" class="me-2" on:click={()=>dispatch('close')}>Yes, I'm sure</Button>
        <Button color="alternative">No, cancel</Button>
    </div>
</Modal>

  