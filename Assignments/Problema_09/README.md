![Tec de Monterrey](../../images/logotecmty.png)
# Canción de amor

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Resulta que mi primo **Solovino Cojo del Monte** está enamorado, y anda componiendo canciones de amor para su enamorada, conocida mundialmente como **La Vikinga**.  Las canciones que compone Solovino son cadenas compuestas por letras minúsculas del alfabeto latino.

Seamos honestos: Solovino es muy malo componiendo y sus canciones no llegan a tener mucho sentido.  Es por ello que la Vikinga le realiza preguntas sobre la canción.  Cada pregunta es acerca de un segmento de la misma, empezando en el *i*-ésimo carácter y terminando en el *d*-ésimo carácter.  La Vikinga, que es otra fanática de las cadenas lo que hace es tomar los caracteres del subsegmento y forma una nueva cadena con ellos, repitiendo cada carater de acuerdo a su posición en el alfabeto.  Es decir, la `a` la repite 1 vez cada que aparece, la `b` la repite dos veces cada que aparece, y así subsecuentemente.

Como ambos están en estos momentos superacaramelados, viéndose con ojos de perro suplicante porque, bueno, ambos son perros, te han pedido que les ayudes a determinar la longitud de las palabras que formará el algoritmo de la Vikinga.

### Entradas

- La primera línea de entrada será el número entero positivo *q*, que representa el número de preguntas que la Vikinga hará sobre la canción de Solovino.
- La segunda línea será la cadena *s*, que representa la canción de Solovino.
  - Puedes estar seguro de que la canción estará compuesta de solo caracteres latinos en minúsculas y que no tendrá espacios.
- A partir de ahí, recibirás *q* líneas conteniendo los límites *izquierdo* y *derecho* del segmento a analizar.
  - Puedes estar seguro de que la posición de la izquierda siempre será menor a la de la derecha.
  - Puedes estar seguro de que las posiciones solicitadas siempre serán parte de la cadena.

#### Ejemplo de entrada

```
3
abacaba
1 3
2 5
1 7
```

### Salidas

- Deberás mostrar, para cada pregunta de la Vikinga, la longitud final de la nueva cadena (un número entero positivo), formada de acuerdo a sus especificaciones.

#### Ejemplo de salida

```
4
7
11
```

### Nota

- En el primer caso, nos dice la pregunta que quiere usar los caracteres del 1 al 3 de la cadena.  Dada la cadena `abacaba`, la subcadena<sub>(1,3)</sub> sería `aba`. El caracter `a` se repetirá una vez cada que aparezca, porque es el primer caracter del alfabeto latino, mientras que el caracter `b` se repetirá dos veces, por ser el segundo caracter del alfabeto latino.  Esto nos da la cadena `abba` que, como puedes ver, está formada por ***4*** caracteres.
- Recuerda que existen funciones en Python como `ord()`, que me devuelve el valor ASCII de un caracter y `chr()`, que me devuelve el valor caracter de un código ASCII.
  - Recuerda también que el valor ASCII de `a` es `97`.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `genera_palabra(subcadena)` para que genere la nueva palabra de acuerdo a las especificaciones de la Vikinga.
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
- [x] Segmentación (Slices)
- [x] Conversión de tipos de datos
- [x] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
