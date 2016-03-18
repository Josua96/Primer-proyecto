
def login():
    print ("                   Ingrese los datos solicitados")
    print ()
    print ("    Digite su identificación de usuario")
    cedula=int(input())
    print()
    print("     Dígite su contraseña")
    contraseña=int(input(  ))
    profesores=[{"Nombre":"Vera Gamboa","Correo":"vgamboa@itcr.ac.cr","Contraseña":4039,"Cedula":205140324},{"Nombre":"Carlos Castro Pereira",
                "Correo":"ccastro@itcr.ac.cr","Contraseña":4029,"cedula":302000234},{"Nombre":"Joaquín Vargas García","Correo":"jvargas@itcr.ac.cr","Contraseña":4019,
                "Cedula":401000423},{"Nombre":"José Moreno Torres","Correo":"josemoreno@itcr.ac.cr","Contraseña": 4009,"Cedula":206400342}]
    for i in profesores:
        if((i["Cedula"]==cedula) and (i["Contraseña"]==
def menu2(a):
    print("*******************************************************************************")
    print (                                   "Entorno de profesores")
    print()
    print ("Bienvenido(@)",a["Nombre"])
    
            
def registro():
        print ("Dígite su nombre")
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
            

    
