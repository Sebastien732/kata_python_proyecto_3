# %% [markdown]
# ## PROYECTO LÓGICA: Katas de Python  
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
# 

# %%
def contar_letras():
    contador_letra = {} # Crea un diccionario vacío para almacenar la frecuencia de cada letra
    cadena_usuario = input("Introduce una frase: ") # Solicita al usuario una frase
    cadena_sin_espacio = cadena_usuario.replace(" ", "") # Elimina los espacios de la frase
    
    for letra in cadena_sin_espacio:
    
        if letra in contador_letra:     # Verifica si la letra ya existe en el diccionario y aumenta su contador
            contador_letra[letra] += 1
        else:                           # Añade la letra al diccionario con valor inicial 1
            contador_letra[letra] = 1 
    print(cadena_usuario)
    print(cadena_sin_espacio)

    return contador_letra # Devuelve el diccionario con las frecuencias de las letras

contar_letras() #llamamos a la funcion

# %% [markdown]
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# %%
numeros = [3, 5, 15, 22, 1, 125, 1012.5]  # Crea una lista que contiene números enteros y decimales
print(f"la lista original de numeros es: {numeros}")  # Muestra por pantalla la lista original

def doblar(numeros):  # Define una función que recibe un número y devuelve su valor doblado
    return int(numeros * 2)  # Multiplica el número por 2 y lo convierte en entero

resultado = list(map(doblar, numeros))  # Aplica la función 'doblar' a cada elemento de la lista y guarda los resultados en una nueva lista

print(f"la nueva lista de numeros es:{resultado}")  # Muestra por pantalla la nueva lista con los valores transformados



# %% [markdown]
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
# 

# %%
def filtra_palabra_cion(lista_palabras, palabra_objetivo):  # Define una función que recibe una lista de palabras y una subcadena objetivo
    lista_filtrada = []  # Crea una lista vacía para guardar las palabras que contienen la subcadena
    for palabra in lista_palabras:  # Recorre cada palabra de la lista original
        if palabra_objetivo in palabra:  # Verifica si la subcadena objetivo está dentro de la palabra actual
            lista_filtrada.append(palabra)  # Añade la palabra a la lista filtrada si contiene la subcadena
    return lista_filtrada  # Devuelve la lista con las palabras que cumplen la condición

palabras = ["educacion", "integracion", "respeto", "vision", "division", "imaginacion"]  # Declara una lista con palabras variadas
objetivo = "cion"  # Asigna como objetivo la subcadena que se quiere buscar
lista_filtrada = filtra_palabra_cion(palabras, objetivo)  # Llama a la función y almacena las palabras que contienen la subcadena
print(lista_filtrada)  # Muestra la lista resultante con las palabras filtradas


# %% [markdown]
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
# 

# %%
lista_1 = [12, 36, 3, 85, 104, 21, 65]  
lista_2 = [12, 25, 48, 2, 45, 48, 21]   

def diferencia(lista_1, lista_2):  # Define una función que recibe dos listas como parámetros
    return list(map(lambda X, Y: X - Y, lista_1, lista_2))  # Resta los elementos correspondientes de ambas listas usando map y una función lambda

lista_3 = list(diferencia(lista_1, lista_2))  # Llama a la función y guarda el resultado en una nueva lista

print(f"la lista 1 es:{lista_1}")  
print(f"la lista 2 es:{lista_2}")  
print(f"la lista 3 representa los valores de la lista 1 menos los valores de la lista 2:{lista_3}")  # Muestra el resultado de la resta elemento a elemento


# %% [markdown]
# 
# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.
# 

# %%
def calcula_nota_media(lista_numeros, nota_minima):  # Define una función que recibe una lista de notas y la nota mínima para aprobar
    media = sum(lista_numeros) / len(lista_numeros)  # Calcula la media aritmética de las notas
    if media >= nota_minima:  # Comprueba si la media es mayor o igual que la nota mínima
        print("aprobado")  # Muestra "aprobado" si la condición se cumple
    else:
        print("suspenso")  # Muestra "suspenso" si la media es menor que la nota mínima

numeros = [4, 7, 5, 6, 7, 6, 5]  # Declara una lista de notas numéricas
nota_minima = 5  # Establece la nota mínima para aprobar

