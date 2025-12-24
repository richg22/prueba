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

const formSchema = toTypedSchema(
  z.object({
    password: z
      .string()
      .min(5, "Ingrese contraseña valida")
      .max(20, "Ingrese contraseña valida"),
    email: z
      .string()
      .min(10, "Correo debe tener minimo 10 caracteres")
      .max(100, "Corre debe tener maximo 100 caracteres"),
  })
);

const { handleSubmit, resetForm } = useForm({
  validationSchema: formSchema,
  initialValues: {
    password: "",
    email: "",
  },
});

type TokenPair = {
  access: string;
  refresh: string;
};

const onSubmit = handleSubmit(async (data) => {
  try {
    const tokens = await $fetch<TokenPair>(
      "http://localhost:8000/api/auth/token/",
      {
        method: "POST",
        body: {
          email: data.email,
          password: data.password,
        },
      }
    );

    localStorage.setItem("access", tokens.access);
    localStorage.setItem("refresh", tokens.refresh);

    toast("Login exitoso", {
      description: "Sesión iniciada correctamente",
    });

    await navigateTo("/main");
  } catch (error) {
    toast("Error al iniciar sesión", {
      description: "Correo o contraseña incorrectos",
    });
  }
});
//https://www.shadcn-vue.com/docs/forms/vee-validate
</script>

<template>
  <!-- <NuxtImg src="/background.png" alt="image" width="1920" height="1080" /> -->
  <div
    class="min-h-screen bg-cover bg-center bg-no-repeat"
    style="background-image: url('/background.png')"
  >
    <div class="flex justify-center">
      <h1 class="font-bold text-5xl text-blue-950 mt-20">LOGIN</h1>
    </div>

    <!-- FORMULARIO -->

    <div class="flex justify-center mt-20">
      <!-- <form @submit="onSubmit"> -->
      <Card class="w-full sm:max-w-md">
        <CardContent>
          <form id="form-vee-demo" @submit="onSubmit">
            <FieldGroup>
              <VeeField v-slot="{ field, errors }" name="email">
                <Field :data-invalid="!!errors.length">
                  <FieldLabel for="form-vee-demo-title"> Correo </FieldLabel>
                  <Input
                    id="form-vee-demo-title"
                    type="email"
                    v-bind="field"
                    placeholder="Ingresa tu correo"
                    autocomplete="off"
                    :aria-invalid="!!errors.length"
                  />
                  <FieldError v-if="errors.length" :errors="errors" />
                </Field>
              </VeeField>

              <VeeField v-slot="{ field, errors }" name="password">
                <Field :data-invalid="!!errors.length">
                  <FieldLabel for="form-vee-demo-title">
                    Contraseña
                  </FieldLabel>
                  <Input
                    type="password"
                    id="form-vee-demo-title"
                    v-bind="field"
                    placeholder="Ingresa tu contraseña "
                    autocomplete="off"
                    :aria-invalid="!!errors.length"
                  />
                  <FieldError v-if="errors.length" :errors="errors" />
                </Field>
              </VeeField>
            </FieldGroup>
          </form>
        </CardContent>

        <div class="flex justify-center">
          <CardFooter>
            <Field orientation="horizontal">
              <Button type="button" variant="outline" @click="resetForm">
                Borrar campos
              </Button>
              <Button type="submit" form="form-vee-demo"> Login</Button>
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
