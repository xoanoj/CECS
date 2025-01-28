Nota de [[Hacking Ético]]

- Se implementa con una base de datos distribuida
- Usa una arquitectura cliente-servidor

Para obtener una respuesta seguramente se consultarán varios servidores DNS hasta contactar con el que tiene la respuesta:

El cliente lanza una pregunta (recursiva) al servidor DNS Local, el servidor DNS realiza preguntas iterativas con distintos servidores DNS

El primer DNS que contacta el servidor DNS local es llamado el Servidor DNS "Raiz"

Registros de DNS:
- SOA (Start of Authority)
- NS (Name Server)
- A (Address)
- AAAA (Dirección IPv6)
- MX (Mail eXchanger)
- PTR (Pointer)
- HINFO (Host Info)
- SRV (Service)
- SPF (Sender Policy Framework)
- TXT (Asociar texto con el nombre del dominio)
- RP (Persona responsable)
