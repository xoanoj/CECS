Parte de [[Seguridad Perimetral]]

Virtual Local Area Networks, son redes virtualizadas, esto nos permite tener varios niveles de capa 2 independientemente de la capa 1.

Nos permite:
- Separar los switches en varios switches virtuales
- Solo los miembros de una VLAN pueden ver el tráfico de dicha VLAN.
	- El tráfico entre VLANs debe pasar por un enrutador
- Al hacer las redes mas eficientes a nivel de capa de enlace fisica, evita ciertos problemas relacionadas con la generacion de trafico masiva en redes.
- Permite controlar y confinar ataques a nivel de red


Caracteristicas:
- Podemos tener dos o mas VLANs por switch
- Los usuarios por lo general no saben a que VLAN pertenecen
- VLAN Estatica: Aquella VLAN que se define mediante los puertos de un switch (ej: los 20 primeros puertos del switch son parte de la VLAN1, los 3 siguientes de la VLAN2...) (Esto quiere decir que las VLANs se definen a nivel de switch, los usuarios finales no saben a que VLAN pertenecen)(Es decir es responsabilidad del switch saber si puede enviar una trama a una VLAN distinta)
- VLAN Dinamica: Una MAC esta asociada a una VLANs

![[Pasted image 20250124185745.png]]
En este ejemplo, los hosts de VLAN X no se pueden comunicar con VLAN Y, para comunicarse tendrian que hacerlo por capa de red

 Si el tráfico atraviesa varios switches tenemos que identificar las tramas que viajan entre los switches, estos enlaces entre los switches se denominan VLAN Trunks:
 
![[Pasted image 20250124185857.png]]

Las tags identifican una VLAN para que el switch que recibe el mensaje sepa a que VLAN enviar el trafico (tercer punto). Las tags se situan en las cabeceras del protocolo eth.

Los enlaces de puerto a host de VLAN se llaman access o edge, trunk es solo entre switches.

Esto quiere decir que las etiquetas las manejan unicamente los switches, un host seguira siempre sin saber a que VLAN pertenece.

Algunos equipos de CISCO requieren que especifiquemos de que tipo es cada puerto del switch, por ejemplo: Este es el puerto access de la VLAN3 numero 4. Esto es el puerto trunk por el que pueden circular las VLAN3,1,5.

El funcionamiento de los puertos trunk y las VLANs se pueden ver mas o menos como un firewall de capa 2.

El estandar 802.1Q del IEEE define como se deberia taggear el trafico, permitiendo que switches de distintos vendedores sean capaces de intercambiar trafico entre VLANs

![[Pasted image 20250124191220.png]]


![[Pasted image 20250124192054.png]]
La tecnica de enviar tramas a traves de la VLAN Trunk se denomina VLAN Trunking

En cuanto a complejidad, tener VLANs implica que:
- No se puede simplemente reemplazar un switch
- Hay que asegurarse de que todos los enlaces troncales estan transportando las VLANs necesarias.

Buenos usos:
- Hay que segmentar la red en varias subredes, pero no hay suficientes switches
- Separar los elementos de infraestructura como telefonos IP, controles automaticos, etc.
- Seperar el plano de control

Malos usos:
- Porque es posible  y te hace sentir cool
- Porque le daran seguridad absoulta para sus usuarios
- Porque le permiten extender la IP hasta otros edificios remotos

No se debe:
- Extender una VLAN a traves de todos los edificios
	- El trafico broadcast viaja a traves de todas las troncales, de un extremo a otro de la red.
	- Una tormenta de broadcast se propagara a traves de toda la extension de la VLAN y afectara a todas las VLANs.