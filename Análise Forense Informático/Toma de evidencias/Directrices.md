- Notas detalladas
- Especificar hora (UTC o en hora local)
- Prepararse para testificar lo realizado
- En caso de dilema entre recoleccion y analisis, prima la reconeccion
- Ir en orden de mas volatil a menos volatil
- Comprobar los metodos de recoleccion implementables
- Ser veloz, preciso y metodico
	- Automatizar todo lo posible
	- Trabajar en paralelo entre dispositivos
	- Ir paso a paso
---

### Orden de volatilidad:

1. Registros y caché
2. Tablas de enrutamiento, procesos, estadisticas del kernel
3. Memoria
4. Sistemas de ficheros temporales
5. Disco
6. Logs remotos del sistema
7. Configuracion fisica y topologia de red
8. Copias de seguridad

(Puede variar en el caso de Cloud)

---

### Cosas a evitar:

- Apagar/Encender innecesariamente
- No confiar en los programas del sistema
- No emplear programas que modifiquen (ni que modifiquen metadatos)
- No tener cuidado al eliminar agentes externos de cambio (ej:detección de que un equipo sea desconectado de la red)

---

### Consideraciones de privacidad:

- Respetar las reglas de privacidad
	- No dar acceso a personas que no lo tendrían normalmente
- No entrometerse en la privacidad de otros salvo necesidad