import os

LIBROS_FILE =  'libros.csv'
PRESTAMO_FILE = 'prestamo.csv'
USUARIOS_FILE = 'usuarios.csv'


def crear_archivos ():
    
    if not os.path.exists("libros.csv"):
        with open("libros.csv", "w", encoding="utf-8") as f:
            f.write("id,titulo,categoria,anio,stock\n")
            f.write("1,Cien años de soledad,Gabriel García Márquez,Novela,1967,7\n")
            f.write("2,El amor en los tiempos del cólera,Gabriel García Márquez,Novela,1985,5\n")
            f.write("3,La hojarasca,Gabriel García Márquez,Novela,1955,4\n")
            f.write("4,Rayuela,Julio Cortázar,Novela,1963,6\n")
            f.write("5,Pedro Páramo,Juan Rulfo,Novela,1955,3\n")
            f.write("6,El origen de las especies,Charles Darwin,Ciencia,1859,2\n")
            f.write("7,Una breve historia del tiempo,Stephen Hawking,Ciencia,1988,4\n")
            f.write("8,Introducción a la Filosofía,José Ferrater Mora,Filosofía,1960,5\n")
            f.write("9,Crítica de la razón pura,Immanuel Kant,Filosofía,1781,1\n")
            f.write("10,El arte de la guerra,Sun Tzu,Estrategia,500,6\n")


    if not os.path.exists("usuario.csv"):
        with open("usuario.csv", "w", encoding="utf-8") as f:
            f.write("id,nombre,email\n")
            f.write("1,Ana,ana@email.com\n")
            f.write("2,Carlos,carlos@email.com\n")
            f.write("3,Laura,laura@email.com\n")
  
    if not os.path.exists("prestamo.csv"):
        with open("prestamo.csv", "w", encoding="utf-8") as f:
            f.write("libro_id,titulo,total_prestamo\n")
            f.write("1,1,2,1,2024-03-01\n")
            f.write("2,2,1,2,2024-03-02\n")
            f.write("3,2,2,1,2024-03-10\n")



            
def ordenar_libro():
    with open("libros.csv", "r", encoding="utf-8") as f:
    lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
        if not lines:
            print("libros.csv vacío o no existe.")
            return

        header = lines[0]                      
        data_lines = lines[1:]                 

        libros = [] 
        for line in data_lines:
            parts = [p.strip() for p in line.split(",")]
            pid = parts[0] if len(parts) > 0 else ""
            titulo = parts[1] if len(parts) > 1 else ""
            categoria = parts[2] if len(parts) > 2 else ""
            
            try:
                año = int(parts[3]) if len(parts) > 3 else 0
            except:
                año = 0
            try:
                stock = int(parts[4]) if len(parts) > 4 else 0
            except:
                stock = 0
            libros.append([pid, nombre, categoria, año, stock])


#                           AGREGAR CLIENTE 

def agregar_cliente ():
    usuario = []
    if os.path.exists("usuario.csv"):
        with open("usuario.csv", "r", encoding="utf-8") as f:
            lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
        if lines:
            for line in lines[1:]:
                parts = [p.strip() for p in line.split(",")]
                usuario.append(parts)  

    max_id = 0
    for c in usuario:
        try:
            cid = int(c[0])
            if cid > max_id:
                max_id = cid
        except:
            pass
    nuevo_id = max_id + 1

    nombre = input("Ingrese nombre del nuevo usuario : ").strip()
    email = input("Ingrese email del nuevo usuario: ").strip()

   
    if not os.path.exists("usuario.csv"):
        with open("usuario.csv", "w", encoding="utf-8") as f:
            f.write("id,nombre,email\n")
    with open("usuario.csv", "a", encoding="utf-8") as f:
        f.write(",".join([str(nuevo_id), nombre, email]) + "\n")

    print(f"\nUsuario agregado con id {nuevo_id}: {nombre} - {email}\n")



#                    CALCULAR TOTAL DE PRESTAMO

def total_prestamo_libros ():
    libro_por_id = {}
    prestamo_por_id = {}
    if not os.path.exists("libros.csv"):
        print("libros.csv no existe.")
        return
    with open("libros.csv", "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(lines) < 2:
        print("libros.csv sin datos.")
        return
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        pid = parts[0] if len(parts) > 0 else ""
        nombre = parts[1] if len(parts) > 1 else ""
        




#                       VER USUARIOS CON PRESTAMO 


def ver_usuario_():
    
    usuarios = []
    if not os.path.exists("usuario.csv"):
        print("usuario.csv no existe.")
        return
    with open("usuario.csv", "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(lines) < 2:
        print("usuarios.csv sin datos.")
        return
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        usuarios.append(parts)

     usuario_prestamo= set()
    if not os.path.exists("prestamo.csv"):
        print("prestamo.csv no existe.")
        return
    with open("prestamo.csv", "r", encoding="utf-8") as f:
        plines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(plines) >= 2:
        for line in plines[1:]:
            parts = [p.strip() for p in line.split(",")]
            cid = parts[1] if len(parts) > 1 else ""
            if cid:
                usuario_prestamo.add(cid)


#                               MENU PPRINCIPAL

def menu():
    clientes = cargar_clientes()
    pedidos = cargar_pedidos()

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. listar libros de menor a mayor")
        print("2. agregar un nuevo usuario")
        print("3. calcular total de prestamo por libro")
        print("4. ver usuarios que han registrado prestamo ")
        print("5. SALIR ")


        opcion = input("Opción: ").strip()

        if opcion == '1':
           ordenar_libro()
        elif opcion == '2':
            agregar_cliente ()
        elif opcion == '3':
            total_prestamo_libros ()
        elif opcion == '4':
            ver_usuario_()
        elif opcion == '5':
         print ("Saliendo...")
    
        else:
            print("Opción inválida")
        
if __name__ == "__main__":
    menu()
 



