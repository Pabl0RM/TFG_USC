import pygame,time,os,random,json,statistics,datetime,platform,subprocess,sys
from pygame.locals import *

global namee
picto=0


def mmain(Name,lang,VERSION,IP_port,vol,mode):
    # Inicializa Pygame
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Helvetica', 40)
    font_textual = pygame.font.SysFont('Helvetica', 120)
    start_time = pygame.time.get_ticks() 
    question_times=[]
    aciertos=0
    fallos=0
    omision=0
    acumulativo=0
    # Definir tamaño de la ventana
    A=512
    B=512


    X,Y = pygame.display.set_mode().get_size()
    window = pygame.display.set_mode((X, Y),RESIZABLE)
    scale=0.91


    # Crear superficie de fondo degradado
    background = pygame.Surface(window.get_size())
    background = background.convert()
    # Cargar la imagen de fondo
    
    bg_image = pygame.image.load('fondo1.png')
    pastel=True;verde_pastel=(0,114,119)
    # Escalar la imagen al tamaño de la ventana
    bg_image = pygame.transform.scale(bg_image, window.get_size())

    # Cargar imágenes

    img_folder = "imgs-IA/"

    # Obtener una lista de los nombres de archivo de todas las imágenes en la carpeta
    img_paths = sorted([img_folder+f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f)) and f.endswith('.png')]    )
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
    # print("Los elementos que contienen 'c'entral son:", len(contiene_c))
    # print("Los elementos que contienen 'incorrecta' son:", len(contiene_incorrecta))
    # print("Los elementos que contienen 'correcta' son:", len(contiene_correcta))
    # print(contiene_c[A])
    # print(contiene_incorrecta[A])
    # print(contiene_correcta[A])
    # exit()
    print(contiene_c)
    last_words_c = [image_name.split("_")[-1].split(".")[0] for image_name in contiene_c]
    last_words_incorrecta = [image_name.split("_")[-1].split(".")[0] for image_name in contiene_incorrecta]
    last_words_correcta = [image_name.split("_")[-1].split(".")[0] for image_name in contiene_correcta]    

    if mode=="img" :
        image1 = pygame.image.load(contiene_c[counter])
        correct_image = pygame.image.load(contiene_incorrecta[counter])
        incorrect_image = pygame.image.load(contiene_correcta[counter])

        # Definir tamaño de las imágenes (int(A*scale), int(B*scale)))
        image1 = pygame.transform.smoothscale(image1, (int(A*scale), int(B*scale)))
        correct_image = pygame.transform.smoothscale(correct_image, (int(A*scale), int(B*scale)))
        incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(A*scale), int(B*scale)))
    else:
        image1 = pygame.Surface((int(A*scale), int(B*scale)))
        correct_image = pygame.Surface((int(A*scale), int(B*scale)))
        incorrect_image = pygame.Surface((int(A*scale), int(B*scale)))   
    #pict(window,contiene_c,contiene_correcta,contiene_incorrecta,counter)
    # Definir posición de las imágenes
    image1_rect = image1.get_rect(center=(int(X*0.5),int( Y/3.5545454)))
    aux_r=random.random()
    print('aux 1',aux_r)
    if aux_r<0.5:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.55)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.55)))
    else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.55)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.55)))

    # Banderas para verificar si se hizo clic en una imagen (int(X/1.23),int( Y/1.7148))
    correct_image_clicked = False
    incorrect_image_clicked = False


    running = True
    max_time_without_click = 8

    # tiempo actual sin clic
    time_without_click = 0
    last_click_time=start_time
    counter+=1
    feedback=(window.get_width()//2,(window.get_height()//2)+160)
    
    picto=0
    while running:
        counting_time = pygame.time.get_ticks() - start_time-acumulativo


       
        
        
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
                    #pict(window,contiene_c,contiene_correcta,contiene_incorrecta,counter)
                    if mode=="text":
                        
                        text_surface_c = font_textual.render(last_words_c[counter], True, (255, 255, 255))
                        text_rect_c = text_surface_c.get_rect(center=(image1_rect.centerx, image1_rect.centery))
                        window.blit(text_surface_c, text_rect_c)

                        text_surface_incorrecta = font_textual.render(last_words_incorrecta[counter], True, (255, 255, 255))
                        text_rect_incorrecta = text_surface_incorrecta.get_rect(center=(correct_image_rect.centerx, correct_image_rect.centery))
                        window.blit(text_surface_incorrecta, text_rect_incorrecta)

                        text_surface_correcta = font_textual.render(last_words_correcta[counter], True, (255, 255, 255))
                        text_rect_correcta = text_surface_correcta.get_rect(center=(incorrect_image_rect.centerx, incorrect_image_rect.centery))
                        window.blit(text_surface_correcta, text_rect_correcta) 



                    
                    if (correct_image_clicked ) and counter <=4:
                        print("correcta")
                        question_times.append(counting_time)
                        aciertos+=1                     
                        pygame.draw.rect(window, (0, 255, 0), incorrect_image_rect, 10)
                        pygame.draw.rect(window, (0, 255, 0), image1_rect, 10)
                        counting_string2="Imagen correcta"
                        counting_text2 = font.render(str(counting_string2), 1, (0, 255, 0))
                        counting_rect2 = counting_text2.get_rect(center = feedback)
                        window.blit(counting_text2, counting_rect2)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        subprocess.run(["python", "feedbackPepper-tablet/pruebaPepper_03.py",IP_port,vol])
                        acumulativo+=pygame.time.get_ticks()-aux

                    if incorrect_image_clicked and counter <=4:
                        print("incorrecta")
                        question_times.append(counting_time)
                        fallos+=1                     
                        pygame.draw.rect(window, (255, 0, 0), correct_image_rect, 10)
                        pygame.draw.rect(window, (255, 0, 0), image1_rect, 10)
                        counting_string2="No es la imagen correcta"
                        counting_text2 = font.render(str(counting_string2), 1, (255, 0, 0))
                        counting_rect2 = counting_text2.get_rect(center = feedback)
                        window.blit(counting_text2, counting_rect2)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        subprocess.run(["python", "feedbackPepper-tablet/pruebaPepper_02.py",IP_port,vol])                    
                        acumulativo+=pygame.time.get_ticks()-aux
                        


                    if (correct_image_clicked ) and counter >=5:
                        question_times.append(counting_time)
                        aciertos+=1                    
                        print("click")
                        pygame.draw.rect(window, (155,155,155), incorrect_image_rect, 10)
                        pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        pygame.time.wait(3500)
                        acumulativo+=pygame.time.get_ticks()-aux
                        

                    
                    if incorrect_image_clicked and counter>=5:
                        question_times.append(counting_time)
                        fallos+=1                        
                        pygame.draw.rect(window, (155,155,155), correct_image_rect, 10)
                        pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                        pygame.display.update()
                        aux=pygame.time.get_ticks()
                        pygame.time.wait(3500)
                        acumulativo+=pygame.time.get_ticks()-aux                  
                    
                                                
                    try:                  
                        # image1 = pygame.image.load(img_paths[counter * 3 - 2])
                        # correct_image = pygame.image.load(img_paths[counter * 3 - 1])
                        # incorrect_image = pygame.image.load(img_paths[counter*3])
                        if mode=="img":
                            image1 = pygame.image.load(contiene_c[counter])
                            correct_image = pygame.image.load(contiene_incorrecta[counter])
                            incorrect_image = pygame.image.load(contiene_correcta[counter])

                            image1 = pygame.transform.smoothscale(image1, (int(A*scale), int(B*scale)))
                            correct_image = pygame.transform.smoothscale(correct_image, (int(A*scale), int(B*scale)))
                            incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(A*scale), int(B*scale)))
                        else:
                            image1 = pygame.Surface((int(A*scale), int(B*scale)))
                            correct_image = pygame.Surface((int(A*scale), int(B*scale)))
                            incorrect_image = pygame.Surface((int(A*scale), int(B*scale)))  
                        #pict(window,contiene_c,contiene_correcta,contiene_incorrecta,counter)
                        # Definir posición de las imágenes
                        image1_rect  = image1.get_rect(center=(int(X*0.5),int( Y/3.5545454)))
                        # correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
                        # incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
                        aux_r=random.random()
                        print('aux 2',aux_r)
                        if aux_r<0.5:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.55)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.55)))
                        else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.55)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.55)))

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
                            pygame.time.wait(2000)
                            acumulativo+=pygame.time.get_ticks()-2000
                        

                    
                        if incorrect_image_clicked and counter>=5:
                            question_times.append(counting_time)
                            fallos+=1                        
                            pygame.draw.rect(window, (155,155,155), correct_image_rect, 10)
                            pygame.draw.rect(window, (155,155,155), image1_rect, 10)
                            pygame.display.update()
                            pygame.time.wait(2000)   
                            acumulativo+=pygame.time.get_ticks()-2000
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
            counting_rect_time = counting_text_time.get_rect(center = feedback)
            window.blit(counting_text_time, counting_rect_time)
            pygame.display.update()
            # pygame.time.wait(2500)     
            # acumulativo+=pygame.time.get_ticks()-2500
            aux=pygame.time.get_ticks()
            pygame.time.wait(3500)
            acumulativo+=pygame.time.get_ticks()-aux    

            if mode=="img":
                image1 = pygame.image.load(contiene_c[counter])
                correct_image = pygame.image.load(contiene_incorrecta[counter])
                incorrect_image = pygame.image.load(contiene_correcta[counter])

                image1 = pygame.transform.smoothscale(image1, (int(A*scale), int(B*scale)))
                correct_image = pygame.transform.smoothscale(correct_image, (int(A*scale), int(B*scale)))
                incorrect_image = pygame.transform.smoothscale(incorrect_image, (int(A*scale), int(B*scale)))
            else:
                image1 = pygame.Surface((int(A*scale), int(B*scale)))
                correct_image = pygame.Surface((int(A*scale), int(B*scale)))
                incorrect_image = pygame.Surface((int(A*scale), int(B*scale))) 

            # Definir posición de las imágenes
            image1_rect =  image1.get_rect(center=(int(X*0.5),int( Y/3.5545454)))

            # correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.7148)))
            # incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.7148)))
            aux_r=random.random()
            print('aux 3',aux_r)
            if aux_r<0.5:correct_image_rect = correct_image.get_rect(center=(int(X/5.33333),int( Y/1.55)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/1.23),int( Y/1.55)))
            else:correct_image_rect = correct_image.get_rect(center=(int(X/1.23),int( Y/1.55)));incorrect_image_rect = incorrect_image.get_rect(center=(int(X/5.33333),int( Y/1.55)))
                    
            # Reiniciar banderas
            correct_image_clicked = False
            incorrect_image_clicked = False                
            counter +=1
            time_since_last_click=0
            time_without_click=0
            last_click_time =  pygame.time.get_ticks() 
        else:
            pass
        # Dibujar tiempo
        

        # change milliseconds into minutes, seconds, milliseconds
        # counting_time = pygame.time.get_ticks() - start_time
        # print('finito',counting_time)
        
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

        counting_text = font.render(str(counting_string), 1, (255,255,255))
        counting_rect = counting_text.get_rect(center = feedback)

        # Dibujar imágenes en la ventana
        # pict(window,contiene_c,contiene_correcta,contiene_incorrecta,counter)
        window.blit(image1, image1_rect)
        window.blit(correct_image, correct_image_rect)
        window.blit(incorrect_image, incorrect_image_rect)
        window.blit(counting_text, counting_rect)
        if mode=="text":
            try:
                text_surface_c = font_textual.render(last_words_c[counter], True, (255, 255, 255))
                text_rect_c = text_surface_c.get_rect(center=(image1_rect.centerx, image1_rect.centery))
                window.blit(text_surface_c, text_rect_c)

                text_surface_incorrecta = font_textual.render(last_words_incorrecta[counter], True, (255, 255, 255))
                text_rect_incorrecta = text_surface_incorrecta.get_rect(center=(correct_image_rect.centerx, correct_image_rect.centery))
                window.blit(text_surface_incorrecta, text_rect_incorrecta)

                text_surface_correcta = font_textual.render(last_words_correcta[counter], True, (255, 255, 255))
                text_rect_correcta = text_surface_correcta.get_rect(center=(incorrect_image_rect.centerx, incorrect_image_rect.centery))
                window.blit(text_surface_correcta, text_rect_correcta)        
            except:
                print(counter)
                print(len(contiene_c)+1)
                picto=1                  

  

        # Actualizar pantalla
        pygame.draw.rect(window, (0,0,0), correct_image_rect, 10)
        pygame.draw.rect(window, (0,0,0), incorrect_image_rect, 10)
        pygame.draw.rect(window, (0,0,0), image1_rect, 10)        
        pygame.display.update()  
        clock.tick(100)   
        if counter >len(contiene_c) or picto:
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
        
        if pastel:window.fill(verde_pastel)
        else:window.blit(bg_image, (0, 0))
        
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)            
        if counting_time%1000==0:print(counting_string);print(acumulativo) 
        
    print("----------------------Fin de juego----------------------\n\n\n")
   


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




    import pygame_menu

    encuesta = pygame_menu.Menu('Analisis',X,Y,  theme=pygame_menu.themes.THEME_DARK)

    variables = [variable_1,variable_2,variable_3,variable_4,variable_5,variable_6,variable_7]

    for variable in variables:
        encuesta.add.label(variable, align=pygame_menu.locals.ALIGN_CENTER,font_size=70)

    def back():
        a=False
        encuesta.clear()
        print("Tiempo total:",(counting_string))
 
        #encuestas

        dictionary = {
            "name": ID_enmcr,
            "time_stamp":str(datetime.datetime.now()),
            "execution_time": counting_string,
            "avg_test_time": meadia_counting_string,
            "aciertos": aciertos,
            "fallos": fallos,
            "puntuacion":formula,
            "omisiones": omision,
            "multi_idioma":lang,
            "Version":VERSION,
            "SO":platform.system()
        }
        print(question_times)
        # Serializing json
        json_object = json.dumps(dictionary, indent=4)

        # Writing to sample.jsonn
        with open("ST_data.json", "w") as outfile:
            outfile.write(json_object)
        pygame.display.quit()
        with open("tmpp.txt", "w") as outfile:
            outfile.write(IP_port)    
        import encuestas
        encuestas.main(vol)
        

    encuesta.add.button('Encuesta', back,font_size=70)
    a=True
    while a:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        encuesta.update(events)
        
        encuesta.draw(window)
        pygame.display.flip()












  
    # Actualizar pantalla
    pygame.display.update()    

    print("Tiempo total:",(counting_string))
 
    #encuestas
    

    
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
    pygame.display.quit()
    with open("tmpp.txt", "w") as outfile:
        outfile.write(IP_port)    
    import encuestas
    encuestas.main(vol)
    
# mmain('proba','proba','proba','localhost:35677','0.666','img')