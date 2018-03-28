#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools


class Node(object):
    """
    Class de type Node pour être utiliser pour le réseau bezien
    Cette class herite du type Object. Pour donner la possibiliter de lui rajouter dynamiquement des attributs
    """

    def __init__(self, name):
        """

        :param name: Nom du noeud
        """
        self.name = name
        # 0 False 1 True None on ne fixe pas de valeur
        self.activ = None
        self.proba = None
        # liste des noeud connecter a celui-ci (fleche qui point sur lui)
        self.connect_node = list()

    def add_connection(self, node):
        """
        Ajoute une connection en fin de liste (la derrnier connection sera a la fin de la liste)
        :param node:
        :return:
        """
        if self.proba is not None:
            raise ValueError("Erreur la proba a été déja fixer")

        self.connect_node.append(node)

    def set_proba(self, *proba_list):
        """
        Rajoute la probabiliter du noeud
        :param proba_list: Liste des proba sous la forme

            Parent 0, Parent 1, Noeud self
            False False False  proba_list index 0
            False  False True  proba_list index 1
            False True False   proba_list index 2
            False  True True   proba_list index 3

            True False False  proba_list index 4
            True  False True  proba_list index 5
            True True False   proba_list index 6
            True  True True   proba_list index 7
            Cette fonction prendra en compte l'ordre de la liste connect_node la premier connection sera la colomne la
            plus a gauche celle ou c'est valeur True, False bouge le moin.
            La derrnier connection sera la connection la plus a droit - 1.
            La derrnière colomne sera le npeud en luis maime (les valeur de true, false bouge le plusse)
        :return:
        """
        # on controle que la liste donnée corespond au nombre de connection que a le noeud
        # +1 car il y a ce noeud a prend en compt
        if len(proba_list) != 2 ** (len(self.connect_node) + 1):
            raise ValueError("Erreur le nombre de proba donnée de corespon pas au nombre de valeur:\n"
                             "Vous avez donner {} proba pour {} connection "
                             "nombre de proba attendu {}".format(len(proba_list), len(self.connect_node),
                                                                 2 ** (len(self.connect_node) + 1)))

        # petit cas exeptionelle si c'est un noeud sans connection vers lui
        if len(self.connect_node) == 0:
            self.proba = {True: proba_list[0], False: proba_list[1]}
            return

        # on fait une table sous la forme [(F, F, F), (F, F, T), ..., (T, T, T)]
        table = list(itertools.product([False, True], repeat=len(self.connect_node) + 1))
        self.proba = {}
        # on init les deux parents car on passe la premier colomne
        nb_colomne = len(table[0])
        for ligne in range(len(table)):
            # si il n'exite pas on cree un dic colomne 0 sont les aorent
            self.proba[table[ligne][0]] = self.proba.get(table[ligne][0], {})
            # on recupaire le dico pour le modifer
            dic_prec = self.proba[table[ligne][0]]
            # on ne traite pas la première colomne car elle ne change que 2 fois
            # est la derrnier colomne car on ne cree un dic mais on mais la valeur de la proba
            for colomne in range(1, nb_colomne - 1):
                # si il n'exite pas on cree un dic
                dic_prec[table[ligne][colomne]] = dic_prec.get(table[ligne][colomne], {})
                # on recupaire le dico pour le modifer
                dic_prec = dic_prec[table[ligne][colomne]]
            # pour la derrnier colomne on rajoute la proba
            dic_prec[table[ligne][nb_colomne - 1]] = proba_list[ligne]

    def set_true(self):
        """
        Mais le noeud a True
        :return:
        """

        self.activ = True

    def set_false(self):
        """
        Mais le noeud a False
        :return:
        """

        self.activ = False

    def remove_activ(self):
        """
        Mais le noeud a neutre
        :return:
        """

        self.activ = None

    def remove_proba(self):
        """
        Remais la probabiliter de se noeud a None
        :return:
        """
        self.proba = None

    def get_proba(self):
        """
        Fonction qui renvoie la probabiliter du noeud en fonction de l'état de c'est voisin
        :return:
        """
        if self.activ is None:
            raise ValueError("Erreur le noeud est a None")

        if self.proba is None:
            raise ValueError("Erreur la table de probabiliter de ce n'a pas été faite")

        # si il n'y a pas de connection
        if len(self.connect_node) == 0:
            return self.proba[self.activ]

        temp = self.proba
        for node in self.connect_node:
            if node.activ is None:
                raise ValueError("Erreur un noeud a une valeur sous la forme None")
            temp = temp[node.activ]
        # puis on renvoie la valeur
        return temp[self.activ]

    def __str__(self):

        return "{} Activ: {} Proba: {}".format(self.name, self.activ, self.proba)


if __name__ == "__main__":
    pass
