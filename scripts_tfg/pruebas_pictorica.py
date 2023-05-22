import pygame
import random,os

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
X, Y = pygame.display.set_mode().get_size()
screen = pygame.display.set_mode((X, Y), pygame.RESIZABLE)

# Nombres de las imágenes
img_folder = "imgs_prueba_pict/"

# Obtener una lista de los nombres de archivo de todas las imágenes en la carpeta
img_paths = sorted([img_folder+f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f)) and f.endswith('.jpg')]    )
counter = 1
contiene_c = []
contiene_incorrecta = []
contiene_correcta = []
# print(img_paths)
for elemento in img_paths:
    if '_central' in elemento:
        contiene_c.append(elemento)
    if '_incorrecta' in elemento:
        contiene_incorrecta.append(elemento)
    if '_correcta' in elemento:
        contiene_correcta.append(elemento)
print(contiene_c)

# Renderizar la última palabra del nombre de las imágenes
last_words_c = [image_name.split("_")[-1].split(".")[0] for image_name in contiene_c]
last_words_incorrecta = [image_name.split("_")[-1].split(".")[0] for image_name in contiene_incorrecta]
last_words_correcta = [image_name.split("_")[-1].split(".")[0] for image_name in contiene_correcta]
print(last_words_c)
# Definir la fuente y tamaño del texto
font = pygame.font.Font(None, 36)

# Definir tamaño de las imágenes
image1 = pygame.Surface((int(X*0.5), int(Y*0.5)))
correct_image = pygame.Surface((int(X*0.25), int(Y*0.25)))
incorrect_image = pygame.Surface((int(X*0.25), int(Y*0.25)))

# Definir posición de las imágenes
image1_rect = image1.get_rect(center=(int(X*0.5), int(Y/3.5545454)))
correct_image_rect = correct_image.get_rect(center=(int(X/1.23), int(Y/1.4)))
incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333), int(Y/1.4)))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar las imágenes
    screen.fill((0, 0, 0))
    screen.blit(image1, image1_rect)
    screen.blit(correct_image, correct_image_rect)
    screen.blit(incorrect_image, incorrect_image_rect)

    # Renderizar el texto en las imágenes
    for i in range(len(last_words_c)):
        text_surface_c = font.render(last_words_c[i], True, (255, 255, 255))
        text_rect_c = text_surface_c.get_rect(center=(image1_rect.centerx, image1_rect.bottom + 50))
        screen.blit(text_surface_c, text_rect_c)

        text_surface_incorrecta = font.render(last_words_incorrecta[i], True, (255, 255, 255))
        text_rect_incorrecta = text_surface_incorrecta.get_rect(center=(correct_image_rect.centerx, correct_image_rect.bottom + 50))
        screen.blit(text_surface_incorrecta, text_rect_incorrecta)

        text_surface_correcta = font.render(last_words_correcta[i], True, (255, 255, 255))
        text_rect_correcta = text_surface_correcta.get_rect(center=(incorrect_image_rect.centerx, incorrect_image_rect.bottom + 50))
        screen.blit(text_surface_correcta, text_rect_correcta)

        # Actualizar la pantalla

        
        pygame.time.wait(3000)
        screen.fill((0, 0, 0))
# Salir del juego
pygame.quit()