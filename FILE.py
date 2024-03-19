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

    # Affiche nom avec l'extention, la taille 
    print(file, photo.format , "%d*%d" %photo.size , photo.mode)
except IOError:
    print("Erreur lors de l'ouverture du fichier ")

# convertit les données des pixels de l'image en un tableau NumPy
tableauPixels = np.array(photo)  

# affiche la taille totale du tableau NumPy (nombre total d'éléments dans le tableau)
print(np.size(tableauPixels))

# affiche la forme du tableau NumPy
print(np.shape(tableauPixels))

# récupère les données des pixels de l'image 
pixels = list(photo.getdata())
print(pixels)

# photo.show()

print("Fin propriété Image initial: ")

print("Propriété Image modifiée: ")

# crée une copie indépendante du tableau NumPy
M=np.copy(tableauPixels)

def export(matrice):
    M = im.fromarray(matrice)
    M.save("image/lenaModify.png", "PNG")

def ajouter_50(im):
    largeur, hauteur = im.size

    # Parcours de chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):

            # Récupération de la valeur du pixel
            pixel = im.getpixel((x, y))

            # Ajout de 50 à chaque canal 
            pixel_modifie = min(pixel + 35, 255)

            # Modification du pixel dans l'image
            im.putpixel((x, y), pixel_modifie)
    return im



# Appliquer la fonction ajouter_50 à l'image
M = ajouter_50(photo)

# Afficher les pixels de l'image modifiée
M = list(M.getdata())
print(M)

tableauPixels1 = np.array(photo)
export(tableauPixels1)
# Afficher l'image modifiée
# M.show()
N="image/lenaModify.png"

phot=im.open(N)
phot.show()



