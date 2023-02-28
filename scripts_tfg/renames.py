import os

img_folder =path= "imgs/"

for filename in os.listdir(img_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        new_name = ""
        if '_central' in filename:
            for i in range(len(filename)):
                if filename[i].isdigit() and (i == 0 or not filename[i-1].isdigit()):
                    new_name += "0" + filename[i]
                else:
                    new_name += filename[i]
            os.rename(os.path.join(img_folder, filename), os.path.join(img_folder, new_name))


# import os



# for filename in os.listdir(path):
#     if "c" in filename:
#         new_filename = filename.replace("c", "central")
#         os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
#         print(f"{filename} ha sido renombrado a {new_filename}")


# lista = ['imgs/T_00_Drcha_incorrecta.jpg', 'imgs/T_00_Izq_correcta.jpg', 'imgs/T_00_c.jpg']

contiene_c = []
contiene_incorrecta = []
contiene_correcta = []
print(os.listdir(path))
for elemento in os.listdir(path):
    if '_central' in elemento:
        contiene_c.append(elemento)
    if '_incorrecta' in elemento:
        contiene_incorrecta.append(elemento)
    if '_correcta' in elemento:
        contiene_correcta.append(elemento)

print("Los elementos que contienen 'c' son:", len(contiene_c))
print("Los elementos que contienen 'incorrecta' son:", len(contiene_incorrecta))
print("Los elementos que contienen 'correcta' son:", len(contiene_correcta))
