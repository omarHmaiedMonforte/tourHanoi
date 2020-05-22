#coding : utf-8

################################ Code #################################
def initialisation(n):
    """Initialisation du plateau de jeu avec le nombre de disque"""
    for i in range(n,0,-1):
        Source.append(i)
    return Source

def nb_disk(Plateau, pos):
    """Retourne le nombre de tour présent sur le plateau"""
    return len(Plateau[pos])

def disk_sup(Plateau, pos):
    """Retourne l'identifiant du disque supérieur de la tour demandée"""
    taille=nb_disk(Plateau, pos) #on récupère le nombre de disques de la tour recherché, grâce a la fonction nb_disk
    if taille>0:
        last=Plateau[pos][taille-1] 
        return last #on retourne la valeur du dernier disque de la tour cherché
    else:
        return -1 #On retourne -1 si la tour est vide

def pos_disk(Plateau, numdisk):
    """Retourne le  numéro de la tour en fonction du disque recherché"""
    for tour in range(3):
        if numdisk in (Plateau[tour]):
            return tour

def check_moov(Plateau, start, final):
    """Vérifie si le déplacement du disque choisi est possible"""
    if (disk_sup(Plateau,start)<disk_sup(Plateau,final)) or (disk_sup(Plateau,final)==-1): # on vérifie la condition si le disque supérieur de la tour d'arrivé est plus grand que celui de la tour de départ
        return True                                                                        # ou si la tour d'arrivée est vide pour que le déplacement s'effectue quand même
    else:                                                                                  # on retourne un booléen
        return False

def check_startmoov(Plateau, start):
    """Vérifie si le disque sélectionner en premier peut-être déplacé ou non"""
    if start==0:
        if(check_moov(Plateau, start, 1) or (check_moov(Plateau, start,2))==True): # vérifie si au moins 1 des disques des 2 autres tours sont supérieur à celui selectionner
            return True

    elif start==1:
        if (check_moov(Plateau, start, 0) or (check_moov(Plateau, start,2))==True): # vérifie si au moins 1 des disques des 2 autres tours sont supérieur à celui selectionner
            return True

    elif start==2:
        if (check_moov(Plateau, start, 0) or (check_moov(Plateau, start,1))==True): # vérifie si au moins 1 des disques des 2 autres tours sont supérieur à celui selectionner
            return True
    else:
        return False

def check_win(Plateau, n):
    """Vérifie si la partie est gagné"""
    if len(Source)==0 and len(Auxiliaire)==0:                           # On commence par vérifié si il n'y as plus de disque dans les deux premières tours
        if disk_sup(Plateau,2)==1 and Destination[0]==len(Destination): # Puis on vérifie si le disque supérieur est bien le plus petit et le disque inférieur est bien le plus grand
            return True                                                 # Il n'y as pas besoin de vérifier l'ordre puisque celui-ci est vérifié à chaque déplacement

def lirecoords(plateau):
    """Fonction permettant de demander et vérifier les tours selectionner pour le déplacement d'un disque"""
    tourdep=-2 #on initialise des
    tourarr=-2 #valeur inexécutable

    while not (0<=tourdep<=2 and nb_disk(plateau,tourdep)>0 and check_startmoov(plateau,tourdep)==True): #boucle while qui vérifie si la tour entrer possible
        tourdep=int(numinput("Tour", "Entrer la tour de départ", default=None, minval=1, maxval=3)-1) #Affiche la fênetre auxiliaire pour entrer le numéro de la tour sans passer par l'interpréteur python
        if not 0<=tourdep<=2:                              # on vérifie si la tour existe
            print("Erreur la tour renseigné n'existe pas !") # on print l'erreur qui va avec
        elif nb_disk(plateau, tourdep)==0:                                  #on vérifie si la tour n'est pas vide
            print("Erreur la tour numéro ",tourdep," renseigné est vide !") # on print l'erreur qui va avec
        elif not check_startmoov(plateau, tourdep):                                                              # on vérifie si l'on peut déplacer le disque
            print("Vous ne pouvez pas déplacé le disque supérieur de la tour",tourdep," sur les autres tours !") # on print l'erreur qui va avec

    while not (0<=tourarr<=2 and check_moov(plateau,tourdep,tourarr)):
        tourarr=int(numinput("Tour", "Entrer la tour d'arrivée", default=None, minval=1, maxval=3)-1) #Affiche la fênetre auxiliaire pour entrer le numéro de la tour sans passer par l'interpréteur python
        def tourselec(tour):
            tourarr=tour
        if not 0<=tourarr<=2:                                # on vérifie si la tour existe
            print("Erreur la tour renseigné n'existe pas !") # on print l'erreur qui va avec
        if tourdep==tourarr:                                                      # on vérifie si ce n'est pas la même tour saisie que celle d'avant
            print("Vous ne pouvez pas déplacé le même disque sur la même tour !") # on print l'erreur qui va avec
        elif check_moov(plateau, tourdep, tourarr)==False:                                                    # on vérifie si l'on peut bien déplacer le disque entre ces deux tours
            print("Le disque supérieur de la tour",tourarr,"est plus petit que celui voulans être déplacé !") # on print l'erreur qui va avec
    return tourdep,tourarr # on retourne les valeurs des tours de départ et d'arrivée pour le déplacement

