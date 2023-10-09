![Tec de Monterrey](../../images/logotecmty.png)
# Tareas sin distracciones

![Rambo Tiberius Shwarzenegger](../../images/RTS_Portrait_Small.png)

Mi primo ***Solovino Cojo del Monte*** tiene que realizar 26 tareas (actividades), pero necesita enfocarse de lleno en cada una de ellas.  Las tareas están representadas por letras mayúsculas.  Su supervisor le ha dicho que, para tener una mejor productividad, deberá resolver las tareas de la siguiente manera:

- Si Solovino inicia una tarea, entonces debe trabajar en dicha tarea hasta resolverla.
- Esto quiere decir que no podrá iniciar una tarea si no ha terminado la tarea actual.
- Después de cambiar de tarea, Solovino no deberia regresar a una tarea anterior.
- Además, Solovino sólo puede trabajar en una tarea al día.  Cada día debe registrar en qué tarea trabajó.

Dadas estas instrucciones, su supervisor quiere saber si Solovino siguió sus instrucciones.

Por ejemplo, si la bitácora de tareas realizadas por Solovino registrara el siguiente orden: "DDBBCCCBBEZ", su supervisor podría darse cuenta que en el tercer día Solovino inició con la tarea B, que en el quinto día se distrajo e inició la tarea C, y que en el octavo día regresó a la tarea B.  Otros ejemplos en los que su supervisor podría sospechar serían: "BAB", "AABBCCDDEEBZZ" y "AAAAZAAAAA".

Si, por el contrario, Solovino terminara sus actividades en el siguiente orden: "FFGZZZY", su supervisor no tendrìa sospechas de distracción alguna por parte de Solovino.  Hay que tener en cuenta que Solovino no está obligado a terminar todas las tareas.  Otros ejemplos en los que su supervisor podría pensar que Solovino está totalmente enfocado, serían "BA", "AFFFCC" y "YYYYY".

Ayuda a Solovino a averiguar si su pervisor podría sospechar de desatención alguna.

### Entradas

- Recibirás una serie indefinida de líneas con el texto correspondiente a las letras de las actividades realizadas por Solovino.
  - Puedes estar seguro de que las cadenas no pasarán de 50 caracteres y que todos serán letras mayúsculas del alfabeto latino.
- La última línea será la cadena "0", lo que te indicará que ya no tienes casos por procesar

#### Ejemplo de entrada

```
ABA
DDBBCCCBBEZ
FFGZZZY
Z
AB
0
```

### Salidas

- Deberás especificar, para cada línea de caso, si Solovino se enfocó (***"Sí"***) o si se distrajo (***"No"***)

#### Ejemplo de salida

```
No
No
Sí
Sí
Sí
```

### Nota

- En los primeros dos casos, las salidas son "No", porque Solovino regresó a trabajar en una actividad en la que ya había trabajado y ya había cambiado de tarea.
- En los otros tres casos, las salidas son "Sí", porque Solovino no regresó a trabajar en tareas que ya habìa terminado.

### Consideraciones

Modifica el archivo `exercise.py` que se encuentra dentro de la carpeta `src` para que me ayudes a resolver mi problema.  Recuerda cumplir con los siguientes puntos:

- Tu código principal ***deberá estar dentro de la función*** `main()`
- ***Deberás modificar*** la función `estuve_enfocado(bitacora)` para que procese la bitácora e indique si Solovino se mantuvo enfocado o no.
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
- [ ] Conversiòn de tipos de datos con `map()`
- [x] Documentación

*Si tu programa no cumple con lo requerido, **se te descontarán puntos** de la calificación otorgada por el calificador.*
