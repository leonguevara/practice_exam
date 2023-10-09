![Tec de Monterrey](../../images/logotecmty.png)
# Bebidas

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Hola.  No estás para saberlo, ni yo para contarlo, pero tengo un pequeño problema estomacal que me obliga a tomar jugo de ciruela.  De hecho, mi refrigerador está lleno de envases que tienen, todos, alguna proporción de jugo de ciruela.

Habiendo *n* frascos en mi regrigerador, el volumen de la fracción de jugo de ciruela en la *x*-ava bebida es de *p<sub>x</sub>* porciento.

He decidido hacer una mezcla de todas las bebidas que están en mi refrigerador, y quiero saber cuál será la proporción final de jugo de ciruela en mi mezcla.  Si la proporción es **superior al 50%**, entonces mi elixir funcionará en mi pancita.  De lo contrario, no me hará efecto alguno.

Necesito que me ayudes a calcular esta proporción.  Prepara un programa que lea, en una lìnea, las proporciones de *n* botellas, y calcule la proporción final de la mezcla.  Además, deberá decir si la mezcla funcionará o no.

### Entradas

- Recibirás una serie de líneas, cada una con *n* números enteros, separados por espacios en blanco.
  - Puedes estar seguro de que en cada línea de entrada no habrá más de 100 elementos.
  - Puedes estar seguro de que cada elemento será un número entre 0 y 100 (inclusive).
- La última entrada será una línea con el número 0.  Cuando la recibas, sabrás que has terminado de recibir entradas y no deberás procesar dicha línea.

#### Ejemplo de entrada

```
50 50 100
0 25 50 75
0 1 8
96 89 93 95 70
0
```

### Salidas
- Para cada caso de prueba, deberás mostrar en una sola línea, la proporción final de la mezcla, seguida de un guión y de la palabra *Sí* o de la palabra *No*, dependiendo de si el porcentaje de la mezcla es superior al 50%.

#### Ejemplo de salida

```
66.67 - Sí
37.50 - No
3.00 - No
88.60 - Sí
```

### Nota
La respuesta al primer caso de prueba es `"66.67 - Sí"`.  La suma de los porcentajes de cada botella es de 200 (50 + 50 + 100) y, como fueron tres botellas, el promedio es de 66.67 (redondeado a dos decimales).  Como la proporción es superior al 50%, se indica que la mezcla **Sí** funcionará.

La respuesta al segundo caso de prueba es `"37.50 - No"`.  La suma de los porcentajes de cada botella es de 150 (0 + 25 + 50 + 75) y, como fueron tres botellas, el promedio es de 66.67 (redondeado a dos decimales).  Como la proporción no es superior al 50%, se indica que la mezcla **No** funcionará.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `calcula_proporcion(lista_de_proporciones)` para que haga el cálculo de la proporción de jugo de ciruela en la mezcla final.
- Las entradas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás decirle cosas como `"Dame las proporciones de las botellas"`, o `"Porcentaje de jugo en las botellas"`.  Si envías mensajes al usuario, tu solución ***será incorrecta***.
- Las salidas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás agregar etiquetas como `"Proporciòn final:"` o `"Caso 1:"`.  Si lo haces, tu solución ***será incorrecta***.
- Deberás procesar ***todas y cada una de tus entradas antes de motrsar las salidas.***  Para ello, deberás usar ***una lista*** que te permita guardar los resultados procesados.

#### Elementos que debe cubrir tu solución:

- [x] Operaciones aritméticas
- [X] Operaciones relacionales y booleanas
- [x] Entrada de datos por entrada estándar (`consola`)
- [x] Salida de datos por salida estándar (`consola`)
- [x] Funciones predefinidas
- [x] Toma de decisiones
- [x] Cadenas con formato
- [x] Funciones
- [x] Ciclos
- [x] Manejo de cadenas
- [x] Listas
- [ ] Segmentación (Slices)
- [ ] Conversión de tipos de datos
- [x] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
