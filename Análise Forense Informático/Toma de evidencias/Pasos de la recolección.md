Parte de [[Toma de evidencias]]

- Eliminar agentes de cambio
- Recolectar con herramientas especializadas
- Registrar la desviación del reloj del sistema
- Preguntarse que más puede ser una evidencia
- Documentar cada paso
- Tomar notas de quien estuvo allí y que estuvo haciendo
- Generar checksums y firmar la evidencia criptograficamente
	- Utilizando una herramienta que  no modifique metadatos
- Explicar claramente como se encontro la evidencia, como se manejo y que paso
	- Hay que documentar:
		- Donde cuando y quien la descubrio, manejo, examino y recolecto
		- Quien la tuvo bajo custodia, cuanto tiempo estuvo y donde
		- Cuando cambie de mano, quien y como hizo la transferencia

---
#### Almacenamiento y acceso a la evidencia

- Usar medio de almacenamiento comunes
- Restringir y documentar acceso a la evidencia
- El RFC no lo menciona pero:
	- Controlar la temperatura y humedad del lugar
	- Usar armario contra incendio e inundación

---
#### Herramientas de la recolección:

- Software en modo solo lectura
- No usar las herramientas del sistemas
- Deberían estar enlazadas de forma estática
- Usar herramientas ligeras
- Usar herramientas que modifiquen lo mínimo posible
- Estar preparado para testificar sobre la autenticidad y fiabilidad de las herramientas.

Herramientas necesarias:

- Copiadores bit a bit
- Generadores de checksum
- Examinador de procesos
- Comprobadores del estado de sistema
- Generador de imagenes del core
- Scripts de automatización