def GameLoop(x,y):
    global n, Plateau, nbcoups, AncienneSelec, Menu, limitecoups, initGame, tempsDebut, partie, alreadyPlay
    Coords = CoordsClick(x,y)
    if Menu:  #si l'on est dans le menu
        if Coords==1: #incrémentation de 1 du nombre de disque total
            if not n==15: #on évite d'aller au-dessus de 15 pour ne pas que le plateau sorte de l'écran
                n+=1 #on incrémente de 1 le nombre total de disque s
                nDisk(n) #on affiche le nouveau nombre total de disque
            return n
        if Coords==-1: #incrémentation de -1 du nombre de disque total
            if not n==2: #on évite de descendre en dessous de 2 disque
                n-=1 #on désincrement de 1 le nombre total de disques
                nDisk(n) #on affiche le nouveau nombre total de disque
            return n
        if Coords==-5:
            clear()
            color((0,0,0))
            dept=tableau()
            print(dept)
            up()
            goto(0,0)
            seth(270)
            for i in dept:
                write(i, move=False, align="center", font=("Arial", 20, "bold"))
                forward(50)
    elif not Menu: #si l'on n'est pas dans le menu
        if initGame: #execution que si l'on vient de sortir du menu
            global partieCopy
            initGame=False #on désactive l'initialisation de la partie
            clear()
            limitecoups = (2**n)*n #on définit la limite de coup en fonction du nombre de disque
            initialisation(n)
            partieCopy[0] = Plateau #initialisation du coup 0 = position de départ des disques
            partie = deepcopy(partieCopy)
            disk_color(n) #création de la liste de dégradé des disque
            draw_set(n) #on dessine le plateau
            titre(n) #on affiche les différents textes
            draw_config(Plateau, n) #on dessine les disque sur le plateau
            tempsDebut = time() #on récupère l'horaire de départ de la partie
            return partie

        if Coords==-1: #annulation des coups
            if not len(partie)==1:
                tourstart=partie[nbcoups-1]
                tourend=partie[nbcoups]

                #tour de départ du précédent coup
                if len(tourend[0])<len(tourstart[0]):
                    backdep=0
                elif len(tourend[1])<len(tourstart[1]):
                    backdep=1
                elif len(tourend[2])<len(tourstart[2]):
                    backdep=2

                #tour de fin du précédent coup
                if len(tourend[0])>len(tourstart[0]):
                    backend=0
                elif len(tourend[1])>len(tourstart[1]):
                    backend=1
                elif len(tourend[2])>len(tourstart[2]):
                    backend=2
                
                nd=Plateau[backend][-1]
                eff_disk(nd, Plateau, n) #on l'efface de son plateau d'origine
                Plateau[backend].pop(-1) #on enlève le disque déplacé de la liste d'origine
                Plateau[backdep].append(nd) #on insère le disque dans la liste de sa destination
                color((0,0,0),(degrade[nd-1])) #fonction permmentant de récupérer la couleur du disque
                draw_disk(nd, Plateau, n) #on dessine le disque sur sa tour d'arrivée
                nbcoups-=1 #on increment le nombre de coups joué de 1
                PrintCoup(nbcoups) #on affiche le nouveau nombre de coup
                
                del partie[nbcoups+1]

        elif 0<=Coords<=2: #déplacement des disques
            if len(SelectTour)==0:
                if check_startmoov(Plateau, Coords): #Double if permettant de verifier si la on peut séléctionner ce disque
                    SelectTour.append(Coords)
            if len(SelectTour)==1:
                if check_moov(Plateau, SelectTour[0], Coords): #Double if permettant de verifier si le  déplacement du disque entre les deux tour est faisable
                    SelectTour.append(Coords)
            
            if len(SelectTour)==2: #Si l'on a deux tours selectionner dans la liste alors on effectue le déplacement du disque
                alreadyPlay=True #La partie à déjà était commencé par le joueur
                tourdep=SelectTour[0] #première tour selectionner au click
                touarr=SelectTour[1] #deuxième tour selectionner au click
                SelectTour.clear() #on vide la liste de selection des tours pour pouvoir refaire une nouvelle selection de tour
                nd=Plateau[tourdep][-1] #on récupère le numéro du disque qui va t'être déplacé
                eff_disk(nd, Plateau, n) #on l'efface de son plateau d'origine
                Plateau[tourdep].pop(-1) #on enlève le disque déplacé de la liste d'origine
                Plateau[touarr].append(nd) #on insère le disque dans la liste de sa destination
                color((0,0,0),(degrade[nd-1])) #fonction permmentant de récupérer la couleur du disque
                draw_disk(nd, Plateau, n) #on dessine le disque sur sa tour d'arrivée
                nbcoups+=1 #on increment le nombre de coups joué de 1
                PrintCoup(nbcoups) #on affiche le nouveau nombre de coup
                
                partieCopy = deepcopy(partie)
                partieCopy[nbcoups]= Plateau
                partie = deepcopy(partieCopy)

                if check_win(Plateau,n): #on vérifie sir la partie est gagné
                    tempsFin=time() #on récupère dans une variable le temps de fin
                    timer=tempsFin-tempsDebut #temps passé en game
                    mtime=temps_moyen(timer, nbcoups)
                    mtime=round(mtime,2)
                    clear() #on efface la fenêtre pour afficher la fênetre de fin
                    convertisseur(timer) #on récupère le temps avec les heures, mniutes, secondes
                    up()
                    goto(0,0)
                    color((255,0,0))
                    write("          Bravo\nVous avez gagné", move=False, align="center", font=("Arial", 50, "bold"))
                    goto(-window_width()/10,-window_height()/6)
                    color((0,0,0))
                    seth(0)
                    write("En ", move=False, align="center", font=("Arial", 25, "bold"))
                    forward(50)
                    write(nbcoups, move=False, align="center", font=("Arial", 25, "bold"))
                    forward(120)
                    write(" coups et en ", move=False, align="center", font=("Arial", 25, "bold"))
                    forward(100)
                    for i in range(len(temps)):
                        write(":", move=False, align="center", font=("Arial", 25, "bold"))
                        forward(25)
                        write(temps[i], move=False, align="center", font=("Arial", 25, "bold"))
                    forward(120)
                    write("secondes", move=False, align="center", font=("Arial", 25, "bold"))
                    goto(-window_width()/10,-2*window_height()/6)
                    write("Le temps moyens par coups est de :", move=False, align="center", font=("Arial", 25, "bold"))
                    seth(0)
                    forward(320)
                    write(mtime, move=False, align="center", font=("Arial", 25, "bold"))
                    cpt=nbcoups
                    nom=str(textinput("joueur", "votre nom svp:"))
                    fichier=open('score.txt','rb')
                    score(fichier,nom,n,cpt,timer,mtime)
                    dept=pickle.load(fichier)
                    fichier.close()
                    exitonclick() #nous fait sortir de la fenêtre graphique lorsque la boucle de jeu est fini et que l'on clique sur la fenêtre
                elif nbcoups==limitecoups: #on vérifie si le nombre de coups n'est pas arrivé à la limite, si c'est le cas
                    up()
                    goto(0,-200)
                    print("Perdu, vous avez dépasser le nombre de coups maximal\nRéessayer avec moins de disques")
                    goto(0,-200)
                    write("Cliquer pour quitter", move=False, align="center", font=("Arial", 20, "bold"))
                    exitonclick() #nous fait sortir de la fenêtre graphique lorsque la boucle de jeu est fini et que l'on clique sur la fenêtre

        elif Coords==-2: #lancement de la résolution automatique
            if not alreadyPlay:
                autohanoi(Plateau, n)
                if check_win(Plateau,n): #on vérifie sir la partie est gagné
                    clear() #on efface la fenêtre pour afficher la fênetre de fin
                    up()
                    goto(0,0)
                    color((255,0,0))
                    write("Maintenant, essayez-vous même", move=False, align="center", font=("Arial", 50, "bold"))
        
        elif Coords==-3: #abandon de la partie
            clear()
            up()
            goto(0,0)
            color((255,0,0))
            write("Vous avez abandonné votre partie", move=False, align="center", font=("Arial", 50, "bold"))
            goto(0,-200)
            write("Cliquer pour quitter", move=False, align="center", font=("Arial", 20, "bold"))
            exitonclick() #nous fait sortir de la fenêtre graphique lorsque la boucle de jeu est fini et que l'on clique sur la fenêtre
    return n, Plateau, limitecoups, nbcoups, AncienneSelec, initGame