calcula_nota_media(numeros, nota_minima)  # Llama a la función con los argumentos definidos


# %% [markdown]
# 
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
# 

# %%
def calc_factorial(n):  
    if n < 0:  # Comprueba si el número es negativo para evitar errores
        print("imposible")  # Muestra un mensaje de error si el número es negativo
    elif n == 0 or n == 1:  # Verifica si el número es 0 o 1
        return 1  # Devuelve 1 porque el factorial de 0 y 1 es 1
    else:
        return n * calc_factorial(n - 1)  # Realiza la llamada recursiva multiplicando n por el factorial de n-1

num = 4  # Asigna el valor 4 a la variable num
print(calc_factorial(num))  # Imprime el resultado del factorial calculado


# %% [markdown]
# 
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
# 

# %%
def conv_tpl_str(lista_tuplas):  
    return list(map(lambda t: " ".join(t), lista_tuplas))  # Aplica una función lambda para unir los elementos de cada tupla y devuelve una lista

lista_tuplas = [("uno", "dos"), ("tres", "cuatro")]  # Crea una lista de tuplas con cadenas de texto

lista_strings = conv_tpl_str(lista_tuplas)  # Llama a la función y guarda el resultado en una nueva lista

print(lista_strings)  # Muestra la lista resultante de cadenas
print(type(lista_strings))  # Muestra el tipo del objeto resultante (list)

   

# %% [markdown]
# 
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
# 

# %%
def dividir_numeros():  
    try:
        num1 = float(input("Introduce el primer número: "))  # Solicita el primer número y lo convierte a decimal
        num2 = float(input("Introduce el segundo número: "))  # Solicita el segundo número y lo convierte a decimal
        resultado = num1 / num2  # Realiza la división y guarda el resultado
    except ZeroDivisionError:  # Captura el error si el segundo número es cero
        print("Error: No se puede dividir entre cero.")  # Muestra un mensaje si hay intento de división por cero
    except ValueError:  # Captura errores si las entradas no son números válidos
        print("Error: Por favor, introduce solo números.")  # Informa al usuario sobre el formato incorrecto
    else:
        print(f"El resultado de la división es: {resultado}")  # Muestra el resultado si no hubo errores

dividir_numeros();  # Llama a la función para ejecutarla



# %% [markdown]
# 
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
# 

# %%
lista_animales = ["Gato", "Conejo", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Cacatoes", "Jabali", "Tortuga"]  # Define una lista con diferentes tipos de animales

def filtrar_mascotas_autorizadas(lista_anim):  # Define una función que evalúa si un animal está autorizado como mascota
    animales_prohibidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]  # Declara una lista con animales no permitidos
    return lista_anim not in animales_prohibidos  # Devuelve True si el animal no está en la lista de prohibidos

animales_acceptados = list(filter(filtrar_mascotas_autorizadas, lista_animales))  # Filtra los animales permitidos y convierte el resultado en lista

print(animales_acceptados)  # Muestra por pantalla la lista de animales autorizados




# %% [markdown]
# 
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
# 

# %%
def calc_promedio(list_num):  
    if not list_num:  
        return "La lista esta vacía"  # Devuelve un mensaje si no hay elementos en la lista
    promedio = sum(list_num) / len(list_num)  # Calcula la suma dividida entre la cantidad de elementos
    return promedio  # Devuelve el promedio calculado

calc_promedio([50, 52, 85, 97, 410, 52])  # Llama a la función con una lista de números y ejecuta el cálculo



# %% [markdown]
# 
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
# 

# %%
def intro_edad():  # Define una función que solicita al usuario su edad y la valida
    try:
        edad = int(input("Introduce tu edad"))  # Pide al usuario que introduzca su edad y la convierte a entero
        if edad > 120 or edad < 0:  # Comprueba si la edad está fuera de un rango razonable
            print("El número introducido es incorrecto")  # Muestra un mensaje de error si la edad no es válida
        else:
            print(f"Tienes {edad} años")  # Muestra la edad del usuario si está dentro de un rango válido
    except ValueError:  # Captura el error si el usuario introduce un valor que no es numérico
        print("Solo puedes introducir números")  # Informa al usuario que solo debe introducir números

