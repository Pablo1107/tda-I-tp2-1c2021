# Nota Entrega: sin nota

 - Parte 1: 9
 - Parte 2: Reentrega
 - Parte 3: 10

*Corrector: Ernesto*

# Comentarios sobre las correcciones

## Comentarios Parte 1
 - Falta el nombre del grupo en la carátula.
 - Correcta la solución por fuerza bruta. Brindan pseudo-código para mostrar el procedimiento, el pseudo-código es una mezcla de python con pseudo-código, no entiendo bien el por qué.
 - Correcta la complejidad temporal y espacial.
 - Se usa "mientras 0 <= j" pero nunca se modifica j, es un loop infinito (-1)
 - Pseudocódigo correcto más haya de lo mencionado anteriormente (parece un olvido ya que en otro loop si modifica i)
 - Excelente la explicación del teorema maestro y por qué la complejidad es O(n*logn).
 - Buena la explicación de la complejidad de por el método de desenrrollado
 - Correcta la complejidad espacial del problema
 - Buena explicación del ejemplo (utilizan el problema que se brinda como ejemplo en los requerimientos), ayudandose con una árbol y pseudocódigo.

## Comentarios Parte 2
 - Utilizan Bellman-ford para la solución.
 - En el algoritmo explican: " se verifica si la distancia guardada para
 - llegar al vértice de origen de la arista sumado al peso de la arista es menor a la guardada para
 - llegar al vértice destino de la arista." Pero no dicen qué se hace con esta verificación. (-1)
 - Más adelante está explicado correctamente con el pseudocódigo.
 - El pseudocódigo está bien, pero para encontrar el ciclo negativo se fijan el primer nodo que le baja la distancia, y éste no necesariamente tiene que pertenecer al ciclo negativo, puede ser afectado por este, y se genera un loop infinito buscando el ciclo. (-2)
 - Muestran correctamente las estructuras que utilizan.
 - Para la explicación de la relación de recurrencia escriben: "predecesores[Ni] es el conjunto de los nodos adyacentes a Ni" no serían los adyacentes, serían los nodos que tienen una arista con destino Ni. (-2) Con esto en mente, el resto está bien. Una relación de recurrencia bastante engorrosa.
 - La complejidad temporal es correcta y la espacial igual.


## Comentarios programa
El código tiene el mismo error que se mencionaba:

Con
```
A
E,F,2
A,B,1
B,C,1
C,D,1
D,E,1
D,G,1
G,H,1
H,B,-20
```

Se queda en un loop infinito

Además en el código se ponen complejidades que no son correctas. Para la búsqueda del ciclo se recorre a lo sumo O(V) veces, no importan las cantidades de aristas. Pusieron O(V*E)

## Comentarios Parte 3
 - Correcta explicación de los 3 tipos de soluciones.
 - Buena justificación de por qué (en la mayoría de los casos) conviene una menor complejidad temporal a una espacial