def CoordsClick(x,y):
    """Retourne sur quoi le click à était effectué sous forme de valeur integer"""
    global SelectTour, n, Menu
    if not Menu:
        if Tour123(n,1)-((0.5*(40+30*(n-1)))/2)<=x<=Tour123(n,1)+((0.5*(40+30*(n-1)))/2) and sety0(n)<=y<=sety0(n)+15*(n+1): #Calcul des coordonnées si l'on clique sur la tour de départ
            return 0
        elif Tour123(n,2)-((0.5*(40+30*(n-1)))/2)<=x<=Tour123(n,2)+((0.5*(40+30*(n-1)))/2) and sety0(n)<=y<=sety0(n)+15*(n+1): #Calcul des coordonnées si l'on clique sur la tour de auxiliaire
            return 1
        elif Tour123(n,3)-((0.5*(40+30*(n-1)))/2)<=x<=Tour123(n,3)+((0.5*(40+30*(n-1)))/2) and sety0(n)<=y<=sety0(n)+15*(n+1): #Calcul des coordonnées si l'on clique sur la tour de arrivée
            return 2
        elif (window_width()/2-10>=x>=window_width()/2-210) and (sety0(n)<=y<=sety0(n)+50):
            return -1
        elif -window_width()/2+10<=x<=-window_width()/2+185 and sety0(n)<=y<=sety0(n)+50:
            return -2
        elif -100<=x<=100 and -window_height()/2+10<=y<=-window_height()/2+60:
            return -3
    elif Menu:
        if 4*window_width()/48+5<=x<=4*window_width()/48+75 and -window_height()/7-80<=y<=-window_height()/7-10:
            return -1
        elif 4*window_width()/48+5<=x<=4*window_width()/48+75 and -window_height()/7+90<=y<=-window_height()/7+160:
            return 1
        elif window_width()/2-220<=x<=window_width()/2-20 and -window_height()/2+10<=y<=-window_height()/2+50:
            return -5
        elif -100<=x<=100 and -window_height()/2+15<=y<=-window_height()/2+77:
            Menu=False
            return Menu

