![Tec de Monterrey](../../images/logotecmty.png)
# Odio los Tres

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Odios los tres.  Desprecio los números enteros que son múltiplos de tres, así como aquellos que terminan en 3.  Si cumplen con ambas condiciones, los odio el doble.

Quiero comenzar a escribir todos los números enteros positivos (mayores que 0) que sí me agradan: 1, 2, 4, 5, 7, 8, 10, 11, 14, 16,... etcétera hasta llegar al *k*-ésimo elemento.

### Entradas

- La primera línea de entrada tendrá un número *T*, que me indicará el número de casos a procesar.
  - Puedes estar seguro que *T* estará entre 1 y 100.
- Después vendràn *T* lìneas, cada una de ellas con un número entero *k*&larr;
  - Puedes estar seguro que *k* estará siempre entre 1 y 1000.

#### Ejemplo de entrada

```
10
1
2
3
4
5
6
7
8
9
1000
```

### Salidas

- Para cada caso de prueba, deberás mostrar en pantalla el *k*-ésimo elemento de la serie de números que sí me agradan.
  - Si *k* es 1, quiero el primero elemento, si *k* es 5, quiero el quinto elemento.

#### Ejemplo de salida

```
1
2
4
5
7
8
10
11
14
1666
```

### Nota

- En el primer caso, nos están pidiendo el elemento en la primera posición, que es 1.
- En el tercer caso, nos están pidiendo el elemento en la tercera posición, que es 4.
- En el último caso, nos están pidiendo el elemento en la posición número 1000, que es 1666.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `genera_serie()` para que genere la serie de números enteros que sí me agradan.
- Las entradas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás decirle cosas como `"Dame tu nombre"`, o `"longitud del lado"`.  Si envías mensajes al usuario, tu solución ***será incorrecta***.
- Las salidas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás agregar etiquetas como `"Resultado:"` o `"Caso 1:"`.  Si lo haces, tu solución ***será incorrecta***.
- Deberás procesar ***todas y cada una de tus entradas antes de motrsar las salidas.***  Para ello, deberás usar ***una lista*** que te permita guardar los resultados procesados.

#### Elementos que debe cubrir tu solución:

- [x] Operaciones aritméticas
- [x] Operaciones relacionales y booleanas
- [x] Entrada de datos por entrada estándar (`consola`)
- [x] Salida de datos por salida estándar (`consola`)
- [ ] Funciones predefinidas
- [x] Toma de decisiones
- [ ] Cadenas con formato
- [x] Funciones
- [x] Ciclos
- [x] Manejo de cadenas
- [x] Listas
- [ ] Segmentación (Slices)
- [x] Conversión de tipos de datos
- [x] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
