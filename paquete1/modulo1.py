class Cliente:
    base_de_datos = {}

    def __init__(self, nombre, apellido, email, telefono, nombre_usuario, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    # Método de registro de usuarios
    def registro_usuario(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        telefono = input("Ingrese su teléfono: ")
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña: ")

        self.base_de_datos[nombre_usuario] = (contrasena, nombre, apellido, email, telefono)
        return "Usuario registrado exitosamente."

    # Método para verificar si la contraseña coincide con el usuario
    def verificar_contrasena(self):
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña: ")
    
        if nombre_usuario in self.base_de_datos:
            contraseña_guardada, *_ = self.base_de_datos[nombre_usuario]
            if contraseña_guardada == contrasena:
                print("Contraseña correcta.")
                return
        print("Usuario o contraseña incorrectos.")

    # Método para mostrar todos los usuarios registrados
    def mostrar_usuarios(self):
        print("Nombres de usuario registrados:")
        for usuario in self.base_de_datos.keys():
            print(usuario)

    # Método para obtener nombre completo del cliente
    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    # Método para obtener datos de los contactos
    def obtener_contacto(self):
        return f"Los datos del usuario son: Nombre completo: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"

    # Método para cambiar el dato de email
    def cambiar_email(self, nuevo_email):
        self.email = nuevo_email

    def __str__(self):
        return f"Cliente: {self.obtener_nombre_completo()}"
