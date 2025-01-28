Parte de [[Seguridad Perimetral]]

Muchas empresas utilizan VPNs para permitir a sus empleados conectarse a sus redes internas de forma remota. De forma generica el trafico debe estar cifrado (ser privado) y verificado de punta a punta. Las comunicaciones de HTTPS y SSH son ejemplos de VPN (de alto nivel), pero tambien existen VPNs de nivel bajo, por ejemplo a nivel de capa 3 (por ejemplo IPSec)

Cuando se utiliza IPSec, todos los datos del paquete son confidenciales (es decir, la cabecera tambien se cifra, no solo los datos)

Tambien existen VPNs de capa 2 como MACSEC

Cuanto mas bajo sea el nivel de la VPN, mas compleja sera la especificacion de su implementacion

---

Esencialmente, funcionan estableciendo una conexion entre el PC del usuario y un servidor VPN situado conectado mediante un router a la red interna de la organizacion.
