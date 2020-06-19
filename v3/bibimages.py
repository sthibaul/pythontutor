#-*- coding: utf-8 -*-

import PIL.Image

try:
    import isnotebook
    is_notebook = isnotebook.isnotebook()
    if is_notebook:
        print("is notebook")
        import IPython.display
except Exception:
    is_notebook = False



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

def ouvrirImage(nom):
    """ Ouvre le fichier nom et retourne l’image contenue dedans
    Par exemple:

    >>> img = ouvrirImage('teapot.png')"""
    __verif_type_chaine(nom)
    return PIL.Image.open(nom).convert("RGB")

def ecrireImage(img, nom):
    """Sauvegarde l’image img dans le fichier nom
    Par exemple:

    >>> ecrireImage(img, "monimage.png")"""
    __verif_type_image(img)
    __verif_type_chaine(nom)
    PIL.Image.Image.save(img, nom)

def nouvelleImage(largeur, hauteur):
    """ Retourne une image de taille largeur × hauteur, initialement noire
    Par exemple:

    >>> img = nouvelleImage(300,200)"""
    __verif_type_entier(largeur)
    __verif_type_entier(hauteur)
    return PIL.Image.new ("RGB", (largeur, hauteur))

def afficherImage(img):
    """ Affiche l’image img
    Par exemple:

    >>> afficherImage(img)"""
    __verif_type_image(img)
    try:
        if is_notebook:
            IPython.display.display(img)
        else:
            PIL.Image.Image.show(img)
    except Exception:
    	print("Affichage non disponible")

def largeurImage(img):
    """ Récupère la largeur de img
    Par exemple:

    >>> l = largeurImage(img)"""
    __verif_type_image(img)
    return img.width

def hauteurImage(img):
    """ Récupère la hauteur de img
    Par exemple:

    >>> h = hauteurImage(img)"""
    __verif_type_image(img)
    return img.height


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

def couleurPixel (img, x,y):
    """ Retourne la couleur du pixel (x, y) dans l’image img
    Exemple d'utilisation :

    >>> couleur = couleurPixel(img, 50,50)
    """
    __verif_type_image(img)
    __verif_type_entier(x)
    __verif_type_entier(y)
    return img.getpixel((x,y))
    
    
#print("bibimages.py")
