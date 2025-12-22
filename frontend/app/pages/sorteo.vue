<script setup lang="ts">
import * as z from "zod";
import { toTypedSchema } from "@vee-validate/zod";
import { useForm, Field as VeeField } from "vee-validate";
import { toast } from "vue-sonner";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Field,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import {
  InputGroup,
  InputGroupAddon,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group";
import { Route, Router } from "lucide-vue-next";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

const { data: usuariorandom } = await useFetch<User>(
  "http://localhost:8000/api/usuarios/random"
);
</script>

<!-- <template>
  <div>srote xd</div>

  <h1 v-if="usuariorandom">{{ usuariorandom.nombre }}</h1>
  <h1 v-if="usuariorandom">{{ usuariorandom.email }}</h1>
</template> -->
<template>
  <!-- <NuxtImg src="/background.png" alt="image" width="1920" height="1080" /> -->
  <div
    class="min-h-screen bg-cover bg-center bg-no-repeat"
    style="background-image: url('/background.png')"
  >
    <div class="flex justify-center">
      <h1 class="font-bold text-5xl text-blue-950 mt-20">SORTEO</h1>
    </div>

    <!-- FORMULARIO -->

    <div class="flex justify-center mt-20">
      <!-- <form @submit="onSubmit"> -->
      <Card class="w-full sm:max-w-md">
        <CardHeader>
          <CardTitle> El ganador del sorteo es: </CardTitle>
        </CardHeader>
        <CardContent>
          <FieldGroup>
            <VeeField v-slot="{ field, errors }" name="nombre">
              <Field :data-invalid="!!errors.length">
                <FieldLabel for="form-vee-demo-title">
                  <h1 v-if="usuariorandom">
                    Nombre completo: {{ usuariorandom.nombre }}
                  </h1>
                </FieldLabel>
                <FieldError v-if="errors.length" :errors="errors" />
              </Field>
            </VeeField>

            <VeeField v-slot="{ field, errors }" name="edad">
              <Field :data-invalid="!!errors.length">
                <h1 v-if="usuariorandom">Edad: {{ usuariorandom.edad }}</h1>
                <FieldError v-if="errors.length" :errors="errors" />
              </Field>
            </VeeField>

            <VeeField v-slot="{ field, errors }" name="email">
              <Field :data-invalid="!!errors.length">
                <h1 v-if="usuariorandom">Correo: {{ usuariorandom.email }}</h1>
                <FieldError v-if="errors.length" :errors="errors" />
              </Field>
            </VeeField>
          </FieldGroup>
        </CardContent>

        <div class="flex justify-center">
          <CardFooter>
            <Field orientation="horizontal">
              <Button to="main" type="button" variant="outline">
                Volver
              </Button>

              <!--  -->
              <!--  -->
            </Field>
          </CardFooter>
        </div>
      </Card>
      <!-- </form> -->
    </div>

    <!-- END FORMULARIO -->
  </div>
</template>
