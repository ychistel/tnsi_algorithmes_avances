Algorithme de Boyer et Moore
============================

La recherche textuelle consiste à trouver la présence d'une chaine de caractères appelée **motif** dans un texte. Il existe différents algorithmes qui résolvent ce problème.

Le langage Python propose la méthode ``find`` qui s'applique sur les chaines de caractères. Si on crée une variable ``texte`` de type ``str``, on peut lui appliquer la méthode ``find`` qui prend en paramètre une chaine de caractères et qui renvoie l'indice du premier caractère dans le texte qui correspond au motif.

    >>> texte = 'La moto de Tom'
    >>> texte.find('mot')
    3

Recherche naïve
----------------

L'algorithme naïf consiste à comparer un à un, de gauche à droite, les caractères du texte avec ceux du motif. Deux cas sont à envisager:

-   Le caractère du texte et le caractère du motif correspondent, on passe au caractère suivant du motif et on le compare au caractère suivant du texte.
-   Le caractère du texte et du motif ne correspondent pas, on décale le motif d'un caractère vers la droite.

On recommence les comparaisons jusqu'à la fin du texte ou du motif tant qu'il ny a pas de correspondance. L'algorithme se termine si on trouve une correspondance ou si on arrive à la fin du texte sans correspondance.

Prenons l'exemple du texte ``hippoppotame`` et du motif ``pop`` en plaçant le motif juste en dessous du texte.

.. figure:: ../img/recherche_naive_1.png
    :align: center
    :width: 300

En appliquant l'algorithme, on obtient les différentes étapes suivantes à chaque itération.

.. figure:: ../img/recherche_naive_2.png
    :align: center
    :width: 600

