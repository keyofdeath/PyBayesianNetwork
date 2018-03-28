#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BazeGraph import Graph
import itertools


class BazeGraph(object):
    """
    Class qui implémente un Réseau Bayésien
    Cette class herite du type Object. Pour donner la possibiliter de lui rajouter dynamiquement des attributs
    """

    def __init__(self):

        self.graph = Graph()
        self.observation = list()

    def add_node(self, node):
        """
        Ajoute un noeud dans le graph
        :param node: Noeud a ajouter
        :return:
        """
        self.graph.add_node(node)

    def link_node(self, node_a, node_b):
        """
        Ajoute un lient entre a et b c'est A vers A node_a --> node_b
        Si A ou (et) B ne sont pas dans le graph il seront ajouter automatiquement
        :param node_a: noeud A dois êtres de type Node
        :param node_b: noeud B dois êtres de type Node
        :return:
        """
        self.graph.add_direction_link(node_a, node_b)
        node_b.add_connection(node_a)

    def get_all_other_node(self, node):
        """
        Fonction qui renvoie tout les noeud - les noeuds observer - le noeud que l'on veux determiner sa proba
        :param node: Noeud utiliser pour savoir sa proba proba
        :return: Une liste de noeud
        """
        return list(filter(lambda n: n.name != node.name and n not in self.observation, self.graph.get_all_node()))

    def get_proba(self, node_to_get_proba):
        """
        Donne la probabiliter que le noeud passer en paramètre sois a vrais ou a faux
        :param node_to_get_proba: Noeud de Type Node que l'on dois déterminer sa probabiliyer
        :return: La probabiliter si se noeud est a True, La probabiliter si se noeud est a False
        La probabiliter renvoiller est entre [0, 1]
        """

        # on recupaire tout les autres noeuds sans les noeuds node_to_get_proba et self.observation
        node_to_change = self.get_all_other_node(node_to_get_proba)

        # on fait une table sous la forme [(F, F, F), (F, F, T), ..., (T, T, T)]
        table = list(itertools.product([False, True], repeat=len(node_to_change)))

        # probabiliter du noeud demander (index 0 = noeud a True, index 1 = noeud a False)
        proba_x = [0, 0]
        somme = 1
        mode_node = [True, False]

        for mode in range(2):
            node_to_get_proba.activ = mode_node[mode]
            # calcul en fonction des changement d'état des autre noeud
            # on parcour chaque ligne de notre table
            for ligne in table:
                # on mais les autre noeud a leur étas
                for i in range(len(node_to_change)):
                    node_to_change[i].activ = ligne[i]
                # une fois tout les noeud mis a leurs état on recupaire leur proba
                for node in node_to_change + self.observation + [node_to_get_proba]:
                    somme *= node.get_proba()
                proba_x[mode] += somme
                somme = 1
        alpha = sum(proba_x)
        return proba_x[0] / alpha, proba_x[1] / alpha

    def set_observation(self, *node_list):
        """
        Ajoute une liste de noeud en observation. C'est noeud de bougeron pas il resteron a la maime valeur
        :param node_list: Liste de paramètre de type Node
        :return:
        """

        self.observation.extend(node_list)

    def __str__(self):

        return str(self.graph)


if __name__ == "__main__":
    pass
