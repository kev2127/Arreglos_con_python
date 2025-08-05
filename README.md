# Arreglos_con_python

Este repositorio contiene ejemplos prácticos del uso de **variables no primitivas** en Python, específicamente **arreglos** (vectores y matrices). Se incluyen operaciones básicas y útiles para quienes están comenzando en el manejo de estructuras de datos más complejas que los tipos primitivos.

---

## 📌 ¿Qué son las variables no primitivas?

En Python, las **variables no primitivas** son aquellas que pueden almacenar múltiples valores y ofrecen estructuras más complejas. A diferencia de los tipos primitivos (como `int`, `float`, `bool` o `str`), las variables no primitivas como listas, tuplas, diccionarios y conjuntos permiten almacenar y manipular múltiples datos a la vez.

En este repositorio nos enfocamos en **listas** (que usaremos como vectores y matrices).

---

## 📋 Contenido

1. [Vectores (listas unidimensionales)](#vectores)
2. [Matrices (listas bidimensionales)](#matrices)
3. [Operaciones comunes](#operaciones-comunes)
4. [Uso de librerías como NumPy](#numpy)

---

## 📌 Vectores

Un **vector** en Python se representa como una **lista** unidimensional. Es ideal para almacenar una secuencia de datos ordenados.

```python
# Crear un vector
numeros = [1, 2, 3, 4, 5]

# Acceso a elementos
print(numeros[0])  # Imprime 1

# Modificación
numeros[2] = 10

# Agregar elementos
numeros.append(6)

# Eliminar elementos
numeros.remove(4)

# Recorrer un vector
for num in numeros:
    print(num)
# Arreglos_con_python
Ejemplos de variable  no primitivos, operaciones con arreglos sea con vectores o matrices
