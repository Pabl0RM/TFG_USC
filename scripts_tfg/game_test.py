import pygame,time,os,random,json,statistics,datetime,platform,subprocess,sys
from pygame.locals import *
import encuestas
global namee
def mmain(Name,lang,VERSION,IP_port):
    # Inicializa Pygame
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)
    start_time = pygame.time.get_ticks() 
    question_times=[]
    aciertos=0
    fallos=0
    omision=0
    acumulativo=0
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
    image1_rect = image1.get_rect(center=(int(X*0.5),int( Y/3.5545454)))
    aux_r=random.random()
    if aux_r<0.7:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.4)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.4)))
    else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.4)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.4)))

    # Banderas para verificar si se hizo clic en una imagen (int(X/1.23),int( Y/1.7148))
    correct_image_clicked = False
    incorrect_image_clicked = False



    running = True
    max_time_without_click = 10

    # tiempo actual sin clic
    time_without_click = 0
    last_click_time=start_time
    counter+=1
    feedback=(window.get_width()//2,(window.get_height()//2)+100)
    
    
    while running:
        counting_time = pygame.time.get_ticks() - start_time-acumulativo
        # print(counting_time)
        
        # window.blit(bg_image, (0, 0))
        
        # counting_minutes = str(counting_time//60000).zfill(2)
        # counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        # counting_millisecond = str(counting_time%1000).zfill(3)

        # counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)            
        # print(counting_string)        
        
        
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
                if ((correct_image_clicked ) or incorrect_image_clicked) and counter <=len(contiene_c):
                    
                    window.blit(image1, image1_rect)
                    window.blit(correct_image, correct_image_rect)
                    window.blit(incorrect_image, incorrect_image_rect)              
                    
                    if (correct_image_clicked ) and counter <=4:
                        print("correcta")
                        question_times.append(counting_time)
                        aciertos+=1                     
                        pygame.draw.rect(window, (0, 255, 0), incorrect_image_rect, 10)
                        pygame.draw.rect(window, (0, 255, 0), image1_rect, 10)
                        counting_string2="Imagen correcta"
                        counting_text2 = font.render(str(counting_string2), 1, (0,0,0))
                        counting_rect2 = counting_text2.get_rect(center = feedback)
                        window.blit(counting_text2, counting_rect2)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        subprocess.run(["python", "feedbackPepper-tablet/pruebaPepper_03.py",IP_port])
                        acumulativo+=pygame.time.get_ticks()-aux

                    if incorrect_image_clicked and counter <=4:
                        print("incorrecta")
                        question_times.append(counting_time)
                        fallos+=1                     
                        pygame.draw.rect(window, (255, 0, 0), correct_image_rect, 10)
                        pygame.draw.rect(window, (255, 0, 0), image1_rect, 10)
                        counting_string2="No es la imagen correcta"
                        counting_text2 = font.render(str(counting_string2), 1, (0,0,0))
                        counting_rect2 = counting_text2.get_rect(center = feedback)
                        window.blit(counting_text2, counting_rect2)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        subprocess.run(["python", "feedbackPepper-tablet/pruebaPepper_02.py",IP_port])                    
                        acumulativo+=pygame.time.get_ticks()-aux
                        


                    if (correct_image_clicked ) and counter >=5:
                        question_times.append(counting_time)
                        aciertos+=1                    
                        print("click")
                        pygame.draw.rect(window, (155,155,155), incorrect_image_rect, 10)
                        pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        pygame.time.wait(3000)
                        acumulativo+=pygame.time.get_ticks()-aux
                        

                    
                    if incorrect_image_clicked and counter>=5:
                        question_times.append(counting_time)
                        fallos+=1                        
                        pygame.draw.rect(window, (155,155,155), correct_image_rect, 10)
                        pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        pygame.time.wait(3000)
                        acumulativo+=pygame.time.get_ticks()-aux                  
                    
                                                
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
                        image1_rect  = image1.get_rect(center=(int(X*0.5),int( Y/3.5545454)))
                        # correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
                        # incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
                        aux_r=random.random()
                        if aux_r<0.7:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.4)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.4)))
                        else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.4)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.4)))

                        # # Reiniciar banderas
                        correct_image_clicked = False
                        incorrect_image_clicked = False
                        counter += 1
                        # print(counting_time)
                        # counting_time=counting_time-2000
                        if (correct_image_clicked ) and counter >=5:
                            question_times.append(counting_time)
                            aciertos+=1                    
                            print("click")
                            pygame.draw.rect(window, (155,155,155), incorrect_image_rect, 10)
                            pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                            pygame.display.update()
                            pygame.time.wait(1500)
                            acumulativo+=pygame.time.get_ticks()-1500
                        

                    
                        if incorrect_image_clicked and counter>=5:
                            question_times.append(counting_time)
                            fallos+=1                        
                            pygame.draw.rect(window, (155,155,155), correct_image_rect, 10)
                            pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                            pygame.display.update()
                            pygame.time.wait(1500)   
                            acumulativo+=pygame.time.get_ticks()-1500
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
            counting_text_time = font.render(str(counting_string_time), 1, (0,0,0))
            counting_rect_time = counting_text_time.get_rect(center = feedback)
            window.blit(counting_text_time, counting_rect_time)
            pygame.display.update()
            pygame.time.wait(2500)     
            
                    
            image1 = pygame.image.load(contiene_c[counter])
            correct_image = pygame.image.load(contiene_incorrecta[counter])
            incorrect_image = pygame.image.load(contiene_correcta[counter])
            
            image1 = pygame.transform.smoothscale(image1, (int(X*0.5),int( Y*.5)))
            correct_image = pygame.transform.smoothscale(correct_image, (int(X*0.25),int( Y*0.25)))
            incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(X*0.25),int( Y*0.25)))

            # Definir posición de las imágenes
            image1_rect =  image1.get_rect(center=(int(X*0.5),int( Y/3.5545454)))

            # correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
            # incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
            aux_r=random.random()
            if aux_r<0.7:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.4)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.4)))
            else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.4)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.4)))
                    
            # Reiniciar banderas
            correct_image_clicked = False
            incorrect_image_clicked = False                
            counter +=1
            time_since_last_click=0
            time_without_click=0
            last_click_time =  pygame.time.get_ticks() 
        else:
            print("")
        # Dibujar tiempo
        

        # change milliseconds into minutes, seconds, milliseconds
        # counting_time = pygame.time.get_ticks() - start_time
        # print('finito',counting_time)
        
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

        counting_text = font.render(str(counting_string), 1, (0,0,0))
        counting_rect = counting_text.get_rect(center = feedback)

        # Dibujar imágenes en la ventana
        window.blit(image1, image1_rect)
        window.blit(correct_image, correct_image_rect)
        window.blit(incorrect_image, incorrect_image_rect)
        window.blit(counting_text, counting_rect)
        
  

        # Actualizar pantalla
        pygame.display.update()  
        clock.tick(100)   
        if counter == len(contiene_c)+1:
            if (correct_image_clicked ) and counter >=5:
                question_times.append(counting_time)
                aciertos+=1                    
                print("click")
                pygame.draw.rect(window, (155,155,155), incorrect_image_rect, 10)
                pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                pygame.display.update()
                pygame.time.wait(1500)
            

        
            if incorrect_image_clicked and counter>=5:
                question_times.append(counting_time)
                fallos+=1                        
                pygame.draw.rect(window, (155,155,155), correct_image_rect, 10)
                pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                pygame.display.update()
                pygame.time.wait(1500) 


            # Actualizar pantalla
            pygame.display.update()  
            # time.sleep(1.5)
            running = False   
            print(counting_time)
        
        window.blit(bg_image, (0, 0))
        
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)            
        print(counting_string) 
        print(acumulativo) 
    print("----------------------Fin de juego----------------------\n\n\n")
    print("------------------------------------------------")


    try:
        t_mean=int(statistics.mean(question_times))
    except:
        t_mean=0
    if Name=="":Name="test"
    
    ID_enmcr=Name
    # change milliseconds into minutes, seconds, milliseconds
    counting_minutes = str(t_mean//60000).zfill(2)
    counting_seconds = str( (t_mean%60000)//1000 ).zfill(2)
    counting_millisecond = str(t_mean%1000).zfill(3)

    meadia_counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)



    # Data to be written
    if lang=="":lang="esp"



    formula=str(aciertos*0.1+3*0.5+(fallos+omision)*0.5)




    window.blit(bg_image, (0, 0))
    # Definir las variables a mostrar
    variable_1 = "Tiempo total: " +counting_string
    variable_2 = "Tiempo medio: " +str(meadia_counting_string)
    variable_3 = "Idioma: " +lang
    variable_4 = "Aciertos: " +str(aciertos)
    variable_5 = "Fallos: " +str(fallos)
    variable_6 = "Omisiones: " +str(omision)
    variable_7 = "Puntuacion: " +formula


            # Definir las dimensiones del rectángulo
    rect_width = 350
    rect_height = 400
    aux=150

    # Crear el rectángulo de color negro
    rect = pygame.Surface((rect_width, rect_height))
    rect.fill((17, 177, 177))

    # Renderizar el rectángulo en la ventana
    window.blit(rect, ((window.get_width()//2)-50, aux ))


    # Definir el color del texto
    text_color = (0, 0, 0)

    ancho_pantalla = window.get_width()
#   Renderizar las variables en la ventana
    variable_1_text = font.render(str(variable_1), True, text_color)
    window.blit(variable_1_text, (ancho_pantalla//2,aux+ 50))

    variable_2_text = font.render(str(variable_2), True, text_color)
    window.blit(variable_2_text, (ancho_pantalla//2,aux+ 100))

    variable_3_text = font.render(str(variable_3), True, text_color)
    window.blit(variable_3_text, (ancho_pantalla//2,aux+ 150))

    variable_4_text = font.render(str(variable_4), True, text_color)
    window.blit(variable_4_text, (ancho_pantalla//2,aux+ 200))

    variable_5_text = font.render(str(variable_5), True, text_color)
    window.blit(variable_5_text, (ancho_pantalla//2,aux+ 250))
    variable_6_text = font.render(str(variable_6), True, text_color)
    window.blit(variable_6_text, (ancho_pantalla//2,aux+ 300))

    variable_7_text = font.render(str(variable_7), True, text_color)
    window.blit(variable_7_text, (ancho_pantalla//2,aux+ 350))    
    pygame.time.wait(5000)    
    # Actualizar pantalla
    pygame.display.update()    

    print("Tiempo total:",(counting_string))
    pygame.time.wait(1500)  
    #encuestas
    
    results=encuestas

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

    # Writing to sample.jsonn
    with open("ST_data.json", "w") as outfile:
        outfile.write(json_object)
        

        
    print(ID_enmcr)
    subprocess.run(["python3", "firebase_waits.py",ID_enmcr])
    pygame.quit()