# Pil pour la manipulation d'images
from PIL import Image as im
# NumPy pour le traitement numérique
import numpy as np
# fichier à ouvrir
file="image/lena.gif"
try:

    # Ouvre le fichier image
    photo=im.open(file)
    photo.show()

    print("Propriété Image initial: ")

    # Affiche nom avec l'extention, la taille e

    # print(file, photo.format , "%d*%d" %photo.size , photo.mode)
except IOError:
    print("Erreur lors de l'ouverture du fichier ")

# convertit les données des pixels de l'image en un tableau NumPy
tableauPixels = np.array(photo)  

# affiche la taille totale du tableau NumPy (nombre total d'éléments dans le tableau)
# print(np.size(tableauPixels))

# affiche la forme du tableau NumPy
# print(np.shape(tableauPixels))

# récupère les données des pixels de l'image 
# pixels = list(photo.getdata())
# print(pixels)

# photo.show()

print("Fin propriété Image initial: ")

print("Propriété Image modifiée: ")

# crée une copie indépendante du tableau NumPy
M=np.copy(tableauPixels)

def export(matrice):
    M = im.fromarray(matrice)
    M.save("image/lenaModify.png", "PNG")

def exportImageCat(matrice):
    M = im.fromarray(matrice)
    M.save("image/imgModify.png", "PNG")    

def ajouter_50(im):
    largeur, hauteur = im.size

    # Parcours de chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):

            # Récupération de la valeur du pixel
            pixel = im.getpixel((x, y))

            # Ajout de 50 à chaque canal 
            pixel_modifie = min(pixel + 50, 255)

            # Modification du pixel dans l'image
            im.putpixel((x, y), pixel_modifie)
    return im

def convertToZero(im):
    largeur, hauteur = im.size

    # Parcours de chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):

            # Récupération de la valeur du pixel
            pixel = im.getpixel((x, y))

            if(pixel < 100):
              pixel_modifie = 0

            # Modification du pixel dans l'image
              im.putpixel((x, y), pixel_modifie)
    return im

def convertTozero1(im):
    for i in range(len(im)):
        for j in range(len(im[i])):
            if im[i][j] < 100:
                im[i][j] = 0
    export(im)

convertTozero1(tableauPixels)
# Appliquer la fonction ajouter_50 à l'image
M = ajouter_50(photo)

P = convertToZero(photo)

# Afficher les pixels de l'image modifiée
M = list(M.getdata())
P = list(P.getdata())
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")

tableauPixels1 = np.array(photo)
export(tableauPixels1)
# Afficher l'image modifiée
# M.show()
N="image/lenaModify.png"

phot=im.open(N)
phot.show()

photoCat = "image/img.jpeg"
try:
    photo2 = im.open(photoCat)
    photo2.show()
    
    
    print("image initial :///////////////////")

    # print(photoCat,photo2.format ,"%d*%d" %photo2.size ,photo2.mode)
except:
 IOError
 print("Erreur lors de l'ouverture du fichier/////////")   


tableauPixels2 = np.array(photo2)
print(tableauPixels2)

def color(im):
    for i in range(2):
        im[:,:,i] = 0
    exportImageCat(im)

color(tableauPixels2)


