# Errores comunes

## Conceptos

### ``Frames per second`` (fps)

- Indica **la cantidad de imágenes por segundos** que se deben renderizar. 
☝️ Es importante fijarlos (ya sea a 60, 120, 180...) 
porque sino se utilizará **toda la potencia de la CPU** y tratará de renderizar **tantas imágenes como pueda**.
Para que el juego funcione igual en todos los pcs, es recomendable fijarlo (al menos) a 60.

- Esta acción solo es necesaria hacerla **1 vez**. 

## Video system not initialized

```bash
pygame.error: video system not initialized
```

☝️ Esto ocurre porque no hemos incluído la instrucción ``pygame.init()``.

Es tan fácil como añadirlo al inicio de todo el script 👏🏼 