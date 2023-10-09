![Tec de Monterrey](../../images/logotecmty.png)
# Equipos alfabéticas

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Estamos encontrando maneras de formar a un conjunto de perros en equipo SWAT, cada uno indicado con una letra minúscula del alfabeto latino.  La idea es que siempre esté presente el perro señalado con la letra `"a"`.  A él se van a ir sumando el resto de sus compañeros, pero se van a formar con las siguientes características:

- Una vez estándo el perro `a` en formación, el perro `b` se posicionará a su izquierda, o a su derecha, pero siempre junto a `a`.
- El perro `c` se formará a la derecha o a la izquierda de la formación ya establecida.  Lo mismo pasará con el perro `d`, y así sucesivamente.
- Es decir, para cada paso, y si pensamos en cadenas, a `cadena <- cadena + carácter` o `cadena <- carácter + cadena`.

Los equipos formados de esta manera, podrán considerarse alfabéticos.

Por ejemplo, los equipos siguientes son alfabéticos: `"a"`, `"ba"`, `"ab"`, `"bac"`, `"ihfcbadeg"`.  Los siguientes equipos **no son** alfabéticos: '"z"', `"aa"`, `"ca"`, `"acb"`. `"xyz"`y `"ddcba"`.

Tu tarea conistirá en construir un programa que te permita identificar si un equipo es alfabético o no.

### Entradas

- Un número no determinado de líneas, cada una de ellas representando a un equipo SWAT perruno en formación.
  - Cada línea consiste de una cadena de caracteres representando a los perros que conforman el equipo.
  - Puedes estar seguro de que la cadena siempre tendrá por lo menos un carácter y un máximo de 26 caracteres.
- Una última línea con un 0, indicando que ya no tienes más casos por procesar.

#### Ejemplo de entrada

```
a
ba
ab
bac
ihfcbadeg
z
aa
ca
acb
xyz
ddcba
0
```

### Salidas

- Para cada caso, deberás mostrar si el equipo está en formación alfabética (mostrando en pantalla `"Sí"`) o no (mostrando en pantalla `"No"`).

#### Ejemplo de salida

```
Sí
Sí
Sí
Sí
Sí
No
No
No
No
No
No
```

### Nota

- Como puedes ver en los primeros cinco casos el elemento `a` está presente y el resto de los integrantes del equipo, en caso de haber màs, se fueron integrando uno por uno a alguno de los costados.
- En los otros casos, puedes ver que el resultado es **No** porque:
  - No incluyen al carácter `a`.
  - Los caracteres se repiten.
  - Falta algún caracter que debió ser incluido.
  - No fueron ordenados correctamente, etc.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `es_alfabetico(equipo)` para que dado el equipo, encuentre si es alfabético o no.
- Las entradas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás decirle cosas como `"Dame tu nombre"`, o `"longitud del lado"`.  Si envías mensajes al usuario, tu solución ***será incorrecta***.
- Las salidas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás agregar etiquetas como `"Resultado:"` o `"Caso 1:"`.  Si lo haces, tu solución ***será incorrecta***.
- Deberás procesar ***todas y cada una de tus entradas antes de motrsar las salidas.***  Para ello, deberás usar ***una lista*** que te permita guardar los resultados procesados.

#### Elementos que debe cubrir tu solución:

- [x] Operaciones aritméticas
- [x] Operaciones relacionales y booleanas
- [x] Entrada de datos por entrada estándar (`consola`)
- [x] Salida de datos por salida estándar (`consola`)
- [x] Funciones predefinidas
- [x] Toma de decisiones
- [ ] Cadenas con formato
- [x] Funciones
- [x] Ciclos
- [x] Manejo de cadenas
- [x] Listas
- [ ] Segmentación (Slices)
- [x] Conversión de tipos de datos
- [ ] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
