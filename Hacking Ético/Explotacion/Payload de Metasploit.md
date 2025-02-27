Parte de [[Explotación]]

En metasploit hablamos de que un payload puede ser:

- Non Staged / Single / Inline / Stageless
	- Se envia todo el handler de golpe
- Staged
	- Se envia un dropper que ocupa espacio minimo que se encarga de descargar y ejecutar el resto de requisitos. Son mas preferibles ya que a veces no son detectados por los antivirus.

La nomenclatura suele ser
- windows/x64/shell_reverse_tcp = NON STAGED
- windows/x64/shell/reverse_tcp = STAGED