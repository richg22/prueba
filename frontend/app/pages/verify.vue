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
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

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

const formSchema = toTypedSchema(
  z.object({
    nombre: z
      .string()
      .min(10, "Nombre debe tener minimo 10 caracteres")
      .max(100, "Nombre debe tener maximo 100 caracteres."),
    edad: z
      .number()
      .gt(0, "Ingrese una edad validad")
      .lte(99, "Ingese una edad validad"),
    email: z
      .string()
      .min(10, "Correo debe tener minimo 10 caracteres")
      .max(100, "Corre debe tener maximo 100 caracteres"),
  })
);

const { handleSubmit, resetForm } = useForm({
  validationSchema: formSchema,
  initialValues: {
    nombre: "",
    edad: 0,
    email: "",
  },
});

const onSubmit = handleSubmit((data) => {
  toast("You submitted the following values:", {
    description: h(
      "pre",
      {
        class:
          "bg-code text-code-foreground mt-2 w-[320px] overflow-x-auto rounded-md p-4",
      },
      h("code", JSON.stringify(data, null, 2))
    ),
    position: "bottom-right",
    class: "flex flex-col gap-2",
    style: {
      "--border-radius": "calc(var(--radius)  + 4px)",
    },
  });
  const { data: usuarios } = useFetch<User[]>(
    "http://localhost:8000/api/usuarios/",
    {
      method: "POST",
      body: { nombre: data.nombre, edad: data.edad, email: data.email },
    }
  );
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
      <h1 class="font-bold text-5xl text-blue-950 mt-20">
        Crea tu nueva contraseña
      </h1>
    </div>

    <!-- FORMULARIO -->

    <div class="flex justify-center mt-20">
      <!-- <form @submit="onSubmit"> -->
      <Card class="w-full sm:max-w-md">
        <CardHeader>
          <CardTitle> Hola {NOMBRE} </CardTitle>
          <CardDescription>
            Crea tu contraseña para finalizar con el registro
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form id="form-vee-demo" @submit="onSubmit">
            <FieldGroup>
              <VeeField v-slot="{ field, errors }" name="nombre">
                <Field :data-invalid="!!errors.length">
                  <FieldLabel for="form-vee-demo-title">
                    Contraseña
                  </FieldLabel>
                  <Input
                    id="form-vee-demo-title"
                    v-bind="field"
                    placeholder="Ingresa tu contraseña "
                    autocomplete="off"
                    :aria-invalid="!!errors.length"
                  />
                  <FieldError v-if="errors.length" :errors="errors" />
                </Field>
              </VeeField>

              <VeeField v-slot="{ field, errors }" name="nombre">
                <Field :data-invalid="!!errors.length">
                  <FieldLabel for="form-vee-demo-title">
                    Repite Contraseña
                  </FieldLabel>
                  <Input
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

              <!-- alert -->
              <AlertDialog>
                <AlertDialogTrigger as-child>
                  <Button> Show Dialog </Button>
                </AlertDialogTrigger>
                <AlertDialogContent>
                  <AlertDialogHeader>
                    <AlertDialogTitle
                      >Are you absolutely sure?</AlertDialogTitle
                    >
                    <AlertDialogDescription>
                      This action cannot be undone. This will permanently delete
                      your account and remove your data from our servers.
                    </AlertDialogDescription>
                  </AlertDialogHeader>
                  <AlertDialogFooter>
                    <AlertDialogCancel>Cancel</AlertDialogCancel>
                    <AlertDialogAction>Continue</AlertDialogAction>
                  </AlertDialogFooter>
                </AlertDialogContent>
              </AlertDialog>

              <!--end alert  -->
            </Field>
          </CardFooter>
        </div>
      </Card>
      <!-- </form> -->
    </div>

    <!-- END FORMULARIO -->
  </div>
  <!-- END DIV DE FONDO DE PANTALLA -->
</template>
