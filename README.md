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

> 🔗 https://docs.python.org/3.9/library/inspect.html#inspect.getmembers

Este módulo nos permite acceder a funciones útiles que nos dan información sobre variables, funciones, objetos...

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
