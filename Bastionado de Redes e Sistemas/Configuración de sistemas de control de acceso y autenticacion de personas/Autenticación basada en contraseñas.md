Parte de [[Bastionado de Redes e Sistemas]]

Políticas de contraseñas:

- Periodos de validez
- Posibilidad de reutilizacion de contraseñas ya usadas
- Formato de la contraseña
	- Longitud mínima
	- Tipos de caracteres que deben incluir
	- Cumplimiento de reglas semánticas
- Posibilidad de elección y modificación de la contraseña por parte del usuario
- Almacenamiento de las claves
	- Tamaño del histórico de claves a almacenar
	- Método de cifrado de las claves
- Número de intentos de autenticación permitidos

Recomendaciones para contraseñas seguras:
- Más de 8 caracteres
- Camibiar las contraseñas con regularidad
- Utilizar signos de puntuación si se permite
- Comprobar las contraseñas a utilizar en las bases de datos de leaks

Acciones a evitar:
- Repetir contraseñas
- Utilizar información personal en la contraseña
- Evitar secuencias básicas de teclado
- No repetir los mismos caracteres
- Evitar utilizar solamente números

Parámetros de gestión de contraseñas:
- Número de intentos limitados
- Longitud mínima
- Restricciones de formato
- Envejecimiento y expiración de contraseñas

---
## Autenticación en entornos de dominio Windows

- Directorio Activo: Servicio de directorio de la plataforma Windows que permite que las aplicaciones encuentren, utilicen y administren recursos del dominio.
- GPOs (Group Policy Objects): Parametrizaciones de Windows que permiten controlar los entornos de trabajo de las cuentas de usuario y equipo. Se pueden definir a varios niveles
	- Locales
	- De Sitio (concepto "site" de AD)
	- Dominio
	- Unidad Organizativa

Cita de seguridad Windows.

```
Políticas de grupo (GPO). Se configuran mediante la herramienta Administración dedirectivas de grupo. Podemos establecer:–Políticas de contraseñas: a través de estas, configuramos ciertos requerimientoscomo la duración de la contraseña, longitud y complejidad.–Políticas de bloqueo de cuentas: permiten configurar cuándo se bloquea una cuentade usuario cuando escribe la contraseña de manera incorrecta varias veces.Ojo! Las políticas de contraseñas deben de ser configuradas en una GPO vinculadaal dominio (bien en la GPO por defecto o en otra distinta). Las políticas decontraseñas en GPOs vinculadas a OUs solo tendrán efecto en los inicio de sesiónlocales en los equipos que pertenezcan a dicha OU.
```

- PSOs (Password Setting Objects): Permiten especificar políticas de contraseñasy de bloqueo de cuentas a nivel de usuario y grupo, lo que nos va a permitir una mayorflexibilidad a la hora de trabajar con grupos de usuarios con condiciones específicas depolíticas de contraseñas.

Los sistemas Windows tienen por defecto:
- Administrador (viene deshabilitada por defecto y debería quedarse así)
- Invitado
- Initial User (se utiliza durante la instalación del SO)

Windows tambien utiliza para ejecutar sus propios servicios:
- LocalSystem (o SYSTEM)(privilegios plenos, muchos malware emplean este proceso)
- LocalService (tiene menos privilegios)
- NetworkService (Servicio de red)

Y en cuanto a grupos:

- Administradores (y Administradores de dominio)
- Operadores de copia
- Invitados
- Operadores de configuración
- Usuarios avanzados
- Usuarios

Grupos especiales de forma interna:
- Creator Owner (La cuenta que ha creado o tomado posesión de un dispositivo)
- Todos (incluye a todos los usuarios)
- Interactive (los que tuilizas introduccion interactiva)
- Network (El grupo de usuarios que accedieran por red)
- Usuarios autenticados (Todos los usuarios que han accedido al sistema mediante un login de usuario y contraseña)
- Anonymous Login
- Terminal Server Users

Tambien existen grupos restringidos
