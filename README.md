# Buscaminas-Tragavenao
![alt text](https://i.imgur.com/YBy2HoQ.png)

Implementación de buscaminas usando Python3 y Pygame.  
Para instalar Pygame: pip install pygame  

## Algunas características:  
-Modificar el color de las banderas  
-Modificar el número de filas columnas y minas  
-Tabla de los 10 mejores puntajes (mejores tiempos)  

## Sobre el .cfg  
Tras iniciar el juego se creará un archivo con extensión cfg.  
Este se puede editar fácilmente con un editor de texto.  
Contiene 3 variables separadas por coma.  
Las primeras 3 indican la cantidad de filas, columnas y minas.  
La cantidad de minas debe ser menor o igual al número de cuadros
(número de filas * número de columnas) menos 2.  
Las últimas 3 indican el color de la bandera en RGB (cada valor de 0 a 255).  
Modificando estos valores se puede tener una bandera con color personalizado.
