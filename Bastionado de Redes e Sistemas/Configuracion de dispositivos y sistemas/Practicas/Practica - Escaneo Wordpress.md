
Practica de [[Configuracion de dispositivos y sistemas]]

Lanzamos el escenario e instalamos

``` bash
gem install wpscan
wpscan --help
```

## Escaneo de servicio Wordpress utilizando wpscan

>wpscan es una herramenta escrita en Ruby que permite realizar una auditoría de posibles vulnerabilidades de un servicio wordpress. 
>
>Utilizando distintos plugins puede realizar distintas baterías de pruebas contra varios aspectos relacionados con este conocido CMS.

Escaneo basico:

``` bash
wpscan --url http://192.168.50.2/wordpress
```

Encontrar usuarios:

``` bash
wpscan --url http://192.168.50.2/wordpress --enumerate u
```

Encontrar plugins vulnerables:

``` bash
wpscan --url http://192.168.50.2/wordpress --enumerate vp
```

Encontrar todo los plugins:

``` bash
wpscan --url http://192.168.50.2/wordpress --enumerate ap
```

Ver todos los temas (incluyendo los que no estan en uso):

``` bash
wpscan --url http://192.168.50.2/wordpress --enumerate at
```

Atacar cuentas de usuarios:

``` bash
wpscan --url http://192.168.50.2/wordpress -passwords passwords.txt
```