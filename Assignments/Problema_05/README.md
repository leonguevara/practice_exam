![Tec de Monterrey](../../images/logotecmty.png)
# Eliminatorias justas

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Nos han invitado a presenciar un torneo de eliminatoria directa, también conocidos como Playoff.  En este torneo, cuatro jugadores se enfrentan en eliminación directa: semifinales y final.  El primer jugador se enfrenta al segundo, y el tercer jugador se enfrenta al cuarto.  Los ganadores de ambos encuntros se enfrentan en la final.

Se sabe que en un enfrentamiento entre dos jugadores, ganará el que mayor habilidad tenga, la habilidad del jugador *i* está dada por el valor *s<sub>i</sub>* del vector de habilidades *s*.

Nos han pedido construir un programa que dados una serie de vectores, cada uno de cuatro elementos, podamos definir si la eliminatoria sería justa.  La eliminatoria sería justa si los dos elementos con mayor habilidad se enfrentan en la final.

### Entradas

- Una serie de vectores de cuatro elementos cada uno, estando los elementos separados por espacios en blanco.
  - Puedes estar seguro qe cada uno de los elementos será un valor entero entre 1 y 100, inclusive.
  - También puedes estar seguro de que, en cada línea, ninguno de los valores se repetirá (no habrá dos o más jugadores con el mismo nivel de habiidades).
- Una última línea cuyo único elemento será el 0, para indicarte que ya no tienes más vectores por procesar.

#### Ejemplo de entrada

```
3 7 9 5
4 5 6 9
5 3 8 1
6 5 3 2
0
```

### Salidas

- Deberás mostrar, para cada caso, si el torneo puede ser considerado justo (***"Sí"***) o injusto (***"No"***)

#### Ejemplo de salida

```
Sí
No
Sí
No
```

### Nota

- En el primer caso, podemos decir que el torneo sí es justo, porque llegarán a la final los elementos con mayor habilidad: 7 y 9.
- En el segundo caso, podemos decir que el torneo no es justo, porque llegaràn a la final los elementos con habilidades 5 y 9, pero habrá quedado fuera el elemento con habilidad 6

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `es_torneo_justo(torneo)` para que haga el cálculo correspondiente al problema.
- Las entradas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás decirle cosas como `"Dame tu nombre"`, o `"longitud del lado"`.  Si envías mensajes al usuario, tu solución ***será incorrecta***.
- Las salidas de tu programa ***no deberán incluir mensajes al usuario***.  Es decir, no deberás agregar etiquetas como `"Resultado:"` o `"Caso 1:"`.  Si lo haces, tu solución ***será incorrecta***.
- Deberás procesar ***todas y cada una de tus entradas antes de motrsar las salidas.***  Para ello, deberás usar ***una lista*** que te permita guardar los resultados procesados.

#### Elementos que debe cubrir tu solución:

- [ ] Operaciones aritméticas
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
