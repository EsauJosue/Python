opcion = int(input('Elije una opción 1,2,3: '))



def saludo(opcion):
    if opcion == 1:
        print ("""
            Hola, ¿cómo estás?
            Elegiste la opción 1
            Adiós 🙂
        """)
    elif opcion == 2:
         print ("""
            Hola, ¿cómo estás?
            Elegiste la opción 2
            Adiós 😇
        """)
    elif opcion ==3:
         print ("""
            Hola, ¿cómo estás?
            Elegiste la opción 3
            Adiós 😉
        """)
    else:
         print ("""
            Hola, no es una opción correcta 🤬
        """)

saludo(opcion)

