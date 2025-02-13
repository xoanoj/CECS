Parte de [[Analise Forense]]

Cada CPU solo puede ejecutar un proceso a la vez (aunque hoy en dia cada CPU cuenta con multiples nucleos e hilos)

Existe una cola de procesos listos, hay dos algoritmos de gestion:
- Apropiativos
- No apropiativos 

Los procesos siguen máquinas de estados, se pueden definir en 3, 5 o 7 estados.

La de 7:

![[Pasted image 20250213201942.png]]

Cuando no hay suficiente espacio en memoria, se utiliza la memoria SWAP que existe en disco.

El diagrama de 7 estados:

![[Pasted image 20250213202224.png]]![[Pasted image 20250213202428.png]]