intro_edad()  # Llama a la función para ejecutarla


# %% [markdown]
# 
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
# 

# %%
frase_ejemplo = "Eso es una frase de ejemplo para enseñar como esta funcion cuenta las lettras de cada palabra"  

def contar_letras_palabras(frase):  
    div_palabra = frase.split()  # Divide la frase en palabras separadas y las guarda en una lista
    num_letras = list(map(len, div_palabra))  # Calcula la longitud de cada palabra y lo guarda en una lista de números
    return num_letras  # Devuelve la lista con el número de letras por palabra

print(contar_letras_palabras(frase_ejemplo))  # Llama a la función y muestra la lista con las cantidades de letras




# %% [markdown]
# 
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
# 

# %%
def return_mayus_minus(caracteres):
    letras_unicas = set(filter(str.isalpha,caracteres)) # uso de set para eliminar duplicados y filter con str.isalpja para filtrar solo lettras
    resultado13 = list(map(lambda x: (x.upper(), x.lower()), letras_unicas)) # crea una lista de tuplas con funcion map para devolver el resultado por cada caracter 
    return resultado13

conjunto_caracter = "frase de ejemplo"
print(return_mayus_minus(conjunto_caracter))


# %% [markdown]
# 
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
# 

# %%
lista14 = ["martillo", "clavo", "taladro", "destornillador", "sierra", "tornillo", "tijera"]  

def filtra_palabra_primera_letra(palabra, letra):  # Define una función auxiliar que recibe una palabra y una letra
    return palabra.startswith(letra)  # Devuelve True si la palabra comienza con la letra proporcionada

def palabra_letra(lista_palabra, letra):  # Define la función principal que filtra palabras según su letra inicial
    def filtra(palabra):  # Declara una función interna para aplicar el filtro
        return filtra_palabra_primera_letra(palabra, letra)  # Devuelve el resultado de la función auxiliar para cada palabra
    return list(filter(filtra, lista_palabra))  # Aplica el filtro a la lista y convierte el resultado en una lista

palabra_letra(lista14, "t")  # Llama a la función pasando la lista original y la letra "t" como criterio


# %% [markdown]
# 
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
# 

# %%
lista15 = [8, 4, 7, 3, 1, 9, 4, 5, 7, 1, 9, 2, 7, 3, 4, 5] 
mas_tres = list(map(lambda x: x + 3, lista15))  # Suma 3 a cada elemento de la lista usando la función map y una lambda
print(mas_tres)  # Muestra por pantalla la nueva lista con los valores incrementados


# %% [markdown]
# 
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()
# 

# %%
from functools import reduce  # Importa la función reduce del módulo functools (aunque en este código no se utiliza)
lista16 = ["libre", "diccionario", "cuaderno", "manual", "libreta", "registro", "nota"]  
lista16_reducida = list(filter(lambda x: len(x) > 6, lista16))  # Filtra las palabras cuya longitud es mayor a 6 caracteres y crea una nueva lista
print(lista16_reducida)  # Muestra por pantalla la nueva lista después del filtrado


# %% [markdown]
# 
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()
# 

# %%

from functools import reduce  # Importa la función reduce del módulo functools si no esta importada del codigo anterior ya(16)
def lista_a_numero(lista_digitos):  # Define una función que toma como parámetro una lista de dígitos
    return reduce(lambda x, y: x * 10 + y, lista_digitos)  # Combina los dígitos multiplicando por 10 y sumando el siguiente
    

print(lista_a_numero([5, 7, 2]))  # Llama a la función con la lista [5, 7, 2] y muestra el resultado (572) = 5x10
# la logica es (((5*10) + 7) *10) + 2


# %% [markdown]
# 
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. 
# Usa la función filter()

# %%
estudiantes = [  
    {"nombre": "Ana", "edad": 20, "calificación": 85},
    {"nombre": "Luis", "edad": 22, "calificación": 90},
    {"nombre": "María", "edad": 19, "calificación": 78},
    {"nombre": "Carlos", "edad": 21, "calificación": 69},
    {"nombre": "Elena", "edad": 20, "calificación": 93}
]

def filtra_calif90(estudiante):  
    return estudiante["calificación"] >= 90  # Devuelve True si la condición se cumple, lo que permite que el estudiante sea filtrado

