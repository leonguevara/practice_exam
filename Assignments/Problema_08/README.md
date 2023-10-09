![Tec de Monterrey](../../images/logotecmty.png)
# Detección de espías

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Hemos encontrado que, entre algunos de nuestros equipos SWAT perrunos, tenemos espías.  Como estos espías no dicen `miau`, resulta un tanto cuanto difícil detectarlos.  Sin embargo, hemos encontrado que, entre nuestros equipos, todos los miembros vibran a la misma frecuencia... excepto uno.

Tu misión es encontrar al espía en cada uno de los equipos que te serán enviados, y señalarlo.

### Entradas

- Un número no determinado de líneas, cada una de ellas representando a un equipo SWAT perruno.
  - Cada línea consiste de tres (3) o más números enteros, separados por espacios en blanco, que representan las vibraciones de cada uno de los miembros del equipo.
  - Puedes estar seguro de que **siempre** habrá un espía.
- Una última línea con un 0, indicando que ya no tienes más casos por procesar.

#### Ejemplo de entrada

```
11 13 11 11
1 4 4 4 4
3 3 3 3 10 3 3 3 3 3
20 20 10
0
```

### Salidas

- Para cada caso, deberás enviar la posición del elemento espía dentro del equipo.

#### Ejemplo de salida

```
2
1
5
3
```

### Nota

- Como puedes ver en el primer caso, todos los elementos del equipo vibran a 11, excepto el segundo que vibra a 13.  Como es el segundo elemento del equipo, señalamos que está en la posición 2.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `encuentra_el_espía(equipo)` para que dado el equipo, encuentre y devuelva la posición del espía.
- Las entradas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás decirle cosas como `"Dame tu nombre"`, o `"longitud del lado"`.  Si envías mensajes al usuario, tu solución ***será incorrecta***.
- Las salidas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás agregar etiquetas como `"Resultado:"` o `"Caso 1:"`.  Si lo haces, tu solución ***será incorrecta***.
- Deberás procesar ***todas y cada una de tus entradas antes de motrsar las salidas.***  Para ello, deberás usar ***una lista*** que te permita guardar los resultados procesados.

#### Elementos que debe cubrir tu solución:

- [ ] Operaciones aritméticas
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
