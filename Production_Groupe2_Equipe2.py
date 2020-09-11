"""
@brief:
    La classe Planete contient toute les informations nécessaire à la création et l'évolution d'une planète au cours de l'animation. Elle encapsule des données qui permettent
    de modulariser et simplifier le code.
"""
class Planete:
    """
    @parameters:
        self     - l'objet courant.
        pos      - tableau contenant la position initiale par rapport à l'origine du repère.
        diametre - diametre de la planète à former.
        centre   - objet centre de rotation. C'est une autre planète, celle autour de laquelle on tourne. Si centre est nul (NULL), cet objet est un étoile.
        color    - tableau contenant les valeurs RGB de la couleur de l'objet.
    @return:
        void.
    @brief:
        Constructeur d'objets de la classe Planete.
    """
    def __init__ (self, pos, diametre, centre, color):
        self.diametre = diametre
        self.centre = centre

        self.pos = {
            'x' : pos[0],
            'y' : pos[1]
        }

        self.color = {
            "r" : color[0],
            "g" : color[1],
            "b" : color[2]
        }

    """
    @parameters:
        self - l'objet courant.
        t - l'angle à appliquer à l'objet courant.
    return:
        void.
    @brief:
        On applique une rotation d'angle t à l'objet courant. Pour cela, on crée la matrice de rotation adéquate (MRot), on met la position de l'objet courant sous forme de matrice
        (MPos) et on multiplie ces deux matrices. Finalement on met à jour la position de l'objet courant en récupérant les nouvelles données dans la matrice résultat (MRes).
        De plus, on met à jour l'information du cosinus du nouvel l'angle formé dans l'objet courant.
    """
    def rotate(self, t):
        MRot = matrix([[cos(t), -sin(t),0],
                       [sin(t),cos(t),0],
                       [0,0,1]
                      ])
        MPos = matrix([[self.pos['x']],
                       [self.pos['y']],
                       [1]
                      ])
        MRes = MRot * MPos

        self.pos = {
            'x' : MRes[0][0],
            'y' : MRes[1][0]
        }

    ############
    #@parameters:
    #    self - l'objet courant.
    #    Tx - la valeur de la transformation à appliquer en abscisse.
    #    Ty - la valeur de la transformation à appliquer en ordonnée.
    #@brief:
    #    On applique une translation à l'objet courant en fonction du couple (Tx,Ty). Pour cela on crée la matrice de translation adéquate (MTra), on met la position de l'objet courant
    #    sous forme de matrice (MPos) et on multiplie ces deux matrices. Finalement on met à jour la position de l'objet courant en récupérant les nouvelles données dans la matrice
    #    résultat ()MRes).
    #@return:
    #    void.
    ############
    def translate(self, Tx, Ty = 0):
        MTra = matrix([[1, 0, Tx],
                       [0, 1, Ty],
                       [0, 0, 1]
                      ])
        MPos = matrix([[self.pos['x']],
                       [self.pos['y']],
                       [1]
                      ])
        MRes = MTra * MPos
        self.pos = {
            'x' : MRes[0][0],
            'y' : MRes[1][0]
        }

    #############
    #@parameters:
    #    self - l'objet courant.
    #@return:
    #    void.
    #@brief:
    #    On déplace le centre de rotation de l'objet courant à l'origine du repère en lui appliquant une translation utilisant la position de l'objet centre de rotation.
    #############
    def translate_to_origin (self):
        MTra = matrix([[1, 0, -self.centre.pos['x']],
                       [0, 1, -self.centre.pos['y']],
                       [0, 0, 1]
                      ])
        MPos = matrix([[self.pos['x']],
                       [self.pos['y']],
                       [1]
                      ])
        MRes = MTra * MPos
        self.pos = {
            'x' : MRes[0][0],
            'y' : MRes[1][0]
        }

    #############
    #@parameters:
    #    self - l'objet courant.
    #@return:
    #    void.
    #@brief:
    #    On déplace le centre de rotation de l'objet courant vers son objet centre de rotation en lui appliquant une translation utilisant la position de l'objet centre de rotation.
    #############
    def translate_to_center (self):
        MTra = matrix([[1, 0, self.centre.pos['x']],
                       [0, 1, self.centre.pos['y']],
                       [0, 0, 1]
                      ])
        MRes = MTra * matrix([[self.pos['x']],[self.pos['y']],[1]])
        self.pos = {
            'x' : MRes[0][0],
            'y' : MRes[1][0]
        }

    #############
    #@parameters:
    #    self - l'objet courant.
    #@return:
    #    Un objet circle.
    #@brief:
    #    On trace un cercle plein, de la couleur de l'objet courant, à l'emplacement de l'objet courant.
    #############
    def draw(self):
        x = self.pos['x']
        y = self.pos['y']
        return circle((x, y), self.diametre/2, fill=True, rgbcolor=(self.color['r']/255, self.color['g']/255, self.color['b']/255))

    #############
    #@parameters:
    #    self - l'objet courant.
    #    planete - la planete avec laquelle on veut vérifier la collision.
    #@return:
    #    Ce que retourne Planete::explode() ou void.
    #@brief:
    #    Si une des bornes de l'axe horizontal de la planete est inclue dans l'intervalle [x-;x+] de l'objet courant où x+ désigne la borne maximale de l'axe horizontal
    #    de l'objet courant et x- la borne minimale, et si une des bornes de l'axe vertical de la planete est inclue dans l'intervalle [y-;y+] de l'objet courant où y+
    #    désigne la borne maximale de l'axe vertical de l'objet courant et y- la borne minimale, alors il y a collision.
    #############
    def collidesWith(self, planete):
        if (((self.pos['x'] - self.diametre/2 < planete.pos['x'] - planete.diametre/2 and planete.pos['x'] - planete.diametre/2 < self.pos['x'] + self.diametre/2)
            or (self.pos['x'] - self.diametre/2 < planete.pos['x'] + planete.diametre/2 and planete.pos['x'] + planete.diametre/2 < self.pos['x'] + self.diametre/2))
            and ((self.pos['y'] - self.diametre/2 < planete.pos['y'] - planete.diametre/2 and planete.pos['y'] - planete.diametre/2 < self.pos['y'] + self.diametre/2)
            or (self.pos['y'] - self.diametre/2 < planete.pos['y'] + planete.diametre/2 and planete.pos['y'] + planete.diametre/2 < self.pos['y'] + self.diametre/2))):
            return true

    #############
    #@parameters:
    #    self - l'objet courant.
    #@return:
    #    Un tableau d'objets de type Planete représentants les fragments produits par une explosion.
    #@brief:
    #    Crée 8 objet de type planète ayant un diamètre 1/8 fois plus petit que l'objet courant et ayant la même couleur que ce dernier.
    #############
    def explode(self):
        firstFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        secondFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        thirdFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        fourthFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        fifthFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        sixthFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        seventhFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        eighthFragment = Planete([self.pos['x'], self.pos['y']], self.diametre/16, self.centre, [self.color['r'], self.color['g'], self.color['b']])
        fragments = [firstFragment, secondFragment, thirdFragment, fourthFragment, fifthFragment, sixthFragment, seventhFragment, eighthFragment]
        return fragments

