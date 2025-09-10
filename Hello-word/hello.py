# En este codigo estoy guardando un archivo de texto en un diccionario 
def load_file_to_dict(filename): #nombre
data_dict = {} # crea un diccionario vacio donde ira la llave y su valor 
with open (filename, "r") as file: # abre el archivo para su lectura y posterior cierre 
for line in line : # lees linea por linea 
    key, value = line.strip().split(",") # se eliminan los espacios y saltos de liea ,divide la lista en comas 
    data_dict[key] = value # guarda el par en el diccionario 
return data_dict #vuelve el diccionario completo

def direct_search(data_dict,key): # busca la llave y si existe te duevuelve su valor 
                                # sino devuelve un mensaje de que no existe 
    return data_dict.get(key, "Element not found")

    data = load_file_to_dict("data.txt")  #contiene el archivo en memoria como dict
key_to_search = "3" # busca una clave 
result = direct_search(data, key_to_search)
print(f"Search result for key '{key_to_search}': {result}") # se imprime el resultado 







import os
import json  # import usado 

def write_record(file_name, record): 
    record_id = record['id'] # se calcula 
    position = hash(record_id) % 100  # usa la función hash() de Python para elegir una “ranura” entre 0 y 99.
    print(position)  # imprime pocision 
    
    with open(file_name, 'r+b') as file:
        # Seek to the calculated position
        file.seek(position * 100)  # mueve el punzon al byte 
        record_str = json.dumps(record).ljust(100) # convierte de dict a json y le pone un valor en la derecha
        print(record_str)
        file.write(record_str.encode('utf-8')) # escribe ese byte correspondiente 

def read_record(file_name, record_id): #Reads a record from the file based on its unique ID.
    
    position = hash(record_id) % 100 # va al byte correspondiente 

    with open(file_name, 'rb') as file:
        file.seek(position * 100)
        record_data = file.read(100).decode('utf-8').strip() # recocorres data 

        if record_data:
            return json.loads(record_data) # si no esta vacio intenta json y devuelve el dict
        else:
            return None # si no esta pues devuelve nada 

def initialize_file(file_name, size=100):
    # Crea un archivo de tamaño size * 100 bytes vacio para tener acceso directo 
    with open(file_name, 'wb') as file:
        file.write(b'\x00' * (size * 100)) 

def main():  # inicializa archivo , escribe 3 registros y los lee 
    file_name = "direct_access_file.dat"
    print(hash('Alice') % 100)

# añade registros al archivo 
    write_record(file_name, {'id': 'R001', 'name': 'Alice', 'balance': 500.75})
    write_record(file_name, {'id': 'R002', 'name': 'Bob', 'balance': 300.50})
    write_record(file_name, {'id': 'R003', 'name': 'Charlie', 'balance': 150.25})

# recupera y ve los registros 
print("Reading records directly:")
    print(read_record(file_name, 'R002'))
    print(read_record(file_name, 'R001'))
    print(read_record(file_name, 'R003'))

    print(hash('R001') % 100)

if __name__ == "__main__":
    main()







# crear el archivo 
with open("archivo_secuencial.txt", "w") as file: # abres para sobreescribir 
    file.write("0|Juan, 30 años\n")
    file.write("1|María, 25 años\n")
    file.write("2|Pedro, 40 años\n")

# Crear índice
indice = {}
with open("archivo_secuencial.txt", "r") as file:
    for line in file:
        pos, data = line.split("|") # se separa en posicion y datos 
        clave = data.split(",")[0]  # Nombre como clave
        indice[clave.strip()] = int(pos) # guaradas las claves en este caso nombre 

# Búsqueda usando índice
busqueda = "María"
if busqueda in indice:
    with open("archivo_secuencial.txt", "r") as file:
        file.seek(indice[busqueda] * 15)  # Asumiendo longitud fija
        print(file.readline())
else:
    print(f"{busqueda} no encontrado.")