calif_mayor_90 = list(filter(filtra_calif90, estudiantes))  # Aplica la función de filtrado a la lista de estudiantes y convierte el resultado en una nueva lista

print(f"Aqui esta la lista de los estudiantes con calificacion mayor o igual a 90 : {calif_mayor_90}")  # Muestra por pantalla los estudiantes que cumplen con la condición


# %% [markdown]
# 
# 19. Crea una función lambda que filtre los números impares de una lista dada.
# 

# %%
lista19 = [14, 48, 51, 36, 95, 11, 21, 74, 53, 65, 20, 16]  
lista19impar = list(filter(lambda x: x % 2 != 0, lista19))  # Filtra los elementos impares de la lista usando una función lambda con la condicion que el residuo de una division no sea = 0
print(lista19impar)  # Muestra por pantalla la lista resultante con los números impares


# %% [markdown]
# 
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()
# 

# %%
lista20 = ["uno","dos","tres","cuatro","cinco",1,2,3,4,5,6]
lista20int = list(filter(lambda x: type(x) is int, lista20)) #filtra solo los elementos de tipo numero enteros
print(lista20int)

# %% [markdown]
# 
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
# 

# %%
num_aleatorio = int(input("introduce un numero")) # pide al usuario un numero entero
num_cubico = lambda x: x ** 3 # funcion lambda que calcula el cubico del valor entrado por el usuario
print(f"El cubo de {num_aleatorio} es {(num_cubico(num_aleatorio))}")

# %% [markdown]
# 
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
# 

# %%
from functools import reduce #importar funcion si no esta hecho ya del ejercicio 16 y 17

lista22 = [5,3,5,7,2]
def producto(x,y): # define la funcion para multiplicar entre 2 numero
    return x * y #devuelve el resultado

valores_multiplicado = reduce(producto,lista22) # Aplica la función 'producto' de forma acumulativa a los elementos de la lista

print(valores_multiplicado)


# %% [markdown]
# 
# 23. Concatena una lista de palabras.Usa la función reduce() .
# 

# %%
lista23 = ["montaña", "sol", "libro", "café", "aventura"]
def concatenar_lista(X,Y):
    return X+Y          #concatena texto ya que no se puede sumar strings
lista_concatenada = reduce(concatenar_lista,lista23)  # Aplica la función de concatenación de manera acumulativa a toda la lista  
print(lista_concatenada)



# %% [markdown]
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
# 

# %%
lista24 = [26, 45, 20, 82, 10]  # Declara una lista de números enteros

def restar(x, y):  # Define una función que toma dos valores
    return x - y  # Resta el segundo valor al primero
lista_diferencia = reduce(restar, lista24)  # Aplica la resta de forma acumulativa a todos los elementos de la lista
print(lista_diferencia)  


# %% [markdown]
# 
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
# 

# %%
def cuenta_caract(x):
    return len(x)       #devuelve la longitud del valor
    print(cuenta_caract()) # muestra el resultado
cuenta_caract(str(input("Entra una palabra"))) # la funcion se aplica a una entrada tipo cadena de parte del usuario


# %% [markdown]
# 
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
# 

# %%

resultado26 = lambda x, y: x % y  # Declara una función lambda que devuelve el residuo de dividir x entre y
print(resultado26(25, 7))  # Llama a la función con los valores 25 y 7, y muestra el resultado por pantalla


# %% [markdown]
# 
# 27. Crea una función que calcule el promedio de una lista de números.
# 

# %%
def calcular_promedio(lista_numeros):  
    return sum(lista_numeros) / len(lista_numeros)  # Devuelve la suma de los números dividida por la cantidad de elementos
numeros = [15, 26.5, 75.6, 27.8, 45.2, 96, 58.1]  # Declara una lista con valores numéricos, incluyendo enteros y decimales
print("promedio = ", round(calcular_promedio(numeros), 2))  # Llama a la función, redondea el resultado a 2 decimales y lo muestra por pantalla


# %% [markdown]
# 
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# 

# %%
list28 = ["kiwi","manzana", "pera", "manzana", "uva", "pera", "plátano", "manzana", "pera", "uva"]  # Declara una lista con varias palabras, algunas repetidas

