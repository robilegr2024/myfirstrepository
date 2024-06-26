# Leer el contenido del archivo
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Crear una nueva cadena vacía para almacenar la secuencia limpiada
cleaned_content = ''

# Recorrer cada línea del contenido del archivo
for line in content.splitlines():
    # Omitir las líneas que no contienen la secuencia
    if 'ORIGIN' in line or '//' in line:
        continue
    # Quitar los números y espacios de cada línea y añadir a cleaned_content
    for char in line:
        if char.isalpha():
            cleaned_content += char

# Confirmar que la secuencia tiene 110 caracteres
if len(cleaned_content) == 110:
    print("La secuencia limpiada tiene 110 caracteres.")
else:
    print(f"La secuencia limpiada tiene {len(cleaned_content)} caracteres, se esperaba 110.")

# Mostrar la secuencia limpiada
print(cleaned_content)
