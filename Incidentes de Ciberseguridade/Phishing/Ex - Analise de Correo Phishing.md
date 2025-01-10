Parte de [[Phishing]]


>Escenario: Eres un analista SOC de nivel 1. Otros compañeros de trabajo te han reenviado varios correos electrónicos sospechosos. Debes obtener detalles de cada correo electrónico para que el equipo implemente las reglas adecuadas para evitar que recibir correos electrónicos de spam/phishing adicionales.

> P1. ¿Qué puerto está clasificado como Transporte Seguro para SMTP?

El puerto 587, ya que esl defectivo para el protocolo SMTPS

> P2. ¿Qué puerto está clasificado como Transporte Seguro para IMAP?

El 993, ya que permite cifrado TLS/SSL

> P3. ¿Qué puerto está clasificado como Transporte Seguro para POP3?

El 995 ya que permite cifrado TLS/SSL

> P4. ¿Qué encabezado de correo electrónico es lo mismo que "Responder a"?

Reply-To

>P5. Email1.eml ¿Para suplantar qué marca fue diseñado este correo electrónico?

La empresa de seguridad ADT

>P6. Email1.eml¿Cuál es la dirección de correo electrónico Remitente?

newsletters@ant\[.]anki-tech\[.]com

>P7. Email1.eml De lo que puedes deducir, ¿cuál crees que será un dominio de interés?

ant\[.]anki-tech\[.]com

>P8. Email1.eml Cual es la url acortada? Desactivala.

hxxps\[://]ant\[.]anki-tech\[.]com/ga/open/2-952622232-3970-423304-83825=3-17b3b9c21a

>P9. En las capturas de pantalla anteriores, ¿cuál es el URI de la imagen bloqueada?

hxxps\[://]i\[.]imgur\[.]com/LSWOtDI\[.]png

>P10. En las capturas de pantalla anteriores, ¿cuál es el nombre del archivo PDF adjunto?

Payment-updateid.pdf

---

>Analiza el correo electrónico email3.eml y responde las preguntas a continuación.
>
>Nota: Alexa es la víctima y Billy es el analista asignado al caso. Alexa reenvió el correo electrónico a Billy para que lo analizara.

>P11. ¿Por qué entidad de confianza se hace pasar este correo electrónico?

Por la empresa Home Depot

>P12. ¿Cuál es el correo electrónico del remitente?

support@teckbe\[.]com

>P13. ¿Cuál es la línea de asunto?

Thank you! Home Depot

> P14. ¿A dónde dirige el enlace URL “HAGA CLIC AQUÍ” (Indica la URL desactivada)

hxxp\[://]t\[.]teckbe\[.]com/p/?j3=EOowFcEwFHl6EOAyFcoUFVTVEchwFHlUFOo6lVTTDcATE7oUE7AUET==

---

## Informe Email 1

### Artefactos:

- From: newsletter@ant\[.]anki-tech\[.]com
- Display name: ADT Security Services
- Sender: newsletter@ant\[.]anki-tech\[.]com
- To: alexa@yahoo\[.]com
- CC: None
- In-Reply-To: None
- Timestamp: 05:35 pm, Jun 21st 2021
- Reply-To: reply@ant\[.]anki-tech\[.]com
- Message-Id: \<mid-34511e6d7ca189088b5e6e69df06a139-109@ant\[.]anki-tech\[.]com>
- Return-Path: reback-a3970-837890-838253-c8b776d9=952622232=8@ant\[.]anki-tech\[.]com
- Originating IP: 43\[.]255\[.]56\[.]161
- rDNS: FAST-INTERNET-43-255-56-161\[.]solnet\[.]net\[.]id
- URLs:
	- hxxps\[://]ant\[.]anki-tech\[.]com/ga/click/2-952622232-3970-423304-838253-590962-350694bcf9-17b3b9c21a
	- hxxps\[://]ant\[.]anki-tech\[.]com/ga/unsubscribe/2-952622232-3970-423304-838253-d0890c7eb0b8a71-17b3b9c21a
	- hxxps\[://]ant\[.]anki-tech\[.]com/ga/open/2-952622232-3970-423304-838253-17b3b9c21a

### Informe:

El correo encontrado en una campaña de phishing se hacia pasar por la empresa de seguridad ADH enviando un newsletter con opciones de ver mas y desuscribirse de la lista de correos que redirigian al dominio ant\[.]anki-tech\[.]com, dominio que segun Fortinet es malicioso y sospechoso de actividades de spam (https://www.virustotal.com/gui/url/347867eb67e011f1d7b2d4eb37ce38b3ba745552388a4ed0c540e2d078df5d7a)

Quizas no sea buena idea bloquear la IP, ya que pertenece a una empresa de hosting llamada Sol One que podria hostear a usuarios legitimos

Bloquear el Display Name tampoco parece una buena idea ya que es una cabecera que ADH podria utilizar comunmente.

La mejor opcion seria bloquear el dominio de correo ant\[.]anki-tech\[.]com ya que ha sido reconocido como spam anteriormente por Fortinet

### Conclusion:

Para evitar seguir recibiendo spam de este tipo se bloquea el dominio de correo del que procede, ya que otras normas podrian evitar el tragico legitimo 