def primer_dupli(x):  
    comprobados = set()
    for palabra in x:  # Recorre cada palabra en la lista
        if palabra in comprobados:  # Comprueba si la palabra está en la lista
            return palabra  # Devuelve la primera palabra encontrada
        else:
            comprobados.add(palabra)  # añade la palabra al set si no estaba antes
    
primer_dupli(list28)

# %% [markdown]
# 
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.
# 

# %%
def enmascarar_variable(cad_str):
    texto = str(cad_str)        #convierte la variable en cadena string
    longitud = len(texto)       #calcula la longitud del string
    if longitud <= 4:           #condicion con longitud de la variable, si la variable es inferior a 4 caracteres no se enmascara nada
        return texto
    return '#' * (longitud - 4) + texto[-4:] #enmascara todos los caracteres hasta las 4 ultimas letras y añade estas 4 leras por separado

print(enmascarar_variable(123456789))     
print(enmascarar_variable("contraseña"))   


# %% [markdown]
# 
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.
# 

# %%
def son_anagramas(palabra1, palabra2):  
    if sorted(palabra1) == sorted(palabra2):  # Compara las letras ordenadas de ambas palabras
        print(f"la palabra {palabra1} es anagrama de la palabra {palabra2}")  # Informa si son anagramas
    else:
        print(f"la palabra {palabra1} no es un anagrama de la palabra {palabra2}")  # Informa si no son anagramas

son_anagramas("jarabe", "rebaja")  # ejemplo de anagramas
son_anagramas("tomate", "ketchup")  # ejemplo cuando no es un anagrama



# %% [markdown]
# 
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.
# 

# %%

def comprobar_nombre():  
    input_lista = input("Introduce una lista de nombres separados por comas: ")  # Solicita nombres separados por comas
    lista_usuario = [nombre.strip().capitalize() for nombre in input_lista.split(",")]  # Elimina espacios y capitaliza cada nombre
    input_nombre = input("Introduce un nombre: ").strip().capitalize()  # Pide un nombre, elimina espacios y aplica mayucula a la primera letra

    print(f"Lista introducida: {lista_usuario}")  # Muestra la lista estandarizada con 1era lerta en mayuscula
    print(f"Nombre introducido: {input_nombre}")  # Muestra el nombre estandarizado ingresado

    if input_nombre in lista_usuario:  # Comprueba si el nombre está en la lista
        print(f"El nombre '{input_nombre}' fue encontrado en la lista")  # Mensaje si se encuentra
    else:
        print("El nombre introducido no fue encontrado en la lista")  # Mensaje si no está

comprobar_nombre() 


# %% [markdown]
# 
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.
# 

# %%
def buscador_puesto(nombre_empleado, lista_empleados):
        for empleado in lista_empleados:  # Recorre cada diccionario de empleado en la lista
            if empleado["nombre"] == nombre_empleado:  # Comprueba si el nombre coincide con el nombre ingresado
                return(print(f"Esta persona ocupa el puesto de {empleado['puesto']}"))  # Muestra el puesto del empleado si hay coincidencia
        print("Este persona no trabaja en la empresa")  # Muestra mensaje si no se encuentra el nombre en la lista

lista_empleados = [
    {"nombre": "John Smith", "puesto": "Data Scientist"},  # Diccionario con nombre y puesto
    {"nombre": "Maria Gonzalez", "puesto": "Data Analyst"},
    {"nombre": "Ahmed Hassan", "puesto": "Business Intelligence Developer"},
    {"nombre": "Ling Wei", "puesto": "Machine Learning Engineer"},
    {"nombre": "Olga Ivanov", "puesto": "Data Engineer"}
    ]

nombre_empleado = input("Entra el nombre completo del empleado: ").strip().title()  # quita espacio y estandariza el nombre introducido con mayusculas a las primeras letras

buscador_puesto(nombre_empleado, lista_empleados)
   

# %% [markdown]
# 
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# 

# %%
nota_control_continuo = [4,6,2,8,7,4,9,7,6,7]
nota_examen = [2,6,4,9,7,5,8,8,7,7]
suma_listas = lambda nota1, nota2: list(map(lambda x,y: x + y , nota1, nota2)) # Función lambda para sumar elementos correspondientes
nota_final = suma_listas(nota_control_continuo, nota_examen) # crea una lista con el resultado del a suma
print(nota_final)

