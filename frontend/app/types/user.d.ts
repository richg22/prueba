interface User {
  id: number;
  nombre: string;
  edad: number;
  email: string;
  password: string;
}

interface UserPending {
  id: number;
  nombre: string;
  edad: number;
  email: string;
  token: number;
}
