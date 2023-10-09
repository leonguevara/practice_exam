![Tec de Monterrey](../../images/logotecmty.png)
# Monedas exactas

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Hola.  Tengo que realizar algunos pagos en efectivo, monendas, y necesito que me ayudes a dar las monedas exactas.  Tengo monedas de 1 y de 2 pesos para cubrir el monto a pagar. Sin embargo, no todo es tan fácil conmigo.  Resulta que me gustan mucho mis monedas y, si voy a desprenderme de ellas, quiero que sea en la misma proporción.  Es decir, no quiero pagar con más monedas de un tipo que del otro.

Es por ello que, tratando de minimizar la diferencia entre la cuenta de monedas de 1 peso y la cuenta de monedas de 2 pesos, necesito que generes un programa que me ayude a determinar dos números enteros no negativos *m<sub>1</sub>* y *m<sub>2</sub>* que sean el número de monedas de 1 y de 2 pesos, respectivamente, de forma tal que me ayuden a pagar de forma exacta el valor del *monto*.  Es decir:

> *m<sub>1</sub>* + 2 · *m<sub>2</sub>* = *monto*

El valor absoluto de la diferencia entre ambas cuentas de monedas *m<sub>1</sub>* y *m<sub>2</sub>* debe ser lo más pequeño posible (debes minimizar `|`m<sub>1</sub> - m<sub>2</sub>`|`).

### Entradas

- La primera línea contiene un entero positivo *t* (1 <= t <= 10<sup>4</sup>) que representa número de casos, o tests, que deberás procesar.  Luego, siguen *t* casos.
- Cada caso consiste de una línea, cada una con un número *n* entero positivo (1 <= n <= 10<sup>9</sup>), representando el monto a pagar, en pesos.

#### Ejemplo de entrada

```
6
1000
30
1
32
1000000000
5
```

### Salidas
- Para cada caso de prueba, deberás mostrar en una sola línea, separados por un espacio en blanco, el total de monedas de 1 peso y el total de monedas de 2 pesos que deberàs usar para cubrir el monto de dicha línea.

#### Ejemplo de salida

```
334 333
10 10
1 0
10 11
333333334 333333333
1 2
```

### Nota
La respuesta al primer caso de prueba es `"334 333"`.  La suma de los valores nominales de las monedas es 334 · 1 + 333 · 2 = 334 + 666 = 1000, donde `|`334 - 333`|` = 1.  Uno no podría obtener un mejor resultado, porque si `|`334 - 333`|` = 0, entonces *m<sub>1</sub>* = *m<sub>2</sub>*, pero esto implicaría que *m<sub>1</sub>* no fuera un entero.

La respuesta al segundo caso de prueba es `"10 10"`.  La suma de los valores nominales de las monedas es 10 · 1 + 10 · 2 = 10 + 20 = 30, y `|`10 - 10`|` = 0, donde no hay número que tenga un valor abosoluto menor que 0.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `divide_monedas(monto)` para que haga la división del monto en el nùmero de monedas correcto.  Recuerda que una función puede regresar varios valores a la vez, si los separmos por comas (`return a, b, c`) y si los regresamos al mismo número de variables `x y z = mi_funcion(algo)`.
- Las entradas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás decirle cosas como `"Dame el número de casos"`, o `"Monto a procesar"`.  Si envías mensajes al usuario, tu solución ***será incorrecta***.
- Las salidas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás agregar etiquetas como `"Monedas de 1 peso:"` o `"Monedas de 2 pesos:"`.  Si lo haces, tu solución ***será incorrecta***.
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
- [ ] Conversión de tipos de datos
- [x] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
