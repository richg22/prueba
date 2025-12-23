<script setup lang="ts">
const { data: usuarios, execute } = await useFetch<User[]>(
  "http://localhost:8000/api/usuarios/"
);

const { data: usuariospending } = await useFetch<UserPending[]>(
  "http://localhost:8000/api/usuariospending/"
);

import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const items = ref(["Seleccione", "Pendiente", "Verificado"]);
const value = ref("Seleccione");

const usuariosfiltrados = computed<User[] | UserPending[]>(() => {
  const usuariosList: User[] = usuarios.value ?? [];
  const pendingList: UserPending[] = usuariospending.value ?? [];

  if (value.value === "Pendiente") return pendingList;
  if (value.value === "Verificado") return usuariosList;
  return [];
});
</script>

<template>
  <div>
    <div class="flex justify-center">
      <h1 class="font-bold text-5xl text-blue-950 mt-10">Lista de usuarios</h1>
    </div>
    <USelect v-model="value" :items="items" />

    <div class="flex justify-center">
      <div class="mt-6 mr-7">
        <h1>Seleccione el tipo de usuario:</h1>
        <!-- <p>{{ usuariosfiltrados }}</p> -->
      </div>
      <select
        v-model="value"
        class="mt-4 w-56 rounded-md border border-slate-300 bg-white px-3 py-2 text-slate-900 shadow-sm"
      >
        <option v-for="item in items" :key="item" :value="item">
          {{ item }}
        </option>
      </select>
    </div>

    <div class="align-middle px-30">
      <Table>
        <TableCaption>Lista de usuarios</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead class="w-[100px]">ID</TableHead>
            <TableHead>NOMBRE</TableHead>
            <TableHead>EDAD</TableHead>
            <TableHead class="text-left"> CORREO </TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="usuario in usuariosfiltrados" :key="usuario.id">
            <TableCell> {{ usuario.id }} </TableCell>
            <TableCell> {{ usuario.nombre }} </TableCell>
            <TableCell> {{ usuario.edad }} </TableCell>
            <TableCell> {{ usuario.email }} </TableCell>
          </TableRow>
        </TableBody>
      </Table>
      <div style="display: flex; justify-content: center; margin-top: 20px">
        <div style="margin-right: 10px">
          <NuxtLink to="/main">
            <Button variant="destructive" size="lg" class="shadow"
              >Pagina Principal</Button
            >
          </NuxtLink>
        </div>
        <div style="margin-left: 10px">
          <NuxtLink to="">
            <Button
              variant="destructive"
              size="lg"
              class="shadow"
              @click="execute"
              >Actualizar</Button
            >
          </NuxtLink>
        </div>

        <div style="margin-left: 10px">
          <NuxtLink to="sorteo">
            <Button
              variant="destructive"
              size="lg"
              class="shadow"
              @click="execute"
              >Seleccionar ganador</Button
            >
          </NuxtLink>
        </div>

        <div></div>
      </div>
    </div>
  </div>
</template>
