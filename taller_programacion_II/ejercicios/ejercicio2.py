"""
Tengo un archivo de logs

[2024-03-15 08:23:11] ERROR   | servidor.py  | Conexión rechazada en puerto 8080
[2024-03-15 08:45:02] INFO    | app.py       | Usuario 'admin' inició sesión
[2024-03-15 09:01:55] WARNING | database.py  | Consulta tardó más de 2 segundos
[2024-03-15 09:10:30] ERROR   | servidor.py  | Timeout al conectar con base de datos
[2024-03-15 09:33:47] INFO    | app.py       | Usuario 'juan' cerró sesión
[2024-03-15 10:05:21] ERROR   | app.py       | Permiso denegado para usuario 'pedro'
[2024-03-1510:45:00] WARNING | servidor.py  | Uso de CPU al 90%
 
1. Total de entradas por error.

"""
from collections import Counter


with open("logs.txt") as file:
    # lista de strings
    texto_lineas = file.readlines()

lista_archivos = []
lista_errors = []

for linea in texto_lineas:

    parser_line = linea.split("]")
    # [ "[2024-03-15 08:23:11", " ERROR   | servidor.py  | Conexión rechazada en puerto 8080"]
    error_detail = parser_line[1].split("|")
    # [" ERROR   ", " servidor.py  ", " Conexión rechazada en puerto 8080" ]
    lista_errors.append(error_detail[0].strip())
    lista_archivos.append(error_detail[1].strip())


print(lista_archivos)

counter_errores = Counter(lista_errors)


print(counter_errores.most_common())

for error, cant in counter_errores.most_common():
    print(f"logging level : {error}   --- canidad:: {cant}")


# diccionario con los distinbntos niveles de logginy las cantidad de veces que aparece cada uno 

# { "ERROR": 3, "INFO": 2, "WARNING" : 2}

errores = { clave : valor for clave, valor in counter_errores.most_common() }

print(errores)