# %% [markdown]
# 
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.  
# Código a seguir:
#     1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#     2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#     3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#     4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#     5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#     6. Implementar el método
#     info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.  
# 35. Caso de uso:
#     1. Crear un árbol.
#     2. Hacer crecer el tronco del árbol una unidad. 
#     3. Añadir una nueva rama al árbol.
#     4. Hacer crecer todas las ramas del árbol una unidad.
#     5. Añadir dos nuevas ramas al árbol.
#     6. Retirar la rama situada en la posición 2.
#     7. Obtener información sobre el árbol.
# 

# %%
class Arbol: # 34 - crea la classe
    def __init__(self): #tronco inicial de longitud 1 sin ramas
        self.tronco = 1
        self.ramas =[]

    def crecer_tronco(self): #añade 1 de longitud al tronco
        self.tronco += 1
    
    def nueva_rama(self, longitud): #añadimos rama al tronco
        self.ramas.append(longitud)
    
    def crecer_ramas(self, incremento): #añadimos longitud a las ramas
        self.ramas = [ rama + incremento for rama in self.ramas]

    def quitar_rama(self,indice): #quita rama segun la posicion indicada
        if 0 <= indice < len(self.ramas): #condicion para posicion sea correcta
            self.ramas.pop(indice)
        else:
            print("No hay rama en esa posicion")
    
    def info_arbol(self):
        print(f"Longitud tronco: {self.tronco}, Numero de ramas: {len(self.ramas)}, Longitud de ramas: {self.ramas}")
                      
# 35 - ejecuta las indicaciones del caso de uso
mi_arbol = Arbol() 
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama(1)
mi_arbol.crecer_ramas(1)
mi_arbol.nueva_rama(1)
mi_arbol.nueva_rama(1)
mi_arbol.quitar_rama(2)
print(mi_arbol.info_arbol())


        

# %% [markdown]
# 
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:  
#     1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#     2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
#     3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
#     4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# 

# %% [markdown]
# Caso de uso:  
#     1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.  
#     2. Agregar 20 unidades de saldo de "Bob".  
#     3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".  
#     4. Retirar 50 unidades de saldo a "Alicia".
# 

# %%
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Método para retirar dinero del saldo del usuario
    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo: # si hay suficioente saldo se ejecuta la linea siguiente
            self.saldo -= cantidad # resta la cantidad al saldo
            print(f"{self.nombre} retiró {cantidad}€. Saldo restante: {self.saldo}€")
        else: #si no hay suficiente saldo se devuelve un mensaje de error
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}€.")

    # Método para transferir dinero DESDE otro usuario HACIA este usuario
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= otro_usuario.saldo: # si hay suficioente saldo en la cuenta del otro usuario, se ejecuta las lineas siguientes
            otro_usuario.saldo -= cantidad # se resta la cantidad al saldo del otr usuario
            self.saldo += cantidad # se añade la cantidad a la cuenta del usuario
            print(f"{otro_usuario.nombre} transfirió {cantidad}€ a {self.nombre}.") # resume la opreacion
            print(f"Saldo de {self.nombre}: {self.saldo}€, saldo de {otro_usuario.nombre}: {otro_usuario.saldo}€") # muestras los saldos respectivos
        else:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}€.") # informa que no hay suficiente saldo

    # Método para agregar dinero al saldo del usuario
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad # añade la cantidad al saldo
        print(f"{self.nombre} recibió {cantidad}€. Saldo actual: {self.saldo}€")


# caso de uso
alicia = UsuarioBanco("Alicia", 100, True) # se crea los 2 usuarios
bob = UsuarioBanco("Bob", 50, True)

print(f"Saldo inicial de {alicia.nombre}: {alicia.saldo}€") # muestra saldo inicial de cada uno
print(f"Saldo inicial de {bob.nombre}: {bob.saldo}€\n")

bob.agregar_dinero(20) # se agrega 20 unidades al saldo de Bob
alicia.transferir_dinero(bob, 80) # se transfiere 80 unidades desde bob hacia Alicia
alicia.retirar_dinero(50) # se quitan 50 unidades del saldo de Alicia

