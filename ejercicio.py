
import os


def selection_sort_list_of_lists(arr, key_index, reverse=False):
    # arr: lista de listas (o tuplas). key_index: índice del elemento por el cual comparar.
    n = len(arr)
    for i in range(n - 1):
        sel = i
        for j in range(i + 1, n):
            a = arr[j][key_index]
            b = arr[sel][key_index]
            if reverse:
                if a > b:
                    sel = j
            else:
                if a < b:
                    sel = j
        if sel != i:
            arr[i], arr[sel] = arr[sel], arr[i]

def crear_archivos_ejemplo_si_faltan():
    # productos.csv
    if not os.path.exists("productos.csv"):
        with open("productos.csv", "w", encoding="utf-8") as f:
            f.write("id,nombre,categoria,precio,stock\n")
            f.write("1,Laptop,Electrónica,3000000,10\n")
            f.write("2,Mouse,Electrónica,50000,100\n")
            f.write("3,Zapatos Deportivos,Ropa,250000,20\n")
            f.write("4,Televisor,Electrónica,2200000,5\n")
            f.write("5,Camiseta,Ropa,60000,50\n")
    # clientes.csv
    if not os.path.exists("clientes.csv"):
        with open("clientes.csv", "w", encoding="utf-8") as f:
            f.write("id,nombre,email\n")
            f.write("1,Ana,ana@email.com\n")
            f.write("2,Carlos,carlos@email.com\n")
            f.write("3,Laura,laura@email.com\n")
    # pedidos.csv
    if not os.path.exists("pedidos.csv"):
        with open("pedidos.csv", "w", encoding="utf-8") as f:
            f.write("id,cliente_id,producto_id,cantidad,fecha\n")
            f.write("1,1,2,2,2024-03-01\n")
            f.write("2,2,1,2,2024-03-02\n")
            f.write("5,2,2,1,2024-03-10\n")