def convertisseur(tempsbrut):
    global temps
    while tempsbrut>=60:
        tempsbrut = tempsbrut/60
        temps.append(round(tempsbrut))
    if len(temps)==0:
        temps.append(round(tempsbrut))
    return temps

def score(file,name,n,cpt,timer,mtime):
    file=open('score.txt','wb')
    dic={'nom':name,'nombre de disque':n,'nombre de coup':cpt,'temps':timer,'temps moyen':mtime}
    pickle.dump(dic,file)
    file.close()

def temps_moyen(timer,nbcoups):
    """Renvoie le temps moyens entre chaque coups"""
    mtime=timer/nbcoups
    return mtime

def tableau():
    fichier=open('score','rb')
    dept=pickle.load(fichier)
    for i in dept:
        print(i)


    fichier.close()

################################ Turtle ###############################

def TurtleWindow():
    """initialisation de la fenêtre graphique"""
    colormode(255)              # Mode de couleur de la tortue en RGB(Rouge, Vert, Bleu)
    title("Tour d'Hanoï")       # Changement du Titre de la fenêtre graphique
    setup(0.993, 0.925, 0, 0)   # Changement de la taille de la fenêtre graphique

def initTurtle():
    """Initialisation des paramètres de la tortue"""
    ht() #On rends la tortue invisible
    speed(0) #Changement de la vitesse de la tortue, ici 0 est égale à la vitesse maximmal de celle-ci
    up() #arrête de dessiner
    goto(setx0(n),sety0(n)) # déplacement de la tortue au point de départ du plateau
    down() #Se remet a dessiner
    
