
Parte de [[Configuracion de los sistemas informaticos]]

Podemos inyectar un comando de arranque al final de la linea que carga el kernel, si lo hacemos (debido a un permiso de edicion mal configurado) podemos instanciar una shell nada mas se inicialice el kernel.

Una vez hecho solo hay que montar el sistema de archivos en modo escritura-lectura y utilizar passwd para modificar la contraseña de root.

Podemos evitar esto, entre otros, configurando el GRUB_TIMEOUT a 0

Podemos tambien configurar el bootloader GRUB para que requiera contraseña.