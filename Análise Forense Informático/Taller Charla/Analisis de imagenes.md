
Taller de [[Analise Forense]]

- PRNU (Photo Response Non Uniformity): Patron de ruido propio de cada sensor debido a imperfecciones de sensor y filtrados que permite identificar dispositivos(comunmente instancias de un modelo, no modelos en si). Para conseguir el PRNU de un dispositivo hay que eliminar el ruido de la imagen.
- Se pueden realizar analisis del PRNU de una imagen bloque a bloque para identificar inserciones.

- Si se inserta una imagen adaptada en tamaño pueden no cuadrar las cantidades de pixeles por bloque. (Esto no funciona con la compresión JPEG)
- En el caso de insertar una imagen JPEG en otra JPEG, las rejillas utilizadas por el protocolo de compresión quedarán desalineadas y los histogramas DCT tendrán valores intermedios que no corresponden con los del resto de la imagen (ya que algunas partes de la imagen estarán comprimidas dos veces mientras que otras solo lo estarán una).
- No obstante si la imagen manipulada se guarda con peor calidad que la de la imagen original será muy complicado utilizar el análisis por bloques para determinar manipulaciones. Si se guarda con calidad superior será más fácil.

- Con vídeos, se puede estimar la localización de la grabación con la ENF (Electric Network Frequency), que produce un sonido de fondo identificable y permite determinar hora aproximada y localización. No solo afecta al sonido sino a la luminosidad de las fuentes de luz en interiores (depende del tipo de luz, es especialmente util con luz incandescente)(Relacionado con el flicker que se determina en función de los hz de la grabación).

---