def plat(n):
    """Dessine la base du plateau de jeu"""
    seth(0)
    forward(200+90*(n-1))
    seth(270)
    forward(20)
    seth(180)
    forward(200+90*(n-1))
    seth(90)
    forward(20)

def tour(n):
    """Dessine une tour"""
    seth(90)
    forward(15*(n+1))
    seth(0)
    forward(6)
    seth(270)
    forward(15*(n+1))
    seth(0)

def draw_set(n):
    """Utilise les fonctions qui trace la base du plateau et les tours"""
    color((178, 81, 33),(178, 81, 33)) #setup de la couleur (de contour et remplissage) de la tortue
    up()
    goto(setx0(n), sety0(n))
    down()
    begin_fill() #lancement du fill
    plat(n)
    seth(0)
    goto(Tour123(n,1), sety0(n)) #déplacement au point de la premeière tour
    tour(n)
    for i in range(2,4): #boucle pour dessiner les 2 tours restante
        seth(0)
        goto(x=Tour123(n,i), y=sety0(n))
        tour( n)
    end_fill() #Remplissage de la forme qui vbient d'être dessiner

def draw_disk(nd, Plateau, n):
    """Tracer du disque choisit"""
    seth(180)
    begin_fill()
    coord_disk(nd, Plateau,n)
    forward(-3+0.5*(40+30*(nd-1)))
    seth(90)
    forward(14)
    seth(0)
    forward(40+30*(nd-1))
    seth(270)
    forward(14)
    seth(180)
    forward(0.5*(40+30*(nd-1))+3)
    end_fill()

def eff_disk(nd, Plateau, n):
        """Efface le disque choisit"""
        color((255,255,255),(255,255,255)) #couleur du tracé et de remplissage de la tortue en blanc
        draw_disk( nd,Plateau,n) #dessine le disque à effacé en blanc
        color((178, 81, 33),(178, 81, 33)) #couleur du tracé et de remplissage de la tortue en marron (couleur du plateau)
        begin_fill()
        coord_disk(nd,Plateau,n)
        seth(180)
        for i in range(2): #boucle for pour redessiner la partie de la tour qui a était effacé
            right(90)
            forward(15)
            right(90)
            forward(6)
        end_fill() #remplissage de la figure qui vient d'être dessiner

