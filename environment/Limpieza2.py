# Leer el contenido del archivo original
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()
print(content)
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

# Guardar la secuencia limpiada en un nuevo archivo
with open('preproinsulin-seq-clean.txt', 'w') as clean_file:
    clean_file.write(cleaned_content)

# Confirmar que la secuencia tiene 110 caracteres
if len(cleaned_content) == 110:
    print("La secuencia limpiada tiene 110 caracteres.")
else:
    print(f"La secuencia limpiada tiene {len(cleaned_content)} caracteres, se esperaba 110.")


# Guardar aminoácidos 1-24 en lsinsulin-seq-clean.txt
with open('lsinsulin-seq-clean.txt', 'w') as file:
    lsinsulin_seq = cleaned_content[0:24]
    file.write(lsinsulin_seq)
    if len(lsinsulin_seq) == 24:
        print("lsinsulin-seq-clean.txt tiene 24 caracteres.")
    else:
        print(f"lsinsulin-seq-clean.txt tiene {len(lsinsulin_seq)} caracteres, se esperaba 24.")

# Guardar aminoácidos 25-54 en binsulin-seq-clean.txt
with open('binsulin-seq-clean.txt', 'w') as file:
    binsulin_seq = cleaned_content[24:54]
    file.write(binsulin_seq)
    if len(binsulin_seq) == 30:
        print("binsulin-seq-clean.txt tiene 30 caracteres.")
    else:
        print(f"binsulin-seq-clean.txt tiene {len(binsulin_seq)} caracteres, se esperaba 30.")

# Guardar aminoácidos 55-89 en cinsulin-seq-clean.txt
with open('cinsulin-seq-clean.txt', 'w') as file:
    cinsulin_seq = cleaned_content[54:89]
    file.write(cinsulin_seq)
    if len(cinsulin_seq) == 35:
        print("cinsulin-seq-clean.txt tiene 35 caracteres.")
    else:
        print(f"cinsulin-seq-clean.txt tiene {len(cinsulin_seq)} caracteres, se esperaba 35.")

# Guardar aminoácidos 90-110 en ainsulin-seq-clean.txt
with open('ainsulin-seq-clean.txt', 'w') as file:
    ainsulin_seq = cleaned_content[89:110]
    file.write(ainsulin_seq)
    if len(ainsulin_seq) == 21:
        print("ainsulin-seq-clean.txt tiene 21 caracteres.")
    else:
        print(f"ainsulin-seq-clean.txt tiene {len(ainsulin_seq)} caracteres, se esperaba 21.")