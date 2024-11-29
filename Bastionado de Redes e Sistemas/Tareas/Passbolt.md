## Creación del escenario:

Clonación de la herramienta:

``` bash
git clone https://github.com/passbolt/passbolt_docker
```

Configuro la URL de la BD en el docker-compose:

![[Pasted image 20241129194109.png]]

Y despliego mediante:

``` bash
docker compose -f docker-compose-ce.yaml up -d
```

Creación del usuario admin (utiliza el correo del dominio mediante whoami):

``` bash
docker compose -f docker-compose-ce.yaml exec passbolt su -m -c "bin/cake passbolt register_user -u $(whoami)@iessanclemente.net -f Xoan -l Otero -r admin" -s /bin/sh www-data
```

Mensaje de confirmación:

![[Pasted image 20241129194422.png]]

Configuramos la contraseña maestra, en mi caso el hash md5 de mi usuario de correo:

```
a24xoanoj@iessanclemente.net
be2c5f5b34af0d343ae403095753c3f3
```

Finalmente accedo a la instancia Passbolt

![[Pasted image 20241129194917.png]]

---
### Ejercicio
Para que mi compañero pudiera acceder a mi instancia tuve que cambiar la configuración