def titre(n):
    """affichage textuel dans la fenêtre graphique"""
    #Affichage du Titre (Tour d'Hanoi)
    color((255,0,0))
    y=window_height()/2-70
    up()
    goto(0,y)
    down()
    write("Tour d'Hanoi", move=False, align="center", font=("Arial", 50, "bold"))

    #Affichage des noms des tours (Départ, Auxiliaire, Arrivée)
    color(0,0,0)
    x=Tour123(n,1)
    y=sety0(n)-50
    up()
    goto(x,y)
    down()
    write("Départ", move=False, align="center", font=("Arial", 15, "bold"))
    x=Tour123(n,2)
    up()
    goto(x,y)
    down()
    write("Auxiliaire", move=False, align="center", font=("Arial", 15, "bold"))
    x=Tour123(n,3)
    up()
    goto(x,y)
    down()
    write("Arrivée", move=False, align="center", font=("Arial", 15, "bold"))

    #Affichage du nombre de coups maximal
    global limitecoups
    y=-window_height()/2+10
    x=-window_width()/2+10
    up()
    goto(x,y)
    down()
    write("Vous avez joué \ncoups sur ", move=False, align="left", font=("Arial", 20, "bold"))
    x=-window_width()/2+150
    up()
    goto(x,y)
    down()
    write(limitecoups, move=False, align="left", font=("Arial", 20, "bold"))
    PrintCoup(0)

    #affichage de la numérotation des tours
    y=-window_height()/2+10
    x=window_width()/2-10
    up()
    goto(x,y)
    down()
    write("                By :\nOmar Hmaied Monforte \n                and\n      Benjamin Bellier", move=False, align="right", font=("Arial", 20, "bold"))

    #affichage du bouton pour annuler le coup
    y=sety0(n)+50
    x=window_width()/2-10
    up()
    goto(x,y)
    down()
    color((220,220,220),(100,100,100))
    pensize(5)
    seth(0)
    begin_fill()
    for i in range(2):
        right(90)
        forward(50)
        right(90)
        forward(200)
    end_fill
    y=sety0(n)
    x=window_width()/2-105
    up()
    goto(x,y)
    down()
    color((0,0,0))
    pensize(1)
    write("Annulation du\n dernier coup", move=False, align="center", font=("Arial", 15, "bold"))

    #affichage du bouton pour abandonner la partie
    y=-(window_height()/2)+10
    x=-100
    up()
    goto(x,y)
    down()
    pensize(5)
    color((225,0,0),(255,0,0))
    begin_fill()
    seth(0)
    for i in range(2):
        forward(200)
        left(90)
        forward(50)
        left(90)
    end_fill()
    pensize(1)
    setx(0)
    color((255,255,255),(255,255,255))
    write("Abandon", move=False, align="center", font=("Arial", 32, "bold"))

    #affichage du bouton pour annuler le coup
    y=sety0(n)+50
    x=-window_width()/2+10
    up()
    goto(x,y)
    down()
    color((220,220,220),(100,100,100))
    pensize(5)
    seth(0)
    begin_fill()
    for i in range(2):
        forward(175)
        right(90)
        forward(50)
        right(90)
    end_fill
    y=sety0(n)
    x=-window_width()/2+100
    up()
    goto(x,y)
    down()
    color((0,0,0))
    pensize(1)
    write(" Résolution\nautomatique", move=False, align="center", font=("Arial", 15, "bold"))

def PrintCoup(nbcoups):
    """Affiche le nombre de coups joué en bas à gauche de la fenêtre graphique"""
    global n #on récupère la variable n global qui est dans le main du programme
    x=-window_width()/2+205 #calcul de la coordonnées "x"  du nombre de coups
    y=-window_height()/2+42 #calcul de la coordonnées "y"  du nombre de coups
    up()
    goto(x,y) #déplacement de la tortue
    down()
    seth(0) #met le regard de la tortue vers la droite
    color((255,255,255),(255,255,255)) #couleur du tracé et du remplissage de la tortue en blanc
    begin_fill()
    for i in range(2): #boucle qui permet d'efffacer l'ancien nombre de coup 
        if nbcoups<10:
            forward(50)
        elif nbcoups>=10:
            forward(100)
        elif nbcoups>=100:
            forward(150)
        elif nbcoups>=1000:
            forward(200)
        left(90)
        forward(40)
    end_fill()
    color((0,0,0)) #couleur du tracé de la tortue en noir
    x=-window_width()/2+215
    up()
    goto(x,y) #déplacment de la tortue
    down()
    write(nbcoups, move=False, align="left", font=("Arial", 20, "bold"))

def sety0(n):
    """Retourne la position du coin supérieur gauche du plateau (coordonnées y=0 de la figure, non de la fenêtre)"""
    return int(-(15*(n+1))/2)

def setx0(n):
    """Retourne la position du coté gauche du plateau (coordonnées x=0 de la figure, non de la fenêtre)"""
    return -(90*(n-1))/2-100

def Tour123(n,t):
    """Retourne la position x de la tour cherché"""
    if t==1:
        return setx0(n) + ((1/2)*(30*(n-1))+37)
    if t==2:
        return Tour123(n,1)+60+30*(n-1)-6
    if t==3:
        return Tour123(n,2)+60+30*(n-1)-6

