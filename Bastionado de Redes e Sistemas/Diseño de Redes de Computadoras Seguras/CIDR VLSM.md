Parte de [[Diseño de Redes de Computadoras Seguras]] 

- CIDR: Usa las mascaras de subredes de longitud variable (VLSM) para ayudar a conservar el espacio de las direcciones
- VLSM es la division de una red en subredes

La mascara de red indica que bytes de una IP estan dedicados a identificar a la red y cuales al host, por ejemplo 17.12.0.1/24 (donde 24 es 24 ya que su otra representacion seria 255.255.255.0 (en binario 24 1s consecutivos)) unicamente el ultimo byte estaria dedicado a identificar hosts mientras que los otros 3 estarian dedicados a identificar redes. Con lo cual una red 124.3.0.0/24 podria tener 255 hosts.

El mecanismo encargado de convertir IPs publicas en privada y viceversa en peticiones y respuesta se denomina NAT

Hoy en dia se utiliza el modelo classless que trabaja con mascaras de red (VLSM)

Cuando se calcula la cantidad de hosts en una red hay que tener el primer valor siempre sera la direccion de red y que el ultimo valor sera el de broadcast. Por ejemplo en 10.10.10.0/24 habra 254 hosts posibles ya que 0 sera siempre la direccion de red y 255 la direccion de broadcast