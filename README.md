# Introducción

El propósito de este proyecto es hacer un videojuego con ``Python``. 

# Stack tecnológico

- ``Python`` + 🔗 [`Pygame Ce`](https://pypi.org/project/pygame-ce/)

# Conocimientos generales

## Parámetros Opcionales

Para definir los parámetros opcionales de una función debes establecer un valor por defecto:

```python
import pygame

def pydle_screen(width=800, height=600):
    return pygame.display.set_mode((width, height))
```

Los argumentos opcionales **siempre** deben de ir al final.

```python
import pygame

def pydle_screen(width, height=600):
    return pygame.display.set_mode((width, height))
```

## Imprimir por consola

En ``Python`` se utiliza la instrucción `print` para imprimir mensajes por consola:

```python
    print("Este es mi mensaje")
```

En caso de querer imprimir una variable concatenada a un texto, debe de preceder ``f`` ante 

```python
    usuario="Usuario"
    print(f"Este es mi saludo para {usuario}")
```

## Imports

Para hacer los imports en ``Python``, se utiliza la instrucción

```python
import package
```

Por ejemplo:

```python

# actions.py

def say_hello():
    print("Hello world!")


# main.py
import core.game_scripts.actions

core.game_scripts.actions.say_hello()
```

☝️Incluso puedes utilizar aliases


También puedes utilizar aliases para los imports:

```python

# actions.py

def say_hello():
    print("Hello world!")


# main.py
import core.game_scripts.actions as pydle_actions

pydle_actions.say_hello()
```

## Importar funciones desde archivos python

Se parece mucho al punto anterior:

```python

# actions.py

def say_hello():
    print("Hello world!")


# main.py
from core.game_scripts.actions import say_hello

say_hello()
```

## Errores típicos

### ``:`` vs `,`

Para los que venimos del frontend es bastante normal confundirnos en este punto, pero en ``python`` **no es tan común** utilizar `,`. Lo correcto generalmente
es utilizar `:`.

❌ Ejemplo de mal uso:

````python
print(f"event_type, {event_type}")
````

✅ Ejemplo de buen uso:

````python
print(f"event_type: {event_type}")
````


### `kebab_case` vs ``camelCase``

**No es correcto** utilizar en python el formato ``camelCase``:

❌ Ejemplo de mal uso:

````python
print(f"eventType, {eventType}")
````

✅ Ejemplo de buen uso:

````python
print(f"event_type: {event_type}")
````
 
# Módulos interesantes de Python

## inspect

Este módulo nos permite acceder a funciones útiles que nos dan información sobre variables, funciones, objetos...

### getmemvers 

> 🔗 https://docs.python.org/3/library/inspect.html#inspect.getmembers

### Caso de uso

Imagina que queremos comprobar si los elementos importados de un módulo son una función.

Gracias a ``inspect`` y su función ``getmembers`` podemos comprobarlo.

👉 La definición de ``getmembers`` dice que:

> _Return all members of an object as (name, value) pairs sorted by name. Optionally, only return members that satisfy a given predicate_

Así que espera **dos parámetros**:
1. El módulo completo que va a inspeccionar
2. Lo que se quiere comprobar (llamado _predicado_ por la propia función). Este parámetro es opcional.

El código sería:

```python
# main.py

import inspect
import core.game_scripts.actions as game_actions

[(name, value)]=inspect.getmembers(game_actions, inspect.isfunction)

print(f"module value: {name}")
```

Esta línea de código 👉 ``inspect.getmembers(game_actions, inspect.isfunction)`` nos devuelve un array con un item que se divide en dos valores:
el **nombre de la función** y **la función en sí**.

> ☝️De hecho, si vemos la consola, veremos que nos imprime el nombre de aquellos elementos que cumplan la condición de ser funciones.


❌ Mal uso del ``getmembers``

```python

# main.py

import inspect
import core.game_scripts.actions as game_actions

[name, value]=inspect.getmembers(game_actions, inspect.isfunction)

print(f"module value: {name}")
```

Nos dará el error ↓

> ```bash
> Traceback (most recent call last):
> File "/Users/lidiasanchez/Python2026/02-pydle-game/start.py", line 5, in <module>
> [name, value]=inspect.getmembers(game_actions, inspect.isfunction)
> ValueError: not enough values to unpack (expected 2, got 1)
> ```

## functools

Este módulo nos permite llamar o retornar otras funciones.

### partial

> 🔗https://docs.python.org/es/3/library/functools.html#functools.partial


### Caso de uso

Aunque las acciones generales del juego (como capturar el movimiento del personaje, mostrar textos, generar batallas, etc) se realizan **dentro** del loop del juego (es decir, una vez inicializado este), hay otras que
necesitamos lanzar **antes** de iniciarlo. Una de ellas es, por ejemplo, **definir la pantalla de juego**.

Tenemos dos ficheros para hacer este proceso: ``core.screen`` y ``core.pydle_system.prepare``.

El fichero ``core.screen`` se encarga tanto de definir como de inicializar la pantalla donde se pintarán los elementos del juego.
El fichero ``core.pydle_system.prepare``, de recibir los elementos que deben estar listos **antes** de inicializar el loop mediante la función
``core.pydle_system.run``.

Una de las cosas a definir es **el tamaño de la pantalla** (su ancho y su alto):

````python
# screen.py

from pygame import display

_screen = display

def screen_size(width, height):
    _screen.set_mode((width, height))
````

Para poder pasar los parámetros a la función, deberíamos hacerlo desde la función de ``prepare``:

```python

import core.screen as screen

def prepare():
    screen.screen_size(800, 600)
```

Pero **no queremos hacer esto**. Porque sino, por cada preparación que tuviéramos que hacer, tendríamos que añadirlo manualmente en esta función ``prepare``.
Para eso tenemos ``functools.partial``:

> 👉 _Retorna un nuevo partial object que cuando sea llamado se comportará como func llamado con los argumentos posicionales args y los argumentos de palabras clave keywords_

> ✍🏻 Un ``partial`` en python es una función creada a partir de otra función existente, pero con uno o más argumentos prellenados o fijos.
> Esos ``partial`` se crean a partir de la función que estamos estudiando (`functool.partial`).

Así que para que la función ``pydle_system.prepare`` pueda lanzar la función `screen_width`:

```python

# start.py

import functools
import core.pydle_system as pydle_system

from core.screen import screen_size

pydle_system.prepare([functools.partial(screen_size, 800, 600)])
```

````python
# pydle_system.py

from inspect import isfunction

def prepare(scripts):
    for script in scripts:
        if isfunction(script):
            script()
````