class F:

    def sequential_search_file(self, filename, value, param): # busca en un cs "secuencial"la primera fila cuyo campo pram tenga value 
        index_param = -1  # prepara la variable donde ira el encabezado
        with open(filename, "r") as file:
            for i, line in enumerate(file): # itera  
                arr = line.split(",") # busca pos del indice de la columna param
                if( i == 0 ): # en la primera iteracion asume es encabezado 
                    try:
                        index_param = arr.index(param) 
                    except Exception :
                        return "No encontré la columna " + param
                elif arr[index_param] == value: # compara para ver si coinciden 
                    return arr
        return -1  


    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f:

                print(linea.strip()) # imprime cada linea y quita saltos de linea 
    
    def write(self, filename, dictionary):
        enable = 1 
        id = 1
        with open(filename, "w", encoding="utf-8") as f:
            labels = list(dictionary[0].keys()) # toma los nombres de las columnas aprtir del primer diccionario
            f.write("id,")
            for label in labels: # esc encabezado
                f.write(label + ",")
            f.write("status" + "\n")
            for a in dictionary: # para cada dict escribe un id 
                count = 0
                f.write(str(id)+ ",") 
                for d in a.values(): # escribe los valores y pone coma 
                    f.write(d )
                    count+=1
                    f.write(",")
                id+=1  # aumenta el id 
                f.write(str(enable)+"\n")
           
    
    def delete(self, filename, id): 
        list = []
        with open(filename, "r", encoding="utf-8") as f: # abres en modo lectura 
            list = f.readlines() # guardas filas en un lista donde cada elem es un string con salto de linea 
        newList = [] # creas nueva lista 
        for l in list: # recorres cada linea del archivo 
            arr = l.strip().split(',') # elimina solatos y pon comas 
            if str(arr[0]) == str(id): # compara el primer elemento osea el id de la funcion, si coincide es el que queremos eliminar 
                print(id)
                arr[len(arr)-1] = "0" # toma la status y le pone 0 osea lo elimina 
               
               # desde aqui 
                ll = ""
                count = 1
                for a in arr:
                    ll = ll + str(a)  
                    if count < len(arr):
                        ll = ll + ","
                    count+=1
                l = ll + "\n"
                # hasta aca une los elementos otra vez con comas y saltos 
            newList.append(l) # si era lo que se debia eliminar agrega status=0 o deja sin cambios 
        self.write_array(filename, newList) # llama el archivo en escritura escribe todo y agrega lo nuevo


    def write_array(self, filename, list):
        with open(filename, "w", encoding="utf-8") as f:
            for l in list: # toma todo de l lo escribe en el archivo 
                f.write(l)


people = [{"name":"Juan", "lastname": "Perez"},
          {"name":"Luis", "lastname": "Gómez"},
          {"name":"Mario", "lastname": "Ruiz"},]

product = [{"name":"PC", "price": "50"},
          {"name":"Mouse", "price": "30"},
          {"name":"Keyboard", "price": "20"},]



sales = [{"name":"PC", "amount": "50"},
          {"name":"Mouse", "amount": "30"},
          {"name":"Keyboard", "amount": "20"},]

f = F()
f.write("people.csv", people)
f.write("products.csv", product)
f.write("sales.csv",sales)

print(f.sequential_search_file("people.csv", "Perez","lastname"))

f.delete("products.csv", 1)






# Create a file with some records
with open("data.txt", "w") as file: # se abre el archivo en modo escritura 
    file.writelines(["John\n", "Maria\n", "Peter\n", "Lucy\n"]) # escribe todas las cadenas de la lista en el archivo 

# Sequential search in the file
def sequential_search_file(filename, value): # archivo y valor osea nombre a buscar
    with open(filename, "r") as file:
        for i, line in enumerate(file): # empieza indice cero y contenido por linea 
            if line.strip() == value:  # elimina saltos de linea y si coincide encontramos registro
                return i  # devuelve posicion del registro 
    return -1  # si no lo encuentra pues aja 

# Perform the search
result = sequential_search_file("data.txt", "Lucy") # se busca el valor en este caso resul 3
if result != -1:
    print(f"Element found at line {result + 1}") # como resul esta en 3 le sumamos uno por que se cuenta desde 1 no 0
else:
    print("Element not found")









    def truncate_file(file_name): 
    """
    Truncates (empties) the file content, leaving it blank.
    """
    with open(file_name, 'w') as file:
        # archivo vacio y existe 
        pass


def add_transaction(file_name, transaction):
    
    with open(file_name, 'a') as file:  # 'a' is for append mode todo se añade al final 
        file.write(f"{transaction['id']},{transaction['date']},{transaction['amount']}\n") # escribe una linea por transaccion al formato 


# Function to read all transactions in sequential order
def read_transactions(file_name):

    transactions = [] # prepara la lista 
    try:
        with open(file_name, 'r') as file: # si no existe salta al except
            for line in file:
                transaction_id, date, amount = line.strip().split(',') # se asumen 3 campos 
                transactions.append({ # crea un diccionario por transaccion y convierte amount a float
                    'id': transaction_id,
                    'date': date,
                    'amount': float(amount)
                })
    except FileNotFoundError:
        print("The file does not exist. Please add a transaction first.")
    return transactions


