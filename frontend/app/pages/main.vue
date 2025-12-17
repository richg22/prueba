<script setup lang="ts">

import * as z from 'zod'
import { toTypedSchema } from '@vee-validate/zod'
import { useForm, Field as VeeField } from 'vee-validate'
import { toast } from 'vue-sonner'
import { Button } from '@/components/ui/button'


const formSchema = z.object({
  title: z
    .string()
    .min(5, 'Bug title must be at least 5 characters.')
    .max(32, 'Bug title must be at most 32 characters.'),
  description: z
    .string()
    .min(20, 'Description must be at least 20 characters.')
    .max(100, 'Description must be at most 100 characters.'),
})

 const { handleSubmit } = useForm({
   validationSchema: toTypedSchema(formSchema),
   initialValues: {
     title: '',
     description: '',
   },
})

const onSubmit = handleSubmit((values) => {
  // Do something with the form values.
  console.log(values)
})

//https://www.shadcn-vue.com/docs/forms/vee-validate
</script>
 


<template>
<!-- <NuxtImg src="/background.png" alt="image" width="1920" height="1080" /> -->
 <div class="min-h-screen bg-cover bg-center bg-no-repeat" style="background-image: url('/background.png')">

    <div class="flex justify-center mt10">
      <h1 class="font-bold text-5xl text-blue-950 mt-40">Pagina principal ❤</h1>
    </div>

   <form @submit="onSubmit">
    <!-- Build the form here -->
  </form>
  </div>
  
</template>
