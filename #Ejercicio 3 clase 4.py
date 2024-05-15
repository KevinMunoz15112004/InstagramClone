#Ejercicio 3 clase 4

print("-----Instagram-----")
user = input("Ingrese su nombre de usuario, # Teléfono o email: ")
password = input("Ingrese su clave")

if user == "Pepito" and password =="123":
    print(f"Welcome {user}")
    print("Loading your posts")
else:
    print("Tu usuario o contraseña no están correctos")

print("Registrate para conectarte al mundo")
input("Iniciar sesión con Facebook")
facebook = input("Si o No")
if facebook == "Si":
    print("Bienvenido")
else:
    mobile = input("Correo o # Telefono: ")
    name = input("Ingrese su nombre: ")
    username = input("Username: ")
    password = input("Ingrese su clave: ")