Parte de [[Phishing]]

Deben reunirse los artefactos, que pueden ser de tipo:

- De cabecera
- De Web
- De Fichero

Por ejemplo, la direccion de correo electronico de envio (que puede estar spoofeado(DMARC exploits juejuejue)), la linea de asunto ya que se puede utilizar como regla para bloquear spam, las direcciones de destinatario ya que puedes identificar al resto de vicimas del correo, la direccion de respuesta ya que si es un exploit de DMARC el atacante no tendra acceso a la bandeja de respuesta del correo spoofeado. La fecha y hora para poder realizar estimaciones. 

En cuanto a artefactos de archivo:
- Nombre del archivo
- Hash

En cuanto artefactos web, todos aquellos a los que te redirija el correo electronico, y el dominio raiz para ver si es malicioso o uno neutral que ha sido vulnerado.

Herramientas como PhishTool automatizan esto

## Caso de Phishing 2 con any.run

- Cómo clasifica AnyRun este correo electrónico?
Como sospechoso 
- ¿Cuál es el nombre del archivo PDF?
Payment-updateid.pdf
- ¿Cuál es el hash SHA 256 para el archivo PDF?
CC6F1A04B10BCB168AEEC8D870B97BD7C20FC161E8310B5BCE1AF8ED420E2C24
- ¿Qué dos direcciones IP se clasifican como maliciosas? Desactiva las direcciones IP.
2x16x107x24
2x16x107x83
- ¿Qué proceso de Windows se marcó como tráfico potencialmente malo ?
svchost.exe

## Caso de Phishing 3 con any.run
- ¿En qué se clasifica este análisis?
Como actividad Maliciosa
- ¿Cuál es el nombre del archivo de Excel?
CBJ200620039539.xlsx
- ¿Cuál es el hash SHA 256 del archivo?
5F94A66E0CE78D17AFC2DD27FC17B44B3FFC13AC5F42D3AD6A5DCFB36715F3EB
- ¿Qué dominios figuran como maliciosos? Desactive las URL y envíe las respuestas en orden alfabético.
biz9holdingsxcom
findresultsxsite
ww38xfindresultsxsite
- ¿Qué direcciones IP figuran como maliciosas? Elimine las direcciones IP y envíe respuestas de menor a mayor.
75x2x11x242
103x224x182x251
204x11x56x48
- ¿Qué vulnerabilidad intenta explotar este archivo adjunto malicioso?
CVE-2017-11882