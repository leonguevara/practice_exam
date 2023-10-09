![Tec de Monterrey](../../images/logotecmty.png)
# Plaza del pueblo

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Tenemos trabajo.  Nos han contratado para poner la plancha a varias plazas en las localidades aledañas a Tejoringo.  Estas plazas tienen un área de *m* x *n* metros.  Para poder cubrir esta área, nosotros podemos conseguir piezas de concreto cuadradas, con dimensiones de *a* x *a* (repito: son cuadradas).  Las dimensiones de las piezas llegan a variar, dependiendo de la localidad.

Necesitas construir un programa que lea, en una sola lìnea, las dimensiones de la plaza y el largo del lado de las piezas a usar, para determinar cuántas piezas necesitamos ocupar.  Por cierto, no podemos romper las piezas.  Si es necesario, cubriremos más terreno del necesario, pero no podemos romper las piezas.

### Entradas

- Una serie no definida de líneas, cada una con tres nùmeros enteros: *m*, *n* y *a*.
  - Puedes estar seguro de que los números que recibas estarán entre 1 y 10<sup>9</sup>, inclusive.
  - Puedes estar seguro de que recibirás 3 números por línea de caso.
- Una última línea que será compuesta de un solo número, el 0, la que te indicará que ya no hay más lìneas por procesar

#### Ejemplo de entrada

```
6 6 4
12 13 4
2 3 4
2 1 2
222 332 5
0
```

### Salidas

- El número de piezas necesarios para cubrir cada área, una línea por caso.

#### Ejemplo de salida

```
4
12
1
1
3015
```

### Nota

- En el primer caso, el área a cubrir es de 6 x 6, mientras que las piezas tienen un largo de 4 por lado.  4 es menor que 6, por lo que se requieren dos piezas de 4 para cubrir el 6.  Esto es lo mismo tanto para el largo como para el ancho, por lo que necesitamos 2 x 2 piezas; es decir: 4 piezas.
- En el tercer caso, el área a cubrir es de 2 x 3, mientras que las piezas tienen un largo de 4 por lado.  4 es mayor que 2, y también es mayor que 3, por lo que se requeire de 1 pieza por lado, por lo que necesitamos 1 x 1 piezas; es decir: 1 pieza.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `calcula_piezas(largo, ancho, lado)` para que haga el cálculo de cuántas piezas necesitas para cubrir determinada área.
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
- [ ] Conversión de tipos de datos
- [x] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