# Ci-dessous, pos, un dictionnaire contenant la position de départ de chacun des objets du système.
pos = {
    "Soleil" : [0,0],
    "Mercure" : [9, 0],
    "Venus" : [15, 0],
    "Terre" : [25, 0],
    "Lune" : [20, 0],
    "Mars" : [35, 0],
    "Jupiter" : [45, 0],
    "Saturne" : [55, 0],
    "Uranus" : [65, 0],
    "Neptune" : [75, 0],
    "Meteorite" : [-85, 45],
    "TraineeFeuOrange" : [-87, 45],
    "TraineeFeuJaune" : [-89, 45]
}

# Ci-dessous, color, un dictionnaire contenant les valeurs de chacune des composantes RGB de la couleur des objets du sytème.
color = {
    "Espace" : [34, 28, 53],
    "Soleil" : [254, 219, 0],
    "Mercure" : [192, 81, 49],
    "Venus" : [254, 216, 128],
    "Terre" : [0, 118, 165],
    "Lune" : [185, 201, 204],
    "Mars" : [255, 106, 20],
    "Jupiter" : [248, 229, 154],
    "Saturne" : [225, 213, 85],
    "Uranus" : [185, 211, 220],
    "Neptune" : [113, 178, 201],
    "Meteorite" : [142, 99, 32],
    "TraineeFeuOrange" : [254, 80, 0],
    "TraineeFeuJaune" : [255, 198, 0]
}

#Instanciation des objets du système.
Espace = circle((0, 0), 500, fill=True, rgbcolor=(29/255, 37/255, 45/255))

Soleil = Planete(pos.get('Soleil'), 10, None, color.get('Soleil'))
Mercure = Planete (pos.get('Mercure'), 3, Soleil, color.get('Mercure'))
Venus = Planete (pos.get('Venus'), 2.5, Soleil, color.get('Venus'))
Terre = Planete (pos.get('Terre'), 4, Soleil, color.get('Terre'))
Lune = Planete (pos.get('Lune'), 1, Terre, color.get('Lune'))
Mars = Planete (pos.get('Mars'), 3, Soleil, color.get('Mars'))
Jupiter = Planete (pos.get('Jupiter'), 6, Soleil, color.get('Jupiter'))
Saturne = Planete (pos.get('Saturne'), 6, Soleil, color.get('Saturne'))
Uranus = Planete (pos.get('Uranus'), 4, Soleil, color.get('Uranus'))
Neptune = Planete (pos.get('Neptune'), 4, Soleil, color.get('Neptune'))

