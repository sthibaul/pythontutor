# coding=utf-8

from graphes import *
import os, platform, subprocess, glob, resource, tempfile


plateforme = platform.system ()

def _getGraphViz():
  if plateforme == 'Windows':
      l = glob.glob('C:/Program Files*/Graphviz*/bin/dot.exe')
      if l == []:
          print("Graphviz non trouve, veuillez l'installer")
          sys.exit(1)
      path = l[0]
      return path[0:-7]
  else:
      l = glob.glob('/usr/bin/dot')
      if l == []:
          l = glob.glob('/usr/local/bin/dot')
          if l == []:
              l = glob.glob('/opt/local/bin/dot')
              if l == []:
                  print("Graphviz non trouve, veuillez l'installer")
                  sys.exit(1)
      path = l[0]
      return path[0:-3]

pathGraphviz = _getGraphViz()

############### Dessin du graphe  #####################

# fonction necessaire a cause par exemple des 'Pays Bas' (blanc dans label)
def _proteger (label):
    return '"' + label + '"'

# La fonction 'dotify' transforme le graphe en un fichier texte
# qui servira de source (suffixe .dot) pour les programmes de Graphviz.
# Cette fonction ne depend pas du systeme d'exploitation.

def dotify (G, etiquettesAretes = True, colormark = 'Black', suffixe = 'dot'):

    (soft,maximum) = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft == 0:
        resource.setrlimit(resource.RLIMIT_NOFILE, (maximum,maximum))

    # graphe non oriente, il faut eviter de traiter chaque arete deux fois
    for s in G.nodes:
        for a in s.edges:
            a.ecrite = False
            
    if G.label == '':
        nom_graphe = 'G'
    else:
        nom_graphe = G.label

    (fd,graph_dot) = tempfile.mkstemp('.dot')
    os.close(fd)
    #graph_dot = '/tmp/' + nom_graphe + '.' + suffixe
    #    
    #try:
    #    f = open (graph_dot, 'w')
    #except IOError:
    #    os.mkdir ('/tmp')
    f = open (graph_dot, 'w')
        
    f.write ('graph "' + nom_graphe + '" {\n' + G.drawopts + '\n')

    for s in G.nodes:
        d = len (s.edges)
        snom = _proteger (s.label)
        for a in s.edges:
            if not a.ecrite:
                a.ecrite = True
                if a.start == s:
                    t = a.end
                else:
                    t = a.start
                f.write ('  ' + snom + ' -- ' + _proteger (t.label))
                if etiquettesAretes:
                    f.write (' [label = ' + _proteger (a.label) + ']')
                if a.mark:
                    f.write (' [style = bold, color = orange]')
                # Semicolons aid readability but are not required (dotguide.pdf)
                f.write (a.drawopts + ';\n')
        bord = 'black'
        if s.mark:
            entoure = 2
            bord = colormark
        else:
            entoure = 1
        if s.color:
            if s.color == "black":
                fontcolor = "white"
            else:
                fontcolor = "black"
            f.write ('  %s [style = filled, peripheries = %s, fillcolor = %s, fontcolor = %s, color = %s] %s;\n' %
                     (snom, entoure, s.color, fontcolor, bord, s.drawopts))
        elif s.mark:
##            f.write ('  ' + snom + ' [peripheries = 2, color = ' + bord + ']' +
##                     s.drawopts + ';\n');
            f.write ('  %s [peripheries = 2, color = %s] %s;\n' %
                     (snom, bord, s.drawopts))
        elif d == 0 or s.drawopts:
            f.write ('  ' + snom + s.drawopts + ';\n')
            
    f.write ('}\n')
    f.close ()
    if soft == 0:
        resource.setrlimit(resource.RLIMIT_NOFILE, (0,maximum))
    return graph_dot

# La fonction 'Graphviz' lance l'execution d'un programme
# de la distribution Graphviz (dot, neato, twopi, circo, fdp)
# pour transformer un fichier texte source de nom 'racine.suffixe'
# en une image de nom 'racine.format' (peut-etre un fichier PostScript)

def Graphviz (source, algo = 'dot', format = 'svg', suffixe = 'dot'):
    (soft,maximum) = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft == 0:
        resource.setrlimit(resource.RLIMIT_NOFILE, (maximum,maximum))
    image = source.replace ('.' + suffixe, '.' + format)
    algo = pathGraphviz + algo
    if plateforme == 'Windows':
        algo = algo + '.exe'
    subprocess.call ([algo, '-T' + format, source, '-o', image])
    if soft == 0:
        resource.setrlimit(resource.RLIMIT_NOFILE, (0,maximum))
    return image


# Enchaine dotify et Graphviz avec des arguments standard adaptes au systeme
# et lance le programme ad hoc pour afficher l'image

def dessinerGraphe (G, etiquettesAretes = False, algo = 'dot', colormark = 'Black'):
    verif_type_graphe (G)
    sys = platform.system ()
    if plateforme == 'Windows':
        # eviter toute embrouille avec les modeles de document de MS Word
        graph_dot = dotify (G, etiquettesAretes, colormark, 'txt')
        image = Graphviz (graph_dot, algo, suffixe = 'txt')
        image = image.replace ('/', '\\')
        os.startfile (image)
        return

    graph_dot = dotify (G, etiquettesAretes, colormark)
    image = Graphviz (graph_dot, algo)
    if plateforme == 'Linux':
        #subprocess.call (['firefox', image])
        subprocess.Popen (['firefox ' + image + ' &'], shell=True)
    elif plateforme == 'Darwin':
        subprocess.call (['open', image])
    else:
        print("Systeme " + plateforme + " imprevu, abandon du dessin")
        
dessiner = dessinerGraphe

