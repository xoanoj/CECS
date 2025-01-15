Parte de [[Diseño de Redes de Computadoras Seguras]]

Afecta a todo aquello que proteje la red en su entorno exterior.
Se debe recordar que las amenazas no necesariamente vienen siempre del exterior.
Normalmente la seguridad perimetral esta configurada de una forma mas estricta y en general de mejor calidad que la interna (lo cual es malo).

Los puntos debiles pueden ser:
- Implicitos (debilidades inherentes de los protocolos)
- Atribuibles a personas

Fundamentalmente, cualquier protocolo que no se utilice debe estar desactivado.

**Componentes**: Elementos tecnologicos intervinientes en la seguridad perimetral.

Los enrutadores (llamados cortafuegos de nivel 3 si filtran trafico) se pueden configurar para gestionar y filtrar el trafico a un nivel maximo de capa 3.

Otros elementos como los WAF (cortafuegos de nivel 7) pueden filtrar paquetes de datos de protocolos de nivel de aplicacion, como HTTP

NetFilter trabaja entre nivel 3 y nivel 4, lo cual permite cierto filtrado de trafico.

Hay dos perspectivas de trabajo:
- Listas negras (Todo permitido excepto por x elementos)
- Listas blancas (Nada esta permitido excepto por x elementos)

En IPTables, una accion de tipo DROP es aquella que deniega un paquete.

IPTables permite de forma indirecta (debido a la responsabilidad de capa) gestionar el trafico de protocolos.

