ls -laParte de [[Bastionado de Redes e Sistemas]], relacionado con [[Kerberos]]

Repositorio:

``` bash
git clone https://github.com/javierfp-isc/bastionado_auth
```

Se levanta utilizando el comando make.

Esquema del escenario:

![[Pasted image 20241216165449.png]]

---

## Trabajando en el escenario

### Configuración de KDC
Accedo al service KDC y lanzo la configuración de kerberos:

```
make sh service=kdc
dpkg-reconfigure krb5-config
```

![[Pasted image 20241216170118.png]]
(Estos parámetros se almacenan en /etc/krb5.conf)

Creamos el realm de kerberos

```
krb5_newrealm
```

![[Pasted image 20241216170329.png]]
Descomentamos la última línea de /etc/krb5kdc/kadm5.acl para habilitar la instancia admin de los principales (es decir, usuarios) de administración.

### Creación de los objetos principal

Las identidades en kerberos se denominan "principal", se aplica tanto a usuarios de clientes como los usuarios de administración como a los servicios etc.

Accedemos a la consola de administración de kerberos mediantes:

```
kadmin.local
```

#### Principal para el servidor de SSH

En la consola de administracion de kerberos ejecutamos 

```
addprinc -randkey host/ssh
```

Lo cual crea el principal host/ssh@AUTH.KERB, el parametro -randkey genera una clave aleatoria para no tener que generarla a mano. Esto lo hacemos porque no utilizaremos contraseñas para la autenticacion sino keytab

Una keytab es un archivo que contiene una clave que se utiliza para autenticar de manera automatica, los principales deben tener su keytab, en este escenario se hace mediante un volumen de docker que esta conectado a los 3 contenedores (kerbshare)

Creamos la keytab del servicio ssh:

```
ktadd -k /sshuser.keytab sshuser@AUTH.KERB
```

Esta tabla habrá que enviarla al servidor ssh para que pueda autenticarse a si mismo contra el KDC

#### Principal para el cliente

Creamos el principal:

```
addprinc -randkey sshuser
```

Y su keytab:

```
ktadd -k /sshuser.keytab sshuser@AUTH.KERB
```

Podemos ver los principales creados con:

```
listprincs
```

Salimos de la consola kadmin.local con la opción q.

### Transferencia de las keytab

#### Transferencia de keytab para el servidor ssh y el usuario ssh

Copiamos al directorio compartido desde el KDC:

```
cp /ssh.keytab /var/kerbshare
cp /sshuser.keytab /var/kerbshare
```

Ahora en el servicio ssh (Al que accedo con make sh service=ssh):

```
cp /var/kerbshare/ssh.keytab /etc/krb5.keytab
```

(NOTA: El archivo /etc/ktb5.keytab es la ubicación por defecto de las keytab de kerberos en el sistema, tambien se buscan aqui por defecto)

Ahora hacemos la misma copia en el cliente:

```
cp /var/kerbshare/sshuser.keytab /sshuser.keytab
```

(NOTA: La cache de credenciales se puede destruir con kdestroy)

### Configuración del servidor ssh

Creamos el usuario:

```
useradd -m -s /bin/bash sshuser
```

#### Configuramos el cliente de kerberos

```
dpkg-reconfigure krb5-config
```

![[Pasted image 20241216174702.png]]

#### Configuracion del servicio openssh

Para que el servidor admita la configuración a través de kerberos es necesario editar /etc/ssh/sshd_config:

![[Pasted image 20241216175408.png]]

Y reiniciamos el servicio con:

```
service ssh restart
```

#### Configuración del cliente

Ejecutamos el configurador

```
dpkg-reconfigure krb5-config
```

y modificamos el ssh_config:

![[Pasted image 20241216180053.png]]

### Accediendo al servicio:

Obtenemos el ticket con la keytab:

![[Pasted image 20241216180248.png]]

![[Pasted image 20241216180327.png]]

Probamos a conectarnos por ssh al servidor ssh:

