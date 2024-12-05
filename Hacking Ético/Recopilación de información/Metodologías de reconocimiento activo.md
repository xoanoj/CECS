
Parte de [[Info Gathering]] y [[Hacking Ético]]


Enumeración de transferencia de zona de DNS:
(ver también apuntes de eJPT [[DNS Zone Transfer]], ver también [[Sistemas DNS]])

``` bash
host -la [dominio]
host -la [dominio] [servidorDNS]
```

Es importante probar con más de un servidor de DNS (de ser posible todos), en el ejemplo de clase:

``` bash
host -la megacorpone.com ns2.megacorpone.com
```

funciona mientras que con ns1 no.

Ejemplo:

``` bash
host -t ns zonetransfer.me
```

Da dos nombres de dominio, despues con:

``` bash
host -la zonetransfer.me nsztm1.digi.ninja
host -la zonetransfer.me nsztm2.digi.ninja
```

Vemos la información.