def opcion_1_ordenar_productos():
    # Abrir y leer todo el archivo tal como lo hace el profesor
    with open("productos.csv", "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if not lines:
        print("productos.csv vacío o no existe.")
        return

    header = lines[0]                      # línea de encabezado
    data_lines = lines[1:]                 # líneas de datos

    productos = []  # lista de listas: [id, nombre, categoria, precio(int), stock(int)]
    for line in data_lines:
        parts = [p.strip() for p in line.split(",")]
        pid = parts[0] if len(parts) > 0 else ""
        nombre = parts[1] if len(parts) > 1 else ""
        categoria = parts[2] if len(parts) > 2 else ""
        # precio hazlo entero par no tener error 
        try:
            precio = int(parts[3]) if len(parts) > 3 else 0
        except:
            precio = 0
        try:
            stock = int(parts[4]) if len(parts) > 4 else 0
        except:
            stock = 0
        productos.append([pid, nombre, categoria, precio, stock])

    """
    selection_sort_list_of_lists(productos, key_index=3, reverse=False)

    # mostrar resultado (similar al profesor)
    print("\nProductos ordenados por precio (menor -> mayor):")
    print("{:<3} {:<25} {:>12} {:>8}".format("id", "nombre", "precio", "stock"))
    for p in productos:
        print("{:<3} {:<25} {:>12} {:>8}".format(p[0], p[1], p[3], p[4]))

    # reescribir productos.csv con el nuevo orden (manteniendo el formato original)
    with open("productos.csv", "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for p in productos:
            line = ",".join([p[0], p[1], p[2], str(p[3]), str(p[4])])
            f.write(line + "\n")
    print("\nproductos.csv actualizado.\n")
    """

# -------------- Opción 2: Agregar nuevo cliente (id autoincremental) ------------
def opcion_2_agregar_cliente():

    clientes = []
    if os.path.exists("clientes.csv"):
        with open("clientes.csv", "r", encoding="utf-8") as f:
            lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
        if lines:
            for line in lines[1:]:
                parts = [p.strip() for p in line.split(",")]
                clientes.append(parts)  

    # calcular id autoincremental (mayor id + 1)
    max_id = 0
    for c in clientes:
        try:
            cid = int(c[0])
            if cid > max_id:
                max_id = cid
        except:
            pass
    nuevo_id = max_id + 1

    # pedir datos al usuario (como el profesor)
    nombre = input("Ingrese nombre del nuevo cliente: ").strip()
    email = input("Ingrese email del nuevo cliente: ").strip()

    # escribir (append) la nueva línea
    # si el archivo no existía, creamos el header antes
    if not os.path.exists("clientes.csv"):
        with open("clientes.csv", "w", encoding="utf-8") as f:
            f.write("id,nombre,email\n")
    with open("clientes.csv", "a", encoding="utf-8") as f:
        f.write(",".join([str(nuevo_id), nombre, email]) + "\n")

    print(f"\nCliente agregado con id {nuevo_id}: {nombre} - {email}\n")

# ---- Opción 3: Calcular total de ventas por producto y escribir total_ventas.csv ---
def opcion_3_total_ventas_por_producto():
    # 1) leer productos para obtener precio y nombre por id
    precio_por_id = {}
    nombre_por_id = {}
    if not os.path.exists("productos.csv"):
        print("productos.csv no existe.")
        return
    with open("productos.csv", "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(lines) < 2:
        print("productos.csv sin datos.")
        return
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        pid = parts[0] if len(parts) > 0 else ""
        nombre = parts[1] if len(parts) > 1 else ""
        try:
            precio = int(parts[3]) if len(parts) > 3 else 0
        except:
            precio = 0
        nombre_por_id[pid] = nombre
        precio_por_id[pid] = precio

    # 2) leer pedidos y acumular totales por producto_id
    totales = {}  # pid -> total dinero
    if not os.path.exists("pedidos.csv"):
        print("pedidos.csv no existe.")
        return
    with open("pedidos.csv", "r", encoding="utf-8") as f:
        plines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(plines) < 2:
        print("pedidos.csv sin datos.")
        return
    for line in plines[1:]:
        parts = [p.strip() for p in line.split(",")]
        # partes: id, cliente_id, producto_id, cantidad, fecha
        pid = parts[2] if len(parts) > 2 else ""
        try:
            cantidad = int(parts[3]) if len(parts) > 3 else 0
        except:
            cantidad = 0
        precio = precio_por_id.get(pid, 0)
        tot = cantidad * precio
        totales[pid] = totales.get(pid, 0) + tot

    # 3) crear lista de filas [producto_id, nombre, total] para ordenar
    filas = []
    for pid, total in totales.items():
        filas.append([pid, nombre_por_id.get(pid, "Desconocido"), int(total)])

    # 4) ordenar por total descendente (índice 2)
    selection_sort_list_of_lists(filas, key_index=2, reverse=True)

    # 5) escribir total_ventas.csv (manual como el profesor)
    with open("total_ventas.csv", "w", encoding="utf-8") as f:
        f.write("producto_id,nombre_producto,total\n")
        for row in filas:
            f.write(",".join([row[0], row[1], str(row[2])]) + "\n")

    # mostrar en pantalla
    print("\nTotal de ventas por producto (mayor -> menor):")
    print("{:<12} {:<30} {:>12}".format("producto_id","nombre_producto","total"))
    for r in filas:
        print("{:<12} {:<30} {:>12}".format(r[0], r[1], r[2]))
    print("\nArchivo total_ventas.csv creado/actualizado.\n")

# --------------- Opción 4: Ver clientes que han realizado compras -----------------
def opcion_4_clientes_con_compras():
    # leer clientes
    clientes = []
    if not os.path.exists("clientes.csv"):
        print("clientes.csv no existe.")
        return
    with open("clientes.csv", "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(lines) < 2:
        print("clientes.csv sin datos.")
        return
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        # [id, nombre, email]
        clientes.append(parts)

    # leer pedidos y sacar ids de clientes que compraron
    clientes_con_pedido = set()
    if not os.path.exists("pedidos.csv"):
        print("pedidos.csv no existe.")
        return
    with open("pedidos.csv", "r", encoding="utf-8") as f:
        plines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
    if len(plines) >= 2:
        for line in plines[1:]:
            parts = [p.strip() for p in line.split(",")]
            cid = parts[1] if len(parts) > 1 else ""
            if cid:
                clientes_con_pedido.add(cid)

    # filtrar clientes por los que aparecen en el set
    filtrados = []
    for c in clientes:
        cid = c[0] if len(c) > 0 else ""
        if cid in clientes_con_pedido:
            filtrados.append(c)  # c = [id,nombre,email]

    # ordenar alfabeticamente por nombre (índice 1) usando selection sort
    # selection_sort_list_of_lists espera comparar valores numéricos o strings directamente
    # convertimos los nombres a minúsculas para comparar de forma consistente
    # para usar la misma función se reemplaza cada fila por [id, nombre_lower, email] solo temporalmente
    temp = []
    for row in filtrados:
        # guardamos nombre en minúscula en la posición 1 para que la comparación sea consistente
        temp.append([row[0], row[1].lower() if len(row) > 1 else "", row[2] if len(row) > 2 else ""])
    selection_sort_list_of_lists(temp, key_index=1, reverse=False)
    # reconstruir 'filtrados' con los nombres originales (case original)
    ordered = []
    for t in temp:
        # buscar el registro original con mismo id (t[0])
        for orig in filtrados:
            if orig[0] == t[0]:
                ordered.append(orig)
                break

    # mostrar resultado
    print("\nClientes que han realizado compras (ordenados por nombre):")
    if not ordered:
        print("No hay clientes con compras registradas.")
    else:
        print("{:<4} {:<20} {:<30}".format("id","nombre","email"))
        for c in ordered:
            nombre = c[1] if len(c) > 1 else ""
            email = c[2] if len(c) > 2 else ""
            print("{:<4} {:<20} {:<30}".format(c[0], nombre, email))
    print()

# ----------------------------- Menú principal ----------------------------------
def main():
    crear_archivos_ejemplo_si_faltan()  # crea archivos como el profesor dio si no existen
    while True:
        print("===== Simulacro Parcial - estilo profesor =====")
        print("1) Ver productos ordenados por precio (actualiza productos.csv)")
        print("2) Agregar un nuevo cliente")
        print("3) Calcular total de ventas por producto (genera total_ventas.csv)")
        print("4) Ver clientes que han realizado compras")
        print("5) Salir")
        opcion = input("Opción: ").strip()
        if opcion == '1':
            opcion_1_ordenar_productos()
        elif opcion == '2':
            opcion_2_agregar_cliente()
        elif opcion == '3':
            opcion_3_total_ventas_por_producto()
        elif opcion == '4':
            opcion_4_clientes_con_compras()
        elif opcion == '5':
            print("Saliendo... ¡éxitos en el parcial, Gaby!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()


