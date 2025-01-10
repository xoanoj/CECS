Parte de [[Diseño de Redes de Computadoras Seguras]]

Existen los modelos TCP/IP y el modelo OSI

OSI:
- 7- Aplicacion
- 6- Presentacion
- 5- Sesion
- 4- Transporte
- 3- Red
- 2- Enlace de datos
- 1- Fisica

Como modelo practico no se utiliza OSI, pero si como conceptual.

Una puerta de enlace puede cambiar el protocolo que utiliza, por ejemplo recibir packets de IP bajo Ethernet pero enviarlos hacia fuera mediante otro protocolo, por ejemplo WiFi.

Las puertas de enlace operan a un maximo de capa de red, nunca por encima. (Recordar que un enrutador cambia la MAC del paquete, no la IP destino)