#-*- coding: utf-8 -*-
import resource

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

def __verif_type_chaine(s):
    if type(s) != str:
        raise __ErreurParametre(s, "un nom de fichier csv")

def ouvrirCSV(nom):
    """ Ouvre le fichier nom et retourne la liste de nombres contenue dedans (par exemple open('notes.csv') """
    __verif_type_chaine(nom)
    l = ["notes.csv"]
    if not nom in l:
        raise ValueError("Seuls les CSV fournis sont autorisés")
    (soft,maximum) = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft == 0:
        resource.setrlimit(resource.RLIMIT_NOFILE, (maximum,maximum))
    f = open(nom)
    if soft == 0:
        resource.setrlimit(resource.RLIMIT_NOFILE, (0,maximum))
    l = []
    for s in f:
        s = str.replace(s, ",", ".")
        s = str.replace(s, "\r", "")
        s = str.replace(s, "\n", "")
        s = str.replace(s, "\n", "")
        try:
            i = float(s)
        except:
            raise __ErreurParametre(s, "un nombre")
        l.append(i)
    return l
