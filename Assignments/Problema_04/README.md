![Tec de Monterrey](../../images/logotecmty.png)
# El buen arreglo

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Como puedes haber imaginado a través de toda la serie de ejercicios, soy un obsesionado con las matemáticas.  En esta ocasión, necesito que me ayudes a identificar buenos arreglos.  Un arreglo (o matriz unidimensional) es un conjunto de números, y podemos considerarlo como un buen arreglo si la media (el promedio) de los elementos de dicho arreglo es igual a 1.

Sin embargo, como yo tengo mucho apego a mis cosas y no quier desprenderme de ninguno de mis arreglos, necesito que me digas cuál es la cantidad mínima de elementos que debo agregar a cada uno de ellos para convertirlo en un arreglo bueno en caso de que no lo sea.  La única restricción que pongo es que los elementos a agregar **NO DEBEN SER NEGATIVOS**.  Es importante hacer notar que el promedio o media del arreglo **no se redondea**.

### Entradas

- La primera línea que recibirás es un número entero *T*, que representa el número de arreglos a procesar.
- Después recibirás *T* líneas, cada una con un conjunto de nùmeros enteros separados por espacios en blanco, representando cada línea el arreglo a validar.
  - Como podrás ver en el ejemplo abajo, los arreglos pueden tener distintas dimensiones, pero puedes estar seguro de que por lo menos tendrán un elemento y no pasarán de 50 elementos.
  - Los elementos del arreglo pueden ser positivos, negativos o ceros, y puedes estar seguro de que sus valores estarán entre -10<sup>4</sup> y 10<sup>4</sup>.

#### Ejemplo de entrada

```
4
1 1 1
1 2
8 4 6 2
-2
```

### Salidas

- Para cada arreglo, deberás mostrar el número de elementos a agregar para convertirlo en un buen arrego, un caso por lìnea.

#### Ejemplo de salida

```
0
1
16
1
```

### Nota

- En el primer caso, se agregan 0 elementos ya que la media del arreglo es 1: no hay necesidad de agregar elementos.
- En el segundo caso, se agrega 1 elemento (de valor 0).  Esto es debido a que la suma de los elementos es 3, y tenemos 2 elementos.  Si agregamos un elemento  con valor 0, tendremos la misma suma, pero con 3 elementos, y ahora sí nuestra media será de 1.
- En el tercer caso, se agregan 16 elementos (de valor 0).  Esto es debido a que la suma de los elementos es 20, y tenemos 4 elementos.  Dado que no podemos agregar elementos negativos, tenemos que agregar 16 elementos de valor 0 para que la suma siga siendo 20 y tener ahora 20 elementos para que la media sea de 1.
- En el cuarto caso, se arega 1 elemento (de valor 4).  Esto es debido a que la suma de elementos del arreglo es de -2 y sólo tenemos un elemento.  Si agregamos un elemento con valor 4, la suma ahora será de 2 y tendremos 2 elementos, por lo que la media será de 1.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `calcula_elementos(arreglo)` para que haga el cálculo correspondiente al problema.
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
