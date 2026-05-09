"""
Dado un archivo de texto. Decir cuantas palabras terminan con punto.
"""

filename = "texto.txt"

with open(filename) as file:
    text_file =  file.read()


# print("texto: ", text_file)

# contador = 0

# for palabra in text_file.split(): 
#     if palabra[-1] == ".":
#         contador += 1



# print("la cantidad de palabras que terminan en . son: ", contador)


contador = sum([1 for palabra in text_file.split() if palabra[-1] == "." ])
print("la cantidad de palabras que terminan en . son: ", contador)
