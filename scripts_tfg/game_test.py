import pygame,time,os,random,json,statistics,datetime,platform
from pygame.locals import *
global namee
def mmain(Name,lang,VERSION):
    # Inicializa Pygame
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)
    start_time = pygame.time.get_ticks() 
    question_times=[]
    aciertos=0
    fallos=0
    omision=0
    # Definir tamaño de la ventana
    X=800
    Y=600


    X,Y = pygame.display.set_mode().get_size()
    window = pygame.display.set_mode((X, Y),RESIZABLE)



    # Crear superficie de fondo degradado
    background = pygame.Surface(window.get_size())
    background = background.convert()
    # Cargar la imagen de fondo
    bg_image = pygame.image.load('fondo1.png')

    # Escalar la imagen al tamaño de la ventana
    bg_image = pygame.transform.scale(bg_image, window.get_size())

    # Cargar imágenes
    img_folder = "imgs/"

    # Obtener una lista de los nombres de archivo de todas las imágenes en la carpeta
    img_paths = sorted([img_folder+f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f)) and f.endswith('.jpg')]    )
    counter = 1
    contiene_c = []
    contiene_incorrecta = []
    contiene_correcta = []
    print(img_paths)
    for elemento in img_paths:
        if '_central' in elemento:
            contiene_c.append(elemento)
        if '_incorrecta' in elemento:
            contiene_incorrecta.append(elemento)
        if '_correcta' in elemento:
            contiene_correcta.append(elemento)
    # print("Los elementos que contienen 'c'entral son:", len(contiene_c))
    # print("Los elementos que contienen 'incorrecta' son:", len(contiene_incorrecta))
    # print("Los elementos que contienen 'correcta' son:", len(contiene_correcta))
    # print(contiene_c[A])
    # print(contiene_incorrecta[A])
    # print(contiene_correcta[A])
    # exit()
    image1 = pygame.image.load(contiene_c[counter])
    correct_image = pygame.image.load(contiene_incorrecta[counter])
    incorrect_image = pygame.image.load(contiene_correcta[counter])

    # Definir tamaño de las imágenes
    image1 = pygame.transform.smoothscale(image1, (int(X*0.5), int(Y*.5)))
    correct_image = pygame.transform.smoothscale(correct_image, (int(X*0.25), int(Y*0.25)))
    incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(X*0.25), int(Y*0.25)))

    # Definir posición de las imágenes
    image1_rect = image1.get_rect(center=(int(X*0.5),int( Y/5.4545454)))
    aux_r=random.random()
    if aux_r<0.7:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
    else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.7148)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))

    # Banderas para verificar si se hizo clic en una imagen (int(X/1.23),int( Y/1.7148))
    correct_image_clicked = False
    incorrect_image_clicked = False



    running = True
    max_time_without_click = 4

    # tiempo actual sin clic
    time_without_click = 0
    last_click_time=start_time
    while running:
        counting_time = pygame.time.get_ticks() - start_time
        window.blit(bg_image, (0, 0))
        
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)            
        print(counting_string)        
        
        
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            # Salir si se presiona ESC
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
                
                
                

                    
            # Verificar si se hizo clic en una imagen
            elif event.type == pygame.MOUSEBUTTONUP:
                last_click_time = pygame.time.get_ticks()
                mouse_pos = pygame.mouse.get_pos()
                if correct_image_rect.collidepoint(mouse_pos):
                    incorrect_image_clicked = True
                elif incorrect_image_rect.collidepoint(mouse_pos):
                    correct_image_clicked = True
                    
                
                # Si se hizo clic en una imagen y el contador es menor a 10, cargar nuevas imágenes
                if ((correct_image_clicked ) or incorrect_image_clicked) and counter <=6:
                    
                    window.blit(image1, image1_rect)
                    window.blit(correct_image, correct_image_rect)
                    window.blit(incorrect_image, incorrect_image_rect)              
                    
                    if (correct_image_clicked ) and counter <=4:
                        print("click")
                        question_times.append(counting_time)
                        aciertos+=1                     
                        pygame.draw.rect(window, (0, 255, 0), incorrect_image_rect, 10)
                        counting_string2="Imagen correcta"
                        counting_text2 = font.render(str(counting_string2), 1, (255,255,255))
                        counting_rect2 = counting_text2.get_rect(center = window.get_rect().center)
                        window.blit(counting_text2, counting_rect2)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        

                    
                    if incorrect_image_clicked and counter <=4:
                        question_times.append(counting_time)
                        fallos+=1                     
                        pygame.draw.rect(window, (255, 0, 0), correct_image_rect, 10)
                        
                        counting_string2="No es la imagen correcta"
                        counting_text2 = font.render(str(counting_string2), 1, (255,255,255))
                        counting_rect2 = counting_text2.get_rect(center = window.get_rect().center)
                        window.blit(counting_text2, counting_rect2)
                        pygame.display.update()
                        pygame.time.wait(2000)


                    if (correct_image_clicked ) and counter >=5:
                        question_times.append(counting_time)
                        aciertos+=1                    
                        print("click")
                        pygame.draw.rect(window, (155,155,155), incorrect_image_rect, 10)
                        pygame.display.update()
                        pygame.time.wait(500)
                        

                    
                    if incorrect_image_clicked and counter>=5:
                        question_times.append(counting_time)
                        fallos+=1                        
                        pygame.draw.rect(window, (155,155,155), correct_image_rect, 10)

                        pygame.display.update()
                        pygame.time.wait(500)                        
                    
                                                
                    try:                  
                        # image1 = pygame.image.load(img_paths[counter * 3 - 2])
                        # correct_image = pygame.image.load(img_paths[counter * 3 - 1])
                        # incorrect_image = pygame.image.load(img_paths[counter*3])

                        image1 = pygame.image.load(contiene_c[counter])
                        correct_image = pygame.image.load(contiene_incorrecta[counter])
                        incorrect_image = pygame.image.load(contiene_correcta[counter])


                        image1 = pygame.transform.smoothscale(image1, (int(X*0.5),int( Y*.5)))
                        correct_image = pygame.transform.smoothscale(correct_image, (int(X*0.25),int( Y*0.25)))
                        incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(X*0.25),int( Y*0.25)))

                        # Definir posición de las imágenes
                        image1_rect = image1.get_rect(center=(int(X*0.5),int( Y/5.4545454)))
                        # correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
                        # incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
                        aux_r=random.random()
                        if aux_r<0.7:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
                        else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.7148)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
                        # # Reiniciar banderas
                        correct_image_clicked = False
                        incorrect_image_clicked = False
                        counter += 1
                        # print(counting_time)
                        counting_time=counting_time-2000
                    except:
                        print("except")
                        running = False
                    # print(counting_time)
            # Dibujar marcos en la imagen seleccionada
            # actualizamos el tiempo sin clic
        time_since_last_click = pygame.time.get_ticks() - last_click_time
        time_without_click = time_since_last_click / 1000
        
        # comprobamos si se ha pasado el tiempo máximo sin clic
        if time_without_click > max_time_without_click:
            question_times.append(counting_time)
            omision+=1        
            print("No se ha hecho clic en la ventana en los últimos 4 segundos.")
            
            counting_string_time="No se ha hecho clic en la ventana en los últimos 4 segundos."
            counting_text_time = font.render(str(counting_string_time), 1, (255,255,255))
            counting_rect_time = counting_text_time.get_rect(center = window.get_rect().center)
            window.blit(counting_text_time, counting_rect_time)
            pygame.display.update()
            pygame.time.wait(2000)     
            
                    
            image1 = pygame.image.load(contiene_c[counter])
            correct_image = pygame.image.load(contiene_incorrecta[counter])
            incorrect_image = pygame.image.load(contiene_correcta[counter])
            
            image1 = pygame.transform.smoothscale(image1, (int(X*0.5),int( Y*.5)))
            correct_image = pygame.transform.smoothscale(correct_image, (int(X*0.25),int( Y*0.25)))
            incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(X*0.25),int( Y*0.25)))

            # Definir posición de las imágenes
            image1_rect = image1.get_rect(center=(int(X*0.5),int( Y/5.4545454)))
            # correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
            # incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
            aux_r=random.random()
            if aux_r<0.7:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
            else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.7148)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
                            
            # Reiniciar banderas
            correct_image_clicked = False
            incorrect_image_clicked = False                
            counter +=1
            time_since_last_click=0
            time_without_click=0
            last_click_time =  pygame.time.get_ticks() 
        else:
            print("\n")
        # Dibujar tiempo
        

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

        counting_text = font.render(str(counting_string), 1, (255,255,255))
        counting_rect = counting_text.get_rect(center = window.get_rect().center)

        # Dibujar imágenes en la ventana
        window.blit(image1, image1_rect)
        window.blit(correct_image, correct_image_rect)
        window.blit(incorrect_image, incorrect_image_rect)
        window.blit(counting_text, counting_rect)
        

        # Actualizar pantalla
        pygame.display.update()  
        clock.tick(25)   
        if counter == 7:
            time.sleep(0.5)
            running = False   
    print("----------------------Fin de juego----------------------\n\n\n")
    print("------------------------------------------------")



    print("Tiempo total:",(counting_string))
    pygame.quit()

    t_mean=int(statistics.mean(question_times))

    if Name=="":Name="test"
    basic_encrypt=[ord(x)+17 for x in list(Name)]
    ID_enmcr=basic_encrypt
    # print(ID_enmcr)
    #print([chr(x-17) for x in ID_enmcr])
    # change milliseconds into minutes, seconds, milliseconds
    counting_minutes = str(t_mean//60000).zfill(2)
    counting_seconds = str( (t_mean%60000)//1000 ).zfill(2)
    counting_millisecond = str(t_mean%1000).zfill(3)

    meadia_counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)



    # Data to be written
    if lang=="":lang="esp"
    dictionary = {
        "name": ID_enmcr,
        "time-stamp":str(datetime.datetime.now()),
        "execution-time": counting_string,
        "avg-test-time": meadia_counting_string,
        "aciertos": aciertos,
        "fallos": fallos,
        "omisiones": omision,
        "multi-idioma":lang,
        "Version":VERSION,
        "SO":platform.system()
    }
    print(question_times)
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("ST_data.json", "w") as outfile:
        outfile.write(json_object)