def coord_disk(nd, Plateau, n):
    """Déplace la tortue au milieu inférieur du disque recherché"""
    if pos_disk(Plateau, nd)==0:                            #recherche la position du disque sur le plateau
        x=Tour123(n,1)                                      #calcul de x
        y=15*Plateau[0].index(nd) - int((20+15*(n+1))/2)+11 #calcul de y

    elif pos_disk(Plateau, nd)==1:                          #recherche la position du disque sur le plateau
        x=Tour123(n,2)                                      #calcul de x
        y=15*Plateau[1].index(nd) - int((20+15*(n+1))/2)+11 #calcul de y

    elif pos_disk(Plateau, nd)==2:                          #recherche la position du disque sur le plateau
        x=Tour123(n,3)                                      #calcul de x
        y=15*Plateau[2].index(nd) - int((20+15*(n+1))/2)+11 #calcul de y

    up()
    goto(x, y) #déplacment de la tortue
    down()

def disk_color(n_vals):
    """créer la liste des différentes couleur pour le dégradé des disques"""
    r1, g1, b1 = 255,0,0 #couleur du disque le plus petit
    r2, g2, b2 = 0,0,255 #couleur du disque le plus grand
    etendue = n_vals - 1 #calcul de l'étendu 
    for i in range(n_vals): #boucle ajoutant les valeur rgb du degradé dans la liste degrade
        alpha = 1 - i / etendue         #calcul du multiplicateur descendant en fonction du numéro du disque
        beta = i / etendue              #calcul du multiplicateur ascendant en fonction du numéro du disque
        r = int(r1 * alpha + r2 * beta) #calcul de la valeur du rouge entre 255->0
        g = int(g1 * alpha + g2 * beta) #calcul de la valeur du vert qui reste toujours à 0
        b = int(b1 * alpha + b2 * beta) #calcul de la valeur du bleu entre 0->255
        degrade.append((r, g, b))       #ajout des 3 valeurs dans la liste
    return degrade

def draw_config(plateau, n):
    """affichage des disques sur le plateau"""
    for i in range(n,0,-1): #boucle for inversé pour dessiner les disques du bas en haut
        color((0,0,0),degrade[i-1]) #couleur de tracé de la tortue en noir et du remplissage avec la liste de dégradé
        draw_disk( i, Plateau, n) #appel la fonction pour dessiner le disque choisit

def erase_all(plateau, n):
    """efface tout les disque présent sur le plateau"""
    for i in range(1, n+1): #boucle qui appel la fonction qui efface le disque choisit
        eff_disk( i, Plateau, n)

def Home():
    """Affichage du MENU graphique"""
    #affichage de MENU
    up()
    goto(0,window_height()/6)
    down()
    color((255,0,0))
    write("MENU", move=False, align="center", font=("Arial", 75, "bold"))

    nDisk(2)

    #Affichage du texte a coté de la selection
    up()
    goto(-2*window_width()/24,-window_height()/7)
    down()
    color((0,0,0))
    write(" Sélectionner votre\nnombre de disques", move=False, align="center", font=("Arial", 20, "bold"))
    
    #Affichage de la flèche inférieur
    up()
    goto(4*window_width()/48+5,-window_height()/7-10)
    down()
    pensize(4)
    color((50,50,50),(100,100,100))
    begin_fill()
    for i in range(3):
        forward(70)
        right(120)
    end_fill()

    #affichage de la flèche superieur
    up()
    goto(4*window_width()/48+5,-window_height()/7+90)
    down()
    pensize(4)
    color((50,50,50),(100,100,100))
    begin_fill()
    for i in range(3):
        forward(70)
        left(120)
    end_fill()

    #dessin du bouton PLAY
    up()
    goto(-100,-window_height()/2+15)
    down()
    color((220,0,0))
    pensize(5)
    seth(0)
    for i in range(2):
        forward(200)
        left(90)
        forward(62)
        left(90)
        
    up()
    goto(0,-window_height()/2+5)
    write("PLAY", move=False, align="center", font=("Arial", 50, "bold"))
    pensize(1)

    #bouton tableau
    color((0,0,255)) #couleur texte bleu (RGB)
    up()
    goto(window_width()/2-20, -window_height()/2+20)
    down()
    pensize(5)
    seth(0)
    left(90)
    for i in range(2):
        forward(40)
        left(90)
        forward(200)
        left(90)
    up()
    goto(window_width()/2-120, -window_height()/2+20)
    write("TABLEAU", move=False, align="center", font=("Arial", 25, "bold"))
    pensize(1)

