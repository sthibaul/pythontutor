#-*- coding: utf-8 -*-

import PIL.Image

try:
    import isnotebook
    _is_notebook = isnotebook.isnotebook()
    if _is_notebook:
        print("is notebook")
        import IPython.display
except Exception:
    _is_notebook = False



class __ErreurParametre (TypeError):
    def __init__(self, arg, param):
        self.arg = arg
        self.param = param
    def __str__(self):
        # affichage discutable
        if isinstance(self.arg, str):
            strArg = "'" + self.arg + "'"
        else:
            strArg = str (self.arg)
        return "\n\n" + strArg + " n'est pas " + self.param

def __verif_type_image(i):
    if "Image" not in i.__class__.__name__:
        raise __ErreurParametre(i, "une image")

def __verif_type_chaine(s):
    if not isinstance(s, str):
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

def _errMaj(wrong, right):
    raise Exception("Attention aux majuscules/minuscules: la fonction " + wrong + " n'existe pas, c'est la fonction " + right + " qui existe")

def _errS(wrong, right):
    raise Exception("Attention aux s: la fonction " + wrong + " n'existe pas, c'est la fonction " + right + " qui existe")

def ouvrirImage(nom):
    """ Ouvre le fichier nom et retourne l’image contenue dedans
    Par exemple:

    >>> img = ouvrirImage('teapot.png')"""
    __verif_type_chaine(nom)
    try:
        return PIL.Image.open(nom).convert("RGB")
    except FileNotFoundError as e:
        raise Exception("Attention, le fichier " + nom + " n'existe pas, peut-être le nom est mal écrit, ou bien ce fichier n'est pas dans le même répertoire que le fichier .py ?")

def ouvririmage(nom):
    _errMaj("ouvririmage", "ouvrirImage")
def OuvrirImage(nom):
    _errMaj("OuvrirImage", "ouvrirImage")
def ouvrirImages(nom):
    _errS("ouvrirImages", "ouvrirImage")
def ouvririmages(nom):
    _errS("ouvririmages", "ouvrirImage")

def ecrireImage(img, nom):
    """Sauvegarde l’image img dans le fichier nom
    Par exemple:

    >>> ecrireImage(img, "monimage.png")"""
    __verif_type_image(img)
    __verif_type_chaine(nom)
    PIL.Image.Image.save(img, nom)

def ecrireimage(img, nom):
    _errMaj("ecrireimage", "ecrireImage")
def EcrireImage(img, nom):
    _errMaj("EcrireImage", "ecrireImage")
def ecrireImages(img, nom):
    _errS("ecrireImages", "ecrireImage")
def ecrireimages(img, nom):
    _errS("ecrireimages", "ecrireImage")

def nouvelleImage(largeur, hauteur):
    """ Retourne une image de taille largeur × hauteur, initialement noire
    Par exemple:

    >>> img = nouvelleImage(300,200)"""
    __verif_type_entier(largeur)
    __verif_type_entier(hauteur)
    if largeur > 36:
        raise Exception("Image trop large, le maximum autorisé est 36, pour éviter que ce soit trop lourd")
    if hauteur > 30:
        raise Exception("Image trop haute, le maximum autorisé est 30, pour éviter que ce soit trop lourd")
    return PIL.Image.new ("RGB", (largeur, hauteur))

def nouvelleimage(largeur, hauteur):
    _errMaj("nouvelleimage", "nouvelleImage")
def NouvelleImage(largeur, hauteur):
    _errMaj("NouvelleImage", "nouvelleImage")
def nouvelleImages(largeur, hauteur):
    _errS("nouvelleImages", "nouvelleImage")
def nouvelleimages(largeur, hauteur):
    _errS("nouvelleimages", "nouvelleImage")

def afficherImage(img):
    """ Affiche l’image img
    Par exemple:

    >>> afficherImage(img)"""
    __verif_type_image(img)
    try:
        if _is_notebook:
            IPython.display.display(img)
        else:
            PIL.Image.Image.show(img)
    except Exception:
    	print("Affichage non disponible")

def afficherimage(img):
    _errMaj("afficherimage", "afficherImage")
def AfficherImage(img):
    _errMaj("AfficherImage", "afficherImage")
def afficherImages(img):
    _errS("afficherImages", "afficherImage")
def afficherimages(img):
    _errS("afficherimages", "afficherImage")

def largeurImage(img):
    """ Récupère la largeur de img
    Par exemple:

    >>> l = largeurImage(img)"""
    __verif_type_image(img)
    return img.width

def largeurimage(img):
    _errMaj("largeurimage", "largeurImage")
def LargeurImage(img):
    _errMaj("LargeurImage", "largeurImage")
def largeurImages(img):
    _errS("largeurImages", "largeurImage")
def largeurimages(img):
    _errS("largeurimages", "largeurImage")

def hauteurImage(img):
    """ Récupère la hauteur de img
    Par exemple:

    >>> h = hauteurImage(img)"""
    __verif_type_image(img)
    return img.height

def hauteurimage(img):
    _errMaj("hauteurimage", "hauteurImage")
def HauteurImage(img):
    _errMaj("HauteurImage", "hauteurImage")
def hauteurImages(img):
    _errS("hauteurImages", "hauteurImage")
def hauteurimages(img):
    _errS("hauteurimages", "hauteurImage")


def colorierPixel(img, x,y, couleur):
    """ Peint le pixel de coordonnées (x,y) dans l’image img de la couleur couleur
    Exemple d'utilisation :

    >>> colorierPixel(img, 50,50, (255,255,255))
    """
    __verif_type_image(img)
    __verif_type_entier(x)
    __verif_type_entier(y)
    __verif_type_couleur(couleur)
    img.putpixel((x,y), couleur)

def colorierpixel(img):
    _errMaj("colorierpixel", "colorierPixel")
def ColorierPixel(img):
    _errMaj("ColorierPixel", "colorierPixel")
def colorierPixels(img):
    _errS("colorierPixels", "colorierPixel")
def colorierpixels(img):
    _errS("colorierpixels", "colorierPixel")

def couleurPixel (img, x,y):
    """ Retourne la couleur du pixel (x, y) dans l’image img
    Exemple d'utilisation :

    >>> couleur = couleurPixel(img, 50,50)
    """
    __verif_type_image(img)
    __verif_type_entier(x)
    __verif_type_entier(y)
    return img.getpixel((x,y))
    
def couleurpixel(img):
    _errMaj("couleurpixel", "couleurPixel")
def CouleurPixel(img):
    _errMaj("CouleurPixel", "couleurPixel")
def couleurPixels(img):
    _errS("couleurPixels", "couleurPixel")
def couleurpixels(img):
    _errS("couleurpixels", "couleurPixel")
    
#print("bibimages.py")
