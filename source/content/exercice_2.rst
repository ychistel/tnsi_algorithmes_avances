Exercices
==========

.. exercice::

    Le site WikiSource_ est une bibliothèque en ligne qui propose des ouvrages libre de droit, tombé dans l'espace public. 

    #.  Télécharger au format ``plain text`` et en intégralité, le roman "Vingt mille lieues sous les mers" de Jules Verne.
    #.  Créer un fichier python ``recherche_texte.py`` contenant les lignes suivantes:

        .. code:: Python

            roman = # fichier du roman téléchargé
            fichier = open(roman,'r',encoding="utf-8")
            texte = fichier.read()
            fichier.close

    #.  Vérifier que la variable ``texte`` n'est pas vide.
    #.  Rechercher, avec la méthode ``find``, la présence de la chaine de caractères ``Mobile dans l’élément mobile !``. Afficher sur une centaine de caratères un extrait du texte contenant ce motif.
    #.  Le capitaine Nemo est un personnage célèbre des romans de Jules Verne. Est-il présent dans cet ouvrage ?

.. exercice::

    La méthode ``find`` peut prendre 2 arguments lors d'un appel. Le premier est le ``motif`` recherché dans le texte et le second argument est l'indice où commence la recherche dans le texte.

    On rappelle que la méthode ``find``:

    -   renvoie l'indice du premier caractère du motif dans le texte s'il est présent.
    -   renvoie ``-1`` si le motif n'est pas présent dans le texte.

    Écrire un fonction ``nombre_occurence(texte,motif)`` qui prend en paramètre un texte et un motif et renvoie le nombre d'occurences du motif dans le texte. 

    .. note::

        Reprendre la lecture du cours avant de poursuivre.

.. exercice::

    On propose d'écrire en Python la recherche naïve d'un motif dans un texte. On utilisera 2 fonctions pour le réaliser:

    #.  La fonction ``correspondance(texte,motif,i)`` prend en paramètre un texte, un motif et un nombre entier ``i`` désignant l'indice de la position du motif dans le texte. 

        La fontion renvoie un booléen qui vaut ``True`` si on a une correspondance entre le motif et le texte dans la fenêtre de recherche et ``False`` dans le cas contraire.

    #.  La fonction ``recherche(texte,motif)`` parcourt la chaine ``texte`` en vérifiant s'il y a une correspondance avec ``motif``.

        -   S'il y a une correspondance, elle renvoie l'indice où se trouve le motif dans la chaine texte.
        -   Dans le cas contraire, elle décale la fenêtre de recherche et cherche une nouvelle correspondance. Si la chaine ``texte`` est entièrement parcourue sans avoir de        correspondance, la fonction renvoie ``-1``.

    #.  Vérifier votre recherche avec le texte ``hippoppotame`` et les motifs ``pop``, ``pot`` et ``top``.
    #.  Reprendre l'exercice 1 et faire les recherches textuelles réalisées avec la méthode ``find``.

.. exercice::

    #.  On recherche le motif ``aab`` dans le texte ``aaaa``. Combien de comparaisons de caractères sont nécessaires pour vérifier la présence du motif dans le texte ?
    #.  Même question avec le motif ``aab`` dans le texte ``aaaaaaa``.
    #.  Généraliser les observations précédentes avec un motif de longueur ``p`` et un texte de longueur ``n``.
    #.  En déduire la complexité de l'algorithme naïf de recherche textuelle.

    .. note::

        Reprendre la lecture du cours avant de poursuivre.

.. exercice::

    #.  Donner les différentes étapes de la recherche par l'algorithme de Boyer-Moore-Horspool dans les cas suivants:

        a.  le texte est ``programme`` et le motif est ``ram``.
        b.  le texte est ``informatique`` et le motif est ``mat``.
        c.  le texte est ``numerique`` et le motif est ``ric``.

    #.  Le dernier cas de la question précédente provoque une erreur. Quelle condition faut-il vérifier pour l'éviter ?

.. exercice::

    Dans l'algorithme BMH, lorsqu'un caractère ``c`` du texte ne correspond pas avec le caractère du motif, on vérifie si ce caractère ``c`` est présent dans le motif. 

    Pour effectuer cette vérification, on construit un dictionnaire dont les clés sont les caractères du motif et les valeurs les indices de position du caractère le plus à droite dans le motif.

    #.  Quel est le dictionnaire associé au motif ``abbac`` ?
    #.  Écrire une fonction qui renvoie ce dictionnaire en prenant en paramètre un motif.

.. exercice::

    On propose d'écrire en Python l'algorithme de Boyer et Moore pour vérifier la présence d'un motif dans un texte. Selon les correspondances entre les caractères du motif et ceux du texte, on effectue différents décalages du motif. 

    #.  Écrire la fonction ``decalage`` qui prend en paramètres :

        -   ``texte`` qui contient la chaine de caractères dans laquelle on recherche un motif;
        -   ``motif`` qui contient la chaine de caractères contenant le motif à chercher;
        -   ``dico`` qui contient le dictionnaire associé au motif dont les valeurs sont les indices de position des caractères du motif les plus à droite;
        -   ``i`` un nombre entier qui aligne le caractère d'indice ``i`` avec le premier caractère du moitf.

        La fonction parcourt le motif, caractère par caractère, et vérifie la correspondance avec le texte aligné. Elle renvoie le décalage du motif. S'il y a correspondance, la fonction renvoie ``0``.

        .. warning::

            La recherche avec l'algorithme de Boyer et Moore commence avec le dernier caractère du motif.

    #.  Écrire la fonction ``bmh`` qui prend en paramètres ``texte`` et ``motif`` qui sont deux chaines de caractères et qui renvoie l'indice de position du motif présent dans le texte. S'il n'y a pas de carrespondance, la fonction renvoie -1.

    #.  Effectuer la recherche du motif ``Mobile dans l'élément mobile`` dans le texte du roman de Jules Vernes ``Vingt mille lieues sous les mers``. Ajouter un compteur pour comparer l'efficacité de l'algorithme avec l'algorithme de recherche naïve.

.. _WikiSource: https://fr.wikisource.org/
