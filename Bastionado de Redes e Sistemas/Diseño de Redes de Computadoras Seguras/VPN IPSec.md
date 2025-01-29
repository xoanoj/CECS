Parte de [[Diseño de Redes de Computadoras Seguras]]

Contexto sobre -> [[VPNs]]

IPSec nos permite enviar datos de forma segura a traves de IP, es en cierto modo equiparable a las [[VLAN]] pero a nivel de capa 3.

IPSec por definicion es un estandar para comunicaciones VPN. Se usa de dos modos:
- Acceso remoto: Los usuarios deben ejecutar algun tipo de software cliente en un dispositivo, el cual se conecta a un servidor VPN en la organizacion a traves de internet.
- Site to site: Tipicamente se usa para interconectar sedes de na organizacion, dos dispositivos VPN establecen un tunel IPSec por el que se comunican de forma segura. Por esto los usuarios no necesitan ningun software cliente.

Por esto existend dos tipos de operacion para IPSec:
- Modo transporte: Se añade una cabecera al paquete IP original, pero sigue manteniendose la cabecera original, por lo que no se oculta dicha informacion. Los datos pueden ser cifrados o no
![[Pasted image 20250129162417.png]]
- Modo tunel: Se encapsula todo el paquete original con una nueva cabecera IP, esto permite ocultar la informacion de red de ambas entidades (Es inherentemente mas seguro que el modo transporte)
![[Pasted image 20250129162641.png]]

Protocolos que permite IPSec:
- IKE (internet key exchange): Es el protocolo utilizado para la gestion de las asociaciones de seguridad (SA) y el intercambio de clave.
- Authentication Headers (AH): Se utiliza para garantizar la integridad de los datos y la autenticidad del origen (no dice nada de confidencialidad)
- Encapsulation Security Payload (ESP): Es el protocolo utilizado principalmente para garantizar tambien la confidencialidad de la informacion.

IPSec define la conexion entre dos extremos mediante el termino "Asociaciond de seguridad" (SA). Cada SA contiene detalles de la conexion, el modo de funcionamiento, el protocolo empleado, informacion de los algoritmos criptograficos empleados y un indice (SPI, Security Parameter Index) que identifica la conexion. Tienen la particularidad de que se definen en una sola dirección, por ello, parauna comunicación bidireccionales necesario establecer dos asociaciones de seguridad, cada una de las cuales tendrá asociados unos parámetros específicos

---
Intercambios de claves con IKE:

![[Pasted image 20250129163332.png]]

---

El protocolo AH puede operar tanto en modo transporte como tunel, igualmente sigue sin ofrecer ningun tipo de confidencialidad

La integridad por hashes se calcula sobre casi todos los datos del paquete (incluyendo la cabecera) por lo que operaciones como SNAT y DNAT pueden causar que los paquetes figuren como falsificados/modificados. Para estos casos utiliza una tecnica NAT-T (NAT Transversal) que engloba todo el paquete en un datagrama UDP.

![[Pasted image 20250129164016.png]]

---

Finalmente el protocolo ESP (el que se utiliza mayoritariamente en la practica ya que garantiza confindencialidad)

Existe un SA para cada sentido ya que la autenticacion se realiza desde ambos extremos , contra ambos extremo. Protege tambien contra ataques de repeticion

En modo transporte, utilizando ESP, NAT no deberia generar problemas (como con AH)

![[Pasted image 20250129164027.png]]