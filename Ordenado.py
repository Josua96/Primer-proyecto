def menu():
    print("*******************************************************************************")        
    print ( "                             TEC Digital")
    print ()
    print()
    print("    Menú Principal")
    print ()
    print("    1.Iniciar Sesión ")
    print ()
    print("    2.Registrarse ")
    print()
    accion=int(input("    ¿Qué proceso desea ejecutar? "))
    print()
    print()
    print("*******************************************************************************")
    if accion==1:
        login()
    elif accion==2:
        registro()
    else:
        print("Error intente de nuevo")
        menu()

menu()

def login():
    print ("                   Ingrese los datos solicitados")
    print ()
    print ("    Digite su identificación de usuario")
    ced=int(input())
    print()
    print("     Dígite su contraseña")
    contra=int(input(  ))
    estudiantes_profesores=[{"Nombre":"Vera Gamboa","Correo":"vgamboa@itcr.ac.cr","Pasw":4039,"Id":205140324,"Tipo":"Prof"},{"Nombre":"Carlos Castro Pereira",
                "Correo":"ccastro@itcr.ac.cr","Pasw":4029,"Id":302000234,"Tipo":"Prof"},{"Nombre":"Joaquín Vargas García","Correo":"jvargas@itcr.ac.cr","Pasw":4019,
                "Id":401000423,"Tipo":"Prof"},{"Nombre":"José Moreno Torres","Correo":"josemoreno@itcr.ac.cr","Pasw": 4009,"Id":206400342,"Tipo":"Prof"},
                {"Nombre":"Alberto Ruiz Perez","Correo":"alberto@gmail.com","Contraseña":1123,"Carnet":2016123456,"Tipo":"Est"},
              {"Nombre":"Alfredo Castilla Lopez","Correo":"alfredo@gmail.com","Contraseña":1456,"Carnet":2016223456,"Tipo":"Est"},
              {"Nombre":"Antonio Umaña Medina","Correo":"anto@gmail.com","Contraseña":1567,"Carnet":2016323456,"Tipo":"Est"},
              {"Nombre":"Ariel Rodriguez Jesus","Correo":"ariel@gmail.com","Contraseña":1678,"Carnet":2016423456,"Tipo":"Est"},
              {"Nombre":"Benito Acosta Sousa","Correo":"benito@gmail.com","Contraseña":1789,"Carnet":2016523456,"Tipo":"Est"},
              {"Nombre":"Berta Bermudez Calderon","Correo":"berta@gmail.com","Contraseña":1910,"Carnet":2016623456,"Tipo":"Est"},
              {"Nombre":"Brenda Ferrer Ortiz","Correo":"brenda@gmail.com","Contraseña":1101,"Carnet":2016723456,"Tipo":"Est"},
              {"Nombre":"Magaly Rojas Rojas","Correo":"magaly@gmail.com","Contraseña":1102,"Carnet":2016823456,"Tipo":"Est"},
              {"Nombre":"Hilary Bustamandte Ureña","Correo":"hilary@gmail.com","Contraseña":1103,"Carnet":2016923456,"Tipo":"Est"},
              {"Nombre":"Margara Aagon Romero","Correo":"margar@gmail.com","Contraseña":1104,"Carnet":2016101234,"Tipo":"Est"},
              {"Nombre":"Joshua Carranza Perez","Correo":"joshua@gmail.com","Contraseña":1105,"Carnet":2016111234,"Tipo":"Est"},
              {"Nombre":"Kervin Sibaja Rodriguez","Correo":"kervin@gmail.com","Contraseña":1106,"Carnet":2016121234,"Tipo":"Est"},
              {"Nombre":"Angelo Guerrero Medina","Correo":"angelo@gmail.com","Contraseña":1107,"Carnet":2016131234,"Tipo":"Est"},
              {"Nombre":"Andy Herrera Herrera","Correo":"andy@gmail.com","Contraseña":1108,"Carnet":2016141234,"Tipo":"Est"},
              {"Nombre":"Carlos Baez Miranza","Correo":"carlos@gmail.com","Contraseña":1109,"Carnet":2016151234,"Tipo":"Est"},
              {"Nombre":"Luis Murrillo Barrios","Correo":"luis@gmail.com","Contraseña":1110,"Carnet":2016161234,"Tipo":"Est"},
              {"Nombre":"Andrey Carranza Perez","Correo":"andrey@gmail.com","Contraseña":1111,"Carnet":2016171234,"Tipo":"Est"},
              {"Nombre":"Ana Gonzalez Gonzalez","Correo":"ana@gmail.com","Contraseña":1112,"Carnet":2016181234,"Tipo":"Est"},
              {"Nombre":"Ericka Bello Mendoza","Correo":"ericka@gmail.com","Contraseña":1113,"Carnet":2016191234,"Tipo":"Est"},
              {"Nombre":"Rabael Ortega Ortega","Correo":"rafael@gmail.com","Contraseña":1114,"Carnet":2016201234,"Tipo":"Est"},
              {"Nombre":"Pedro Pedroza Perez","Correo":"pedro@gmail.com","Contraseña":1115,"Carnet":2016211234,"Tipo":"Est"}]

    for x in estudiantes_profesores:
        if((x["Id"]==ced)and(x["Pasw"]==contra)):
            print(x["Nombre"]) 
            return
    print("Identificación o contraseña incorrectos, intente de nuevo")
    login()

def registro():
        print ("Dígite su nombre")

def menuprofesor(a):
    print("*******************************************************************************")
    print (                                   "Entorno de profesores")
    print()
    print ("Bienvenido(@)",a)
    
def menuestudiante():
    print("*******************************************************************************")
    print("Hola")
