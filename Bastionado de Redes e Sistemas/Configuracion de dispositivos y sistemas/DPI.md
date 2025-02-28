Parte de [[Configuracion de dispositivos y sistemas]]

DPI (Deep Packet Inspection) es una técnica (aunque normalmente se habla e motors DPI) de analisis de tráfico que no utiliza únicamente el trazado de estados de paquetes individuales. Permite controlar flujos de tráfico, inspeccionar el tráfico en detalle, gestionar el tráfico en tiempo real y en general realizar un analisis mucho más dinámico.

Como analogia:

>Analisis de Malware Estatico - > Analisis de Malware Dinamico
>Inspeccion del estado de paquetes (como IPTables) - > DPI

El DPI puede emplear machine learning o definicion de listas o excepciones para evitar falsos positivos

Como problema tambien puede dificultar la gestion de dispositivos que empleen DPI (ya que son sistemas complejos) y pueden ralentizar el tráfico ya que el analisis es mas costoso en recursos. Tambien puede incumplir las leyes de protección de datos.

Esta muy relacionado con los IDSs e IPSs 