def nDisk(n):
    up()
    goto(4*window_width()/48,-window_height()/7)
    down()
    seth(0)
    pensize(5)
    color((50,50,50),(200,200,200))
    begin_fill()
    for i in range(4):
        forward(80)
        left(90)
    end_fill()
    seth(0)
    up()
    goto(4*window_width()/48+40,-window_height()/7-5)
    color((255,255,255),(255,255,255))
    write(n, move=False, align="center", font=("Arial", 55, "bold"))
    pensize(1)

def play_autoHanoi(tourdep, tourarr, Plateau):
    global nbcoups
    nd=Plateau[tourdep][-1] #on récupère le numéro du disque qui va t'être déplacé
    eff_disk(nd, Plateau, n) #on l'efface de son plateau d'origine
    Plateau[tourdep].pop(-1) #on enlève le disque déplacé de la liste d'origine
    Plateau[tourarr].append(nd) #on insère le disque dans la liste de sa destination
    color((0,0,0),(degrade[nd-1])) #fonction permmentant de récupérer la couleur du disque
    draw_disk(nd, Plateau, n) #on dessine le disque sur sa tour d'arrivée
    nbcoups+=1 #on increment le nombre de coups joué de 1
    PrintCoup(nbcoups) #on affiche le nouveau nombre de coup

def disque(nombre):
    n=0
    while nombre%2**n==0:
        n+=1
    return n

def autohanoi(plateau,n):
    for i in range(1,(2**n)):
        nd=disque(i)
        if n%2==0:
            if nd%2==0:
                deplacement_gauche(plateau,n,nd)
            if nd%2==1:
                deplacement_droite(plateau,n,nd)
        if n%2==1:
            if nd%2==0:
                deplacement_droite(plateau,n,nd)
            if nd%2==1:
                deplacement_gauche(plateau,n,nd)

def deplacement_gauche(plateau,n,nd):
    tour=pos_disk(plateau, nd)
    tourdep=tour
    
    if tour == 0:
        tour=2
    elif tour==2:
        tour=1
    elif tour==1:
        tour=0

    tourarr=tour
    print(tourdep,tourarr)
    play_autoHanoi(tourdep, tourarr, Plateau)

def deplacement_droite(plateau,n,nd):
    tour=pos_disk(plateau, nd)
    tourdep=tour
    
    if tour == 0:
        tour=1
    elif tour==1:
        tour=2
    elif tour==2:
        tour=0

    tourarr=tour
    print(tourdep, tourarr)
    play_autoHanoi(tourdep, tourarr, Plateau)

#######################################################################
################################ Main #################################
#######################################################################
from turtle import * #importation du module turtle
from random import * #importation du module random
from time import * #importation du module time
from copy import deepcopy #importation de la fonction deepcopy
import pickle

partie = dict() #initialisation du dictionnaire permettant de connaitre les coups effectué lors de la partie
partieCopy = dict()

Source = list() #initialisation de la liste de la tour Source
Auxiliaire = list()  #initialisation de la liste de la tour Auxiliaire
Destination = list()  #initialisation de la liste de la tour Destination
Plateau = [Source, Auxiliaire, Destination] #initialisation de la liste du plateau avec toute les tours
degrade = list() #initialisation de la liste degrade
SelectTour = list() #initialisation de la liste pour la selection des tours
AncienneSelec = list() #initialisation de la liste pour l'annulation du coup
temps = list() #initialisation de la liste qui nous retourne le temps du joueur

Menu = True #on initialise la variable booléen permettant de savoir si l'on est dans le menu ou pas
autoresolution=False #Initialisation du paramètre permettant de savoir si la partie a était faite/finie avec l'algorythme de résolution automatique
annulation=False #initialisation de la variable annulation si l'on annul un coup
initGame = True #permet de vérifier si l'on doit initialiser la partie ou pas
alreadyPlay = False #boleen si on utilise l'algorithme de recursion automatique

n = 2 #Initialisation du nombre total de disques
nbcoups = 0 #on initilaise le nombre de coup effectué
limitecoups = 0 #on initialise le nombre de coups maximal
tempsDebut = 0 #initialisation de la variable temps
################################ Code #################################
TurtleWindow()
initTurtle()
Home()

onscreenclick(GameLoop)
mainloop()