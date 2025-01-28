
Parte de [[Info Gathering]] y [[Hacking Ético]]
### DNS

Ver [[Sistemas DNS]]

Registros whois:

``` bash
whois -H [dominio/IP]
whois [dominio/IP/Rango]
```

En europa los datos de registrante etc. están censurados.
Los dominios .es tienen registro WHOIS pero estan en dominios.es o nic.es

También se puede usar:

viewdns.info
who.is

Tambien se puede usar la wayback machine para ver who.is hace x años para ver registros whois de páginas europeas que hoy en dia estarian censuradas.

---

Otras formas de conseguir info mediante DNSs:

``` bash
host [dominio]
```

Usando los tipos de registro de [[Sistemas DNS]]:

``` bash
host -t [tipoDeRegistro] [dominio]
```

Descubrir subdominios por fuerza bruta contra DNS:

Metodo malo:

Crear un archivo .txt con una lista de posible cabeceras de subdominio y utilizar

``` bash
for i in $(cat [lista].txt) ; do host $i.[site].[com,net...] ; done
```

La forma apropiada sería utilizar una herramienta de fuerza bruta activa como FFUF (aunque esto sería [[Metodologías de reconocimiento activo]]) 

---

Transferencias de zona: ver [[Metodologías de reconocimiento activo]]

---
Ver subdominios con dorking:

``` bash
site:[domain] -www
```

---

theHarvester requiere claves de API para algunos sources, se utiliza en buena parte para reconocimiento de empresas

```
theHarvester -d [dominio] -a
```

---

También existe h8mail (no viene por defecto en kali)

```
h8mail -t [cuentadecorreo]
```

---

Para buscar cuentas de usuarios en distintos servicios podemos utilizar whatsmyname.app, sherlock...