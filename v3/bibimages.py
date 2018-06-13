#-*- coding: utf-8 -*-

from PIL.Image import *


def ouvrirImage(nom):
    """ Ouvre le fichier nom et retourne l’image contenue de dans (par exemple open('teapot.png') """
    return Image.open(nom)

def ecrireImage(img, nom):
    """Sauvegarde l’image img dans le fichier nom """
    save(img, nom)

def nouvelleImage(largeur, hauteur):
    """ Retourne une image de taille largeur × hauteur, initialement noire """
    return Image.new ("RGB", (largeur, hauteur))

def afficherImage(img):
    """ Affiche l’image img """
    Image.show(img)

def largeurImage(img):
    """ Récupère la largeur de img """
    return img.width

def hauteurImage(img):
    """ Récupère la hauteur de img """
    return img.height


def colorierPixel(img, coord, couleur):
    """ Peint le pixel coord dans l’image img de la couleur couleur
    Exemple d'utilisation :
    >>> coloriderPixel(nouvelleImage(300,200), (50,50), (255,255,255))
    """
    Image.putpixel(img, coord, couleur)

def couleurPixel (img, coord):
    """ Retourne la couleur du pixel (x, y) dans l’image img
    Exemple d'utilisation :
    >>> couleur = couleurPixel(nouvelleImage(300,200), (50,50))
    """
    return Image.getpixel(img, coord)
    
