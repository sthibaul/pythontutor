######  This product includes color specifications and designs  ######
######  developed by Cynthia Brewer (http://colorbrewer.org/)   ######

def couleurNumero (palette, n):
    return palette [n % len (palette)]

# Les apostrophes doubles sont nécessaires pour Graphviz
# contrairement aux noms de couleurs comme 'red', 'green', etc.
# On pourrait aussi modifier 'dotify' pour placer systématiquement
# les couleurs entre apostrophes doubles (") 

Set312 = ['"#8dd3c7"', '"#ffffb3"', '"#bebada"', '"#fb8072"',
          '"#80b1d3"', '"#fdb462"', '"#b3de69"', '"#fccde5"',
          '"#d9d9d9"', '"#bc80bd"', '"#ccebc5"', '"#ffed6f"']

Set28 = ['"#66c2a5"', '"#fc8d62"', '"#8da0cb"', '"#e78ac3"',
         '"#a6d854"', '"#ffd92f"', '"#e5c494"', '"#b3b3b3"']

Set19 = ['"#e41a1c"', '"#377eb8"', '"#4daf4a"', '"#984ea3"',
         '"#ff7f00"', '"#ffff33"', '"#a65628"', '"#f781bf"', '"#999999"']

Dark28 = ['"#1b9e77"', '"#d95f02"', '"#7570b3"', '"#e7298a"',
          '"#66a61e"', '"#e6ab02"', '"#a6761d"', '"#666666"']

Accent8 = ['"#7fc97f"', '"#beaed4"', '"#fdc086"', '"#ffff99"',
           '"#386cb0"', '"#f0027f"', '"#bf5b17"', '"#666666"']

_palettes = [Accent8, Dark28, Set28, Set19, Set312]

def paletteNumero (n):
    n = n % len (_palettes)
    return _palettes[n]

print ('Cette  application  utilise  des  schémas  de  couleurs\n\
développés par Cynthia Brewer (http://colorbrewer.org/)')


