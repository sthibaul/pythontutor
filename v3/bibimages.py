#-*- coding: utf-8 -*-

from PIL.Image import *


class __ErreurParametre (TypeError):
    def __init__(self, arg, param):
        self.arg = arg
        self.param = param
    def __str__(self):
        # affichage discutable
        if type (self.arg) == str:
            strArg = "'" + self.arg + "'"
        else:
            strArg = str (self.arg)
        return "\n\n" + strArg + " n'est pas " + self.param

def __verif_type_image(i):
    if not "Image" in i.__class__.__name__:
        raise __ErreurParametre(i, "une image")

def __verif_type_chaine(s):
    if type(s) != str:
        raise __ErreurParametre(s, "un nom d'image")

def __verif_type_entier(i):
    if i.__class__.__name__ != 'int':
        raise __ErreurParametre(i, "un entier")

def __verif_type_coord(c):
    if c.__class__.__name__ != 'tuple':
        raise __ErreurParametre(c, "des coordonnées")
    if c.__len__() != 2:
        raise __ErreurParametre(c, "des coordonnées avec 2 composantes")
    if c[0].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "des coordonnées entières")
    if c[1].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "des coordonnées entières")

def __verif_type_couleur(c):
    if c.__class__.__name__ != 'tuple':
        raise __ErreurParametre(c, "une couleur")
    if c.__len__() != 3:
        raise __ErreurParametre(c, "une couleur avec 3 composantes")
    if c[0].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "une couleur avec 3 composantes entières")
    if c[1].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "une couleur avec 3 composantes entières")
    if c[2].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "une couleur avec 3 composantes entières")

def ouvrirImage(nom):
    """ Ouvre le fichier nom et retourne l’image contenue de dans (par exemple open('teapot.png') """
    __verif_type_chaine(nom)
    return open(nom)

def ecrireImage(img, nom):
    """Sauvegarde l’image img dans le fichier nom """
    __verif_type_image(img)
    __verif_type_chaine(nom)
    Image.save(img, nom)

def nouvelleImage(largeur, hauteur):
    """ Retourne une image de taille largeur × hauteur, initialement noire """
    __verif_type_entier(largeur)
    __verif_type_entier(hauteur)
    return new ("RGB", (largeur, hauteur))

def afficherImage(img):
    """ Affiche l’image img """
    __verif_type_image(img)
    Image.show(img)

def largeurImage(img):
    """ Récupère la largeur de img """
    __verif_type_image(img)
    return img.width

def hauteurImage(img):
    """ Récupère la hauteur de img """
    __verif_type_image(img)
    return img.height


def colorierPixel(img, coord, couleur):
    """ Peint le pixel coord dans l’image img de la couleur couleur
    Exemple d'utilisation :
    >>> coloriderPixel(nouvelleImage(300,200), (50,50), (255,255,255))
    """
    __verif_type_image(img)
    __verif_type_coord(coord)
    __verif_type_couleur(couleur)
    Image.putpixel(img, coord, couleur)

def couleurPixel (img, coord):
    """ Retourne la couleur du pixel (x, y) dans l’image img
    Exemple d'utilisation :
    >>> couleur = couleurPixel(nouvelleImage(300,200), (50,50))
    """
    __verif_type_image(img)
    __verif_type_coord(coord)
    return Image.getpixel(img, coord)
    