# Main function to test sequential file organization
def main():
    transaction_file = "sequential_transactions.txt"
    truncate_file(transaction_file)
    add_transaction(transaction_file, {'id': 'T001', 'date': '2025-01-01', 'amount': 100.50})
    add_transaction(transaction_file, {'id': 'T002', 'date': '2025-01-02', 'amount': 300.75})
    add_transaction(transaction_file, {'id': 'T003', 'date': '2025-01-03', 'amount': 150.25})

    # Read and display all transactions
    transactions = read_transactions(transaction_file)
    print("Transactions stored sequentially:")
    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    main()



#menu en clases 

import csv
import os


CLIENTES_FILE = 'clientes.csv'
PEDIDOS_FILE = 'pedidos.csv'

# clientes 

def cargar_clientes():
    
    clientes = []
    if os.path.exists(CLIENTES_FILE):
        with open(CLIENTES_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id_cliente'] = int(row['id_cliente'])
                row['activo'] = int(row['activo'])
                clientes.append(row)
    return clientes


def guardar_clientes(clientes):

    with open(CLIENTES_FILE, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id_cliente', 'nombre', 'apellido', 'telefono', 'activo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for c in clientes:
            writer.writerow(c)


def registrar_cliente(clientes):
    
    nombre = input('Nombre: ').strip()
    apellido = input('Apellido: ').strip()
    telefono = input('Teléfono: ').strip()
    nuevo_id = obtener_nuevo_id(clientes, 'id_cliente')
    clientes.append({'id_cliente': nuevo_id, 'nombre': nombre, 'apellido': apellido,
                     'telefono': telefono, 'activo': 1})
    guardar_clientes(clientes)
    print("Cliente registrado con ID:", nuevo_id)


   clientes = []
    if os.path.exists("clientes.csv"):
        with open("clientes.csv", "r", encoding="utf-8") as f:
            lines = [ln.rstrip("\n") for ln in f.readlines() if ln.strip() != ""]
        if lines:
            for line in lines[1:]:
                parts = [p.strip() for p in line.split(",")]
                clientes.append(parts)  

def eliminar_cliente(clientes): # tuve un pequeño problema aqui y si me guie de ia 

    id_elim = input('ID del cliente a eliminar: ').strip()
    if not id_elim.isdigit():
        print("ID inválido")
        return
    id_elim = int(id_elim)
    for c in clientes:
        if c['id_cliente'] == id_elim and c['activo'] == 1:
            c['activo'] = 0
            guardar_clientes(clientes)
            print("Cliente eliminado lógicamente")
            return
    print("Cliente no encontrado o ya estaba inactivo")


# parte pedidos_

def cargar_pedidos():
    
    pedidos = []
    if os.path.exists(PEDIDOS_FILE):
        with open(PEDIDOS_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id_pedido'] = int(row['id_pedido'])
                row['id_cliente'] = int(row['id_cliente'])
                row['precio'] = float(row['precio']) if row['precio'] else 0.0
                row['cantidad'] = int(row['cantidad']) if row['cantidad'] else 0
                row['activo'] = int(row['activo'])
                pedidos.append(row)
    return pedidos


def guardar_pedidos(pedidos):
    
    with open(PEDIDOS_FILE, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id_pedido', 'id_cliente', 'producto', 'precio', 'cantidad', 'activo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in pedidos:
            writer.writerow(p)


def registrar_pedido(clientes, pedidos):
    
    id_cliente = input('ID del clientee: ').strip()
    if not id_cliente.isdigit():
        print("ID inválido")
        return
    id_cliente = int(id_cliente)
    cliente = next((c for c in clientes if c['id_cliente'] == id_cliente and c['activo'] == 1), None)
    if not cliente:
        print("Cliente no encontrado o inactivo")
        return

    producto = input("Producto: ").strip()
    precio = input("Precio (opcional): ").strip()
    cantidad = input("Cantidad (opcional): ").strip()
    precio = float(precio) if precio else 0.0
    cantidad = int(cantidad) if cantidad else 0

    nuevo_id = obtener_nuevo_id(pedidos, 'id_pedido')
    pedidos.append({'id_pedido': nuevo_id, 'id_cliente': id_cliente, 'producto': producto,
                    'precio': precio, 'cantidad': cantidad, 'activo': 1})
    guardar_pedidos(pedidos)
    print("Pedido registrado con ID:", nuevo_id)


def listar_pedidos_cliente(pedidos, clientes):
   
    id_cliente = input('ID del cliente: ').strip()
    if not id_cliente.isdigit():
        print("ID inválido")
        return
    id_cliente = int(id_cliente)
    cliente = next((c for c in clientes if c['id_cliente'] == id_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return

    print("\nPedidos de", cliente['nombre'], cliente['apellido'])
    encontrado = False
    for p in pedidos:
        if p['id_cliente'] == id_cliente and p['activo'] == 1:
            encontrado = True
            print(p['id_pedido'], "-", p['producto'], "-", p['precio'], "-", p['cantidad'])
    if not encontrado:
        print("No tiene pedidos activos")



def eliminar_pedido(pedidos): # tiene prblemas al correr 
    id_pedido = input("ID del pedido a eliminar: ").strip()
    for pedido in pedidos:
        if pedido['id_pedido'] == id_pedido and pedido['activo'] == 1:
            pedido['activo'] = 0
            guardar_pedidos(pedidos)
            print("Pedido eliminado.")
            return
    print(" Pedido no encontrado / inactivo")


# parte de ventas

def guardar_venta(clientes, pedidos):
    """
    Registra una venta (similar a un pedido pero obligatorio con cantidad).
    """
    id_cliente = input("ID del cliente: ").strip()
    if not id_cliente.isdigit():
        print("ID inválido")
        return
    id_cliente = int(id_cliente)
    cliente = next((c for c in clientes if c['id_cliente'] == id_cliente and c['activo'] == 1), None)
    if not cliente:
        print("Cliente no encontrado o inactivo")
        return

    producto = input("Producto: ").strip()
    cantidad = input("Cantidad: ").strip()
    if not cantidad.isdigit():
        print("Cantidad inválida")
        return
    cantidad = int(cantidad)
    precio = input("Precio (opcional): ").strip()
    precio = float(precio) if precio else 0.0

    nuevo_id = obtener_nuevo_id(pedidos, 'id_pedido')
    pedidos.append({'id_pedido': nuevo_id, 'id_cliente': id_cliente, 'producto': producto,
                    'precio': precio, 'cantidad': cantidad, 'activo': 1})
    guardar_pedidos(pedidos)
    print("Venta registrada con ID:", nuevo_id)


def listar_ventas_por_cliente(clientes, pedidos):
    """
    Lista las ventas de un cliente y calcula el total.
    """
    nombre = input("Nombre del cliente: ").strip().lower()
    clientes_encontrados = [c for c in clientes if c['nombre'].lower() == nombre and c['activo'] == 1]

    if not clientes_encontrados:
        print("Cliente no encontrado o inactivo")
        return

    for cliente in clientes_encontrados:
        print("\nVentas de", cliente['nombre'], cliente['apellido'])
        ventas = [p for p in pedidos if p['id_cliente'] == cliente['id_cliente'] and p['activo'] == 1]
        if not ventas:
            print("No tiene ventas")
            continue
        total = 0
        for v in ventas:
            subtotal = v['precio'] * v['cantidad']
            total += subtotal
            print(v['producto'], "-", v['cantidad'], "x", v['precio'], "=", subtotal)
        print("TOTAL:", total)


# Utilidades 

def obtener_nuevo_id(items, id_field):
    
    if items:
        return max(item[id_field] for item in items) + 1
    else:
        return 1


#                               menu pricipal

def menu():
    clientes = cargar_clientes()
    pedidos = cargar_pedidos()

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente (lógico)")
        print("4. Registrar pedido")
        print("5. Listar pedidos de cliente")
        print("6. Guardar venta")
        print("7. Listar ventas por cliente")
        print("8. eliminar pedido")
        print("9. Salir")

        opcion = input("Opción: ").strip()

        if opcion == '1':
            registrar_cliente(clientes)
        elif opcion == '2':
            listar_clientes(clientes)
        elif opcion == '3':
            eliminar_cliente(clientes)
        elif opcion == '4':
            registrar_pedido(clientes, pedidos)
        elif opcion == '5':
            listar_pedidos_cliente(pedidos, clientes)
        elif opcion == '6':
            guardar_venta(clientes, pedidos)
        elif opcion == '7':
            listar_ventas_por_cliente(clientes, pedidos)
        elif opcion == '9':
            print("Saliendo...")
            break
        elif opcion == '8':
            eliminar_pedido(pedidos)
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()