print(f"\nSaldo final de {alicia.nombre}: {alicia.saldo}€") # Imprimir el saldo final de cada usuario
print(f"Saldo final de {bob.nombre}: {bob.saldo}€")




# %% [markdown]
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
#     1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
#     2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
#     3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
#     4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
# 

# %%
import re


texto37 = "Juan tenía un gato. El gato dormía mucho. A veces Juan también dormía. Juan y el gato comían, dormían y jugaban. El gato maullaba." \
" Juan reía. Día tras día, Juan y su gato vivían momentos tranquilos juntos."


def contar_palabras(texto):
       texto_limpio = re.sub(r'[^\w\s]', '', texto.lower()) # Convierte todo a minúsculas y quita los signos de puntuación
       palabras = texto_limpio.split() #separa el texto en palabras
       recuento_palabras = {} # crea un diccionario vacio
       for palabra in palabras:
              if palabra in recuento_palabras:
                 recuento_palabras[palabra] += 1 # añade 1 a una palabra cada vez que se encuentra en el texto si ya existe en el diccionario
              else:
                    recuento_palabras[palabra] = 1 # crea la palabra en el diccionario
       return recuento_palabras


def reemplazar_palabras(texto,palabra_original,palabra_nueva):
     nuevo_texto = texto.replace(palabra_original,palabra_nueva) # reemplaza una palabra por otra
     return nuevo_texto

       
def eliminar_palabra(texto,palabra_eliminada):
     texto_troncado = texto.replace(palabra_eliminada,"") #reemplaza una palabra con valor blanco sin espacio
     return texto_troncado


def procesar_texto(texto, opcion, *args): #define la funcion con el texto la opcion de funcion y *arg segun cuantos argumentos hara falta)
    if opcion == "contar": # si la opcion es contar, se devuelve la funcion contar_palabras
        return contar_palabras(texto)
    elif opcion == "reemplazar":  # si la opcion es reemplazar, se devuelve la funcion reemplaza_palabras
        if len(args) != 2: # condicion que hay 2 argumentos, si no se cumple devuelve un mensaje de error
            return "Error: Se requieren dos argumentos para reemplazar (palabra_original, palabra_nueva)."
        return reemplazar_palabras(texto, args[0], args[1]) # si hay 2 argumentos la funcion se cumple
    elif opcion == "eliminar":  # si la opcion es eliminar, se devuelve la funcion eliminar_palabra
        if len(args) != 1: # si falta o hay mas de 1 argumento, lanza un mensaje de error
            return "Error: Se requiere una palabra para eliminar."
        return eliminar_palabra(texto, args[0]) # llama la funcion
    else:
        return "Opción no válida. Usa: 'contar', 'reemplazar' o 'eliminar'." #devuelve un mensaje de error si no se cumple ninguna de la condiciones anteriores
    



print(procesar_texto(texto37,"reemplazar","gato","raton")) # ejemplo cambiando la palabra gato por raton
print(procesar_texto(texto37,"eliminar", "tranquilos")) # elimina la palabra tranquilos si aparece el el texto
procesar_texto(texto37,"contar") # ejecuta la funcion contar

# %% [markdown]
# 
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# 

# %%
def momento_dia():  
    try:
        hora = int(input("Entra la hora (0-23): "))  # Solicita al usuario una hora y la convierte a entero
        if 7 <= hora < 15:  # Evalúa si la hora está entre 7 y 14 inclusive
            print("Día")  # Imprime "Día" si está en ese rango
        elif 15 <= hora < 23:  # Evalúa si la hora está entre 15 y 22 inclusive
            print("Tarde")  # Imprime "Tarde" si está en ese rango
        else:
            print("Noche")  # Imprime "Noche" si la hora es menor a 7 o mayor o igual a 23

    except ValueError:  # Captura el error si el usuario no introduce un número entero válido
        print("Número inválido. Introduce solo el número de la hora entre 0 y 23")  # Muestra mensaje de error al usuario
        return momento_dia()  # Llama recursivamente a la función para que el usuario intente de nuevo

momento_dia()


# %% [markdown]
# 
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
# 

# %%