Meteorite = Planete (pos.get('Meteorite'),6.5, Soleil, color.get('Meteorite'))
TraineeFeuOrange = Planete (pos.get('TraineeFeuOrange'),5, Soleil, color.get('TraineeFeuOrange'))
TraineeFeuJaune = Planete (pos.get('TraineeFeuJaune'),4, Soleil, color.get('TraineeFeuJaune'))

#fragments est un tableau destiné à contenir d'éventuels fragments de planète.
fragments = []

#############
#@parameters:
#    fragments - contenant d'éventuels fragments de planètes.
#@return:
#    Une concaténation d'objets de type circle destinés à être animés.
#@brief:
#    On applique les transformations adéquates à chaque objets et on concatène les résultats graphiques.
#############
def anim(fragments):
    # On applique une translation à la météorite et sa trainée de feu.
    Meteorite.translate(5)
    TraineeFeuOrange.translate(5)
    TraineeFeuJaune.translate(5)

    # La lune déplacé à sa distance relative à l'origine du repère puis on lui applique une rotation d'1 radian.
    Lune.translate_to_origin()
    Lune.rotate(1)

    # On déplace toutes les planète à leur distance relative à l'origine du repère.
    Mercure.translate_to_origin()
    Venus.translate_to_origin()
    Terre.translate_to_origin()
    Mars.translate_to_origin()
    Jupiter.translate_to_origin()
    Saturne.translate_to_origin()
    Uranus.translate_to_origin()
    Neptune.translate_to_origin()

    # S'il y a des fragments, on les déplace à leur distance relative à l'origine du repère.
    if(len(fragments)):
        for frag in fragments:
            frag.translate_to_origin()

    # On applique une rotation spécifique à chacune des planètes.
    Mercure.rotate(0.40)
    Venus.rotate(0.35)
    Terre.rotate(0.5)
    Mars.rotate(0.65)
    Jupiter.rotate(0.50)
    Saturne.rotate(0.40)
    Uranus.rotate(0.30)
    Neptune.rotate(0.20)

    # S'il y a des fragments on leur applique une rotation de 0.1 radian.
    if(len(fragments)):
        for frag in fragments:
            frag.rotate(0.10)

    # Le soleil est déplacé d'1 unité.
    Soleil.translate(1)

    # Les planètes sont déplacées vers leur objet centre de rotation (le Soleil).
    Mercure.translate_to_center()
    Venus.translate_to_center()
    Terre.translate_to_center()
    Mars.translate_to_center()
    Jupiter.translate_to_center()
    Saturne.translate_to_center()
    Uranus.translate_to_center()
    Neptune.translate_to_center()

    # S'il existe des fragments, on les déplace vers leur objet centre de rotation (ils sont dans le système donc on les fait tourner autour du Soleil).
    if(len(fragments)):
        for frag in fragments:
            frag.translate_to_center()

    # La lune est déplacée vers son objet centre de rotation.
    Lune.translate_to_center()

    # On fait la somme des représentations graphiques des planètes avec leur nouvelles positions dans la variable animation.
    animation = Espace + Terre.draw() + Soleil.draw() + Lune.draw() + Mercure.draw() + Venus.draw() + Mars.draw() + Jupiter.draw() + Saturne.draw() + Neptune.draw()
    # S'il n'y a PAS de fragments on ajoute Uranus , la météorite et sa trainée à l'animation ( Oui ces deux objets vont se rencontrer :) ).
    if (len(fragments) == 0):
        animation = animation + Uranus.draw() + TraineeFeuJaune.draw() + TraineeFeuOrange.draw()+ Meteorite.draw()
    # Si la météorite rentre en contact avec Uranus, on explose Uranus et on ajoute les fragments crées au tableau de fragments.
    if (Meteorite.collidesWith(Uranus)):
        for frag in Uranus.explode():
            fragments.append(frag)
    # S'il y a des fragments on leur applique une translation propre à chacun en plus de la rotation appliquée plus haut.
    if (len(fragments)):
        fragments[0].translate(0, 0.5)
        fragments[1].translate(0.75, 0.75)
        fragments[2].translate(0.5, 0)
        fragments[3].translate(0.75, -0.75)
        fragments[4].translate(0, -0.5)
        fragments[5].translate(-0.75, -0.75)
        fragments[6].translate(-0.5, 0)
        fragments[7].translate(-0.75, 0.75)
        # On ajoute la représentation graphique des fragments à la somme des objets à animer.
        for frag in fragments:
            animation = animation + frag.draw()
    # On renvoie la variable animation pour pouvoir animer le résultat.
    return animation

# On anime le résultat de la fonction anim(fragments) pour 15 images dans un repère sans axes, cadré entre -120 et 120 sur chacun des axes.
anim = animate([plot(anim(fragments)) for k in srange(0, 15)], axes = False, xmin = -120, xmax = 120, ymin = -120, ymax = 120)
anim.show(delay=14, iterations=3000)