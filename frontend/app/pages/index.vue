<script setup lang="ts">
const { data: usuarios, execute } = await useFetch<User[]>(
  "http://localhost:8000/api/usuarios/"
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
</script>

<template>
  <div>
    <div style="justify-content: center; display: flex">
      <h1 class="font-bold text-5xl text-blue-950">Lista de usuarios</h1>
    </div>
    <div style="padding: 20px; align-items: center">
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
          <TableRow>
            <TableCell class="font-medium">
              <h1 v-for="usuario in usuarios">{{ usuario.id }}</h1>
            </TableCell>
            <TableCell>
              <h1 v-for="usuario in usuarios">{{ usuario.nombre }}</h1>
            </TableCell>
            <TableCell>
              <h1 v-for="usuario in usuarios">{{ usuario.edad }}</h1>
            </TableCell>
            <TableCell>
              <h1 v-for="usuario in usuarios">{{ usuario.email }}</h1>
            </TableCell>
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
      </div>
    </div>
  </div>
</template>