def calificacion():  # Función que evalúa una nota numérica y muestra una categoría de desempeño
    try:
        nota = int(input("Entre la nota en formato numerico entre 0 y 100: "))  # Solicita al usuario una nota numérica y la convierte a entero
        if 89 < nota <= 100:  # Verifica si la nota está entre 90 y 100
            print("excelente")  # Muestra la categoría correspondiente
        elif 79 < nota < 89:  # Verifica si la nota está entre 80 y 88
            print("muy bien")
        elif 69 < nota < 79:  # Verifica si la nota está entre 70 y 78
            print("bien")
        elif 0 <= nota < 69:  # Verifica si la nota está entre 0 y 68
            print("insuficiente")
        else:
            print("El valor entrado es incorrecto. Entre de nuevo la nota en formato numerico entre 0 y 100: ")  # Mensaje si la nota está fuera del rango permitido
            calificacion()  # Llama recursivamente a la función para intentar de nuevo

    except ValueError:  # Captura errores si el usuario introduce texto u otro valor no numérico
        print("El valor entrado es incorrecto. Entre de nuevo la nota en formato numerico entre 0 y 100: ")  # Informa del error
        return calificacion()  # Vuelve a ejecutar la función para permitir otro intento


# %% [markdown]
# 
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
# 

# %%
import math # Importa la biblioteca para operaciones matemáticas con pi

def superficie(forma, medidas): 
    if forma == "rectangulo":
        if len(medidas) != 2: # condiciona que tengamos 2 argumentos para procedr al calculo de superficie
            print("se necesita en ancho y el largo del rectangulo para calcular su superficie")
        ancho, largo = medidas # Extrae las medidas
        return ancho * largo # calcula superficie
    elif forma == "circulo":
        if len(medidas) != 1: # Verificamos que se pase solo el radio
            print("se necesita en rayo del circulo para calcular su superficie")
        radio  = medidas[0]  # Obtenemos el radio correctamente (antes era una tupla)
        return math.pi * radio ** 2 # calcula la spuerficie del circulo
    elif forma == "triangulo":
        if len(medidas) != 2:
            print("se necesita la longitud de la base y la altura del triangulo para calcular su superficie")
        base, altura = medidas
        return round((base * altura)/2),2 # calcula la superficie del triangulo
    else:
        return "Forma no reconocida. Usa solo 'rectangulo', 'circulo' o 'triangulo'"  # Manejo de opción no válida
    
print(f"La superficie del rectangulo es de {superficie("rectangulo",(2,3))}")
print(f"la superficie del circulo es de {superficie("circulo",(2,))}")
print(f"la superficie del triangulo es de {superficie("triangulo",(4,2))}")
  


# %% [markdown]
# 
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
#     1. Solicita al usuario que ingrese el precio original de un artículo.
#     2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#     3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#     4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#     a cero). Por ejemplo, descuento de 15€.
#     5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#     6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.
# 

# %%
def monto_final():
    try:
        precio_original = float(input("Ingresa el precio original del articulo: ")) #Solicita al usuario que ingrese el precio original de un artículo.
        if precio_original <= 0:
            print("Error: El precio original debe ser un número positivo. Inténtalo de nuevo.")
            return monto_final()
        tiene_descuento = str(input("Indica por 'sí' o 'no' si tienes descuento: ")).strip().lower() #Pregunta al usuario si tiene un cupón de descuento quitando espacio y mayusculas
        if tiene_descuento not in ["sí", "si", "no"]:
            print("Error: Respuesta incorrecta. Solo se acepta 'sí' o 'no'. Inténtalo de nuevo.")
            return monto_final()
            valor_descuento = 0 # crea valor con zero
        if tiene_descuento == "sí" or tiene_descuento == "si": # condicion para acceptar respuestas con o sin tilde
            valor_descuento = float(input("Indique el valor del descuento: "))
            if valor_descuento <= 0 or precio_original < valor_descuento:
                print("el importe introducido no se puede aplicar, se aplicara el precio original")
                valor_descuento = 0
            precio_final = precio_original - valor_descuento
            print(f"El precio final es de {precio_final:.2f} €") #devuleve resultado con un maximo de 2 decimales
    except ValueError:
        print("el precio introducido es incorrecto, vuelve a introducir el precio original del articulo: ")
        


monto_final()


