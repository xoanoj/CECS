Herramientas:
- Sysinternals de Microsoft
- Nirsoft
Tienen como ventaja que no necesitan instalación y que en su maryoría se pueden ejecutar desde el cmd.                                                                                                                                   
Es mejor ejecutar las herramientas desde un dispositivo de solo lectura (si puede ser desde una consola cmd.exe)
La salida de los comandos debe mandarse a otro dispositivo
Los motores antivirus pueden bloquear las herramientas por lo que se debe deshabilitar, aunque no siempre se puede. Si no esta habilitado no deberiamos habilitarlo.

Es imprescindible establecer una linea temporal de la recopilacion de evidencias y acceso y modificacion de recursos:

``` powershell
date /t > FechaYHoraDeInicio.txt &time /t >>
FechaYHoraDeInicio.txt &tzutil /g>>
FechaYHoraDeInicio.txt
```

En windows XP no hay tzutil:

``` powershell
date /t > FechaYHoraDeInicio.txt &time /t >>
FechaYHoraDeInicio.txt &reg query
"HKEY_CURRENT_USER\Software\Microsoft\Wind
ows NT\CurrentVersion\Time Zones" >>
FechaYHoraDeInicio.txt
```

Al final habría que hacer lo mismo pero con fecha de fin

Info de red y conexiones:

![[Pasted image 20241209202626.png]]
![[Pasted image 20241209202635.png]]

Ficheros y carpetas compartidas:

![[Pasted image 20241209202905.png]]![[Pasted image 20241209202919.png]]

Procesos:

![[Pasted image 20241209202932.png]]![[Pasted image 20241209202941.png]]

Información de Usuarios:

![[Pasted image 20241209203105.png]]![[Pasted image 20241209203111.png]]

Contraseñas:

Son útiles (lol) e identifican diferentes servicios (lol)

- MailPassView
	- Contraseñas de los principales gestores de correo
	- mailpv /stab "MailPassView.txt"

- WebBrowserPassView
	- Contraseñas almacenadas en los navegadores
	- WebBrowserPassView /stab "fichero.txt"

- Network Password Recovery
	- Contraseñas de los recursos de red a los que está conectado el usuario actual
	- Nepass /stab "NetworkPasswordRecovery.txt"

Cache de navegadores:

![[Pasted image 20241209203506.png]]

Ficheros y directorios:

![[Pasted image 20241209203611.png]]![[Pasted image 20241209203619.png]]![[Pasted image 20241209203634.png]]

Historial de internet:

![[Pasted image 20241209203716.png]]![[Pasted image 20241209203722.png]]

Ultimas busquedas:

- MyLastSearch de Nirsoft
- MyLastSearch /stab "MyLastSearch.txt"

Cookies:
- Son pequeños ficheros de texto, permiten
	- Mantener la sesion de un sitio web
	- Realizar un seguimiento de la navegacion
	- Almacenar las preferencias de visualizacion
- Contiene info relevante como
	- Nombres de usuario
	- Fechas
	- etc.
- Programas
	- ChromeCookiesView
	- MozillasCookiesView
	- IECookiesView

Volumenes cifrados:

![[Pasted image 20241209204301.png]]

Otros:

![[Pasted image 20241209204319.png]]![[Pasted image 20241209204326.png]]

---
Buenas prácticas

- Se puede incluir la fecha y hora en el nombre del fichero donde se captura la evidencia

``` powershell
tasklist > "ProcesosEnEjecución-%date:~6,4%-
%date:~3,2%-%date:~0,2%_%time:~0,2%-
%time:~3,2%-%time:~6,2%-%time:~9,2%.txt"
```

Scripts:
- Ejecutar estos comandos uno a uno es tedioso, se deben crear scripts
- El script debe tener en cuenta
	- Sistema de 35b o 64b para lanzar las versiones correctas de las herramientas
	- Si el sistema es Windows XP obtener la timezone correctamente

Capturas de tráfico de red:

![[Pasted image 20241209204657.png]]

(Puede ser mejor TShark)

