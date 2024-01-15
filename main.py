from paquete1 import Cliente

# Crear un objeto Cliente como ejemplo
cliente1 = Cliente("Julia", "Sandoval", "jsandoval@email.com", "123456789", "Sandy", "12345")

# Usar métodos de la clase Cliente: se quita el comentario de acuerdo al método que se quiera probar

# Probar el método registro de usuario
#resultado = cliente1.registro_usuario()
#print(resultado) 

# Probar el método verificar contraseña
#cliente1.verificar_contrasena()

# Probar el método mostrar usuarios, es necesario ejecutar el método registro de usuarios primero
#cliente1.mostrar_usuarios()

# Probar el método obtener nombre completo
#print(cliente1.obtener_nombre_completo())  

# Probar el método obtener contactos
print(cliente1.obtener_contacto())  

# Probar el método cambiar mail
#cliente1.cambiar_email()

