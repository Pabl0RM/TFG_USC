import os

img_folder = "imgs/"
for filename in os.listdir(img_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        new_name = ""
        for i in range(len(filename)):
            if filename[i].isdigit() and (i == 0 or not filename[i-1].isdigit()):
                new_name += "0" + filename[i]
            else:
                new_name += filename[i]
        os.rename(os.path.join(img_folder, filename), os.path.join(img_folder, new_name))