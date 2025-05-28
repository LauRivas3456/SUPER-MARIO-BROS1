Super Mario Bros (Nivel 1) – Recreación en Python para Proyecto final 
Este proyecto es una recreación del primer nivel del clásico juego Super Mario Bros, desarrollado en Python utilizando la librería Pygame. El objetivo es revivir la experiencia del videojuego original

Características
1. Motor gráfico 2D basado en Pygame
2. Reimplementación de elementos clave del primer nivel: bloques, enemigos, plataformas, y decoraciones
3. Gestión de colisiones, movimientos y saltos
4. Módulos organizados por funcionalidad: gráficos, audio, lógica del juego, actores, y herramientas
5. Archivos de imagen y música incluidos 

Requisitos para ejecucion 
1. Python 3.8+
2. Pygame (pip install pygame)

Instalación
git clone https://github.com/LauRivas3456/SUPER-MARIO-BROS1.git

Documentacion
main.py
Es el archivo principal del juego. Se encarga de iniciar todo: abre la ventana, carga imágenes y sonidos, y corre el bucle donde se actualiza y dibuja todo.
musica.py
Controla la música y sonidos del juego, como la canción de fondo o el sonido al agarrar monedas y morir. Usa pygame.mixer para manejarlos.
graphics.py
Se encarga de mostrar imágenes en pantalla: personajes, enemigos, fondos y objetos. Usa sprites para que todo se vea bien.
graphics_text.py
Muestra texto como el puntaje o mensajes. Sirve para que el jugador vea información del juego en pantalla.
graphics_transform.py
Tiene funciones para cambiar el tamaño, girar o mover imágenes. Ayuda a que las animaciones se vean mejor.
file_management.py
Maneja archivos que tienen datos del juego, como los niveles y las posiciones de los objetos. Los lee cuando se inicia el juego.
custom_math.py
Guarda funciones matemáticas personalizadas que se usan para calcular física o colisiones.
other_tools.py
Tiene funciones útiles para tareas varias, como manejar colores o calcular coordenadas. Ayuda a que el código sea más organizado.
reference.py
Guarda valores y configuraciones generales, como tamaños y velocidades. Así se pueden usar en todo el juego sin repetirlos.
MarioBros/actores.py
Define a Mario y a los enemigos. Cada uno tiene su forma de moverse, chocar y animarse.
MarioBros/baseElementos.py
Tiene las clases base de los objetos del juego. Les da cosas comunes como posición, imagen y colisiones.
MarioBros/bloques.py
Maneja los bloques con los que Mario puede interactuar, como los que dan monedas o poderes al golpearlos.
MarioBros/cargar.py
Lee archivos para armar los niveles, colocando enemigos, bloques y decoraciones en el lugar correcto.
MarioBros/decorativo.py
Define cosas del fondo como nubes y montañas. No afectan el juego, pero lo hacen ver más bonito.
MarioBros/plataformas.py
Maneja las plataformas donde Mario camina o salta. Algunas se mueven o hacen algo especial.
MarioBros/reference.py
Tiene configuraciones específicas del mundo de Mario, como imágenes y colores que se usan dentro del juego.
MarioBros/Archivos/
Guarda todas las imágenes, sonidos y archivos de configuración. Aquí están los recursos que el juego necesita para funcionar bien.



Autores
Ana Sofia Gomez Camargo
Laura Valentina Rivas Caicedo

Este proyecto fue desarrollado como trabajo final para la materia Programacion orientada a objetos, en el marco del curso de Tecnologia y Desarrollo en Software

Nos basamos en múltiples recursos para aprender y estructurar este juego, entre ellos:

1. Tutoriales de creación de juegos con Pygame
2. Repositorios educativos sobre Mario Bros en Python
3. Asesoría del profesor 
