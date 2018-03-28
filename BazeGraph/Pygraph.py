#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


class Graph(object):
    def __init__(self, dict_graph=None):
        """
        Constructeur du graph
        :param dict_graph: dictionnaire du graph sous le forme
            {
                noeud 1 : [[voisin 1, poid du lien], ...,[voisin n, poid du lien]],
                ...
                noeud n : [[voisin 1, poid du lien], ...,[voisin n, poid du lien]]
            }
        """
        if dict_graph is None:
            dict_graph = dict()
        # Graph orienter et non orienter
        self.__dictGraph = dict_graph
        # Graph non orienter
        self.__dictGraphConnect = dict()
        self.__nbLink = 0
        self.DEFAULT_WEIGHT = 1
        self.NODE_VALUE = 0
        self.NODE_LINK_WEIGHT = 1
        self.tab_node = list()

    def add_node(self, node):
        """
        Ajoute un noeud dans le graph
        :param node:
        :return: True noeud ajouter false noeud existe deja
        """
        if node not in self.__dictGraph:
            self.__dictGraph[node] = list()
            self.tab_node.append(node)
            self.__dictGraphConnect[node] = list()
            return True
        else:
            return False

    def add_direction_link(self, node_a, node_b, weight=1):
        """
        Ajoute une liaison qui vas du noeud A vers le noeud B sous la forme [valeur du neud, poid de la liaison]
        :param node_a:
        :param node_b:
        :param weight: Poids du lien par defaut 1
        :return:
        """
        self.__nbLink += 1
        # Si le noeud A n'est pas dans notre graph on l'ajoute
        if node_a not in self.__dictGraph:
            self.add_node(node_a)

        # Si le noeud B n'est pas dans notre graph
        if node_b not in self.__dictGraph:
            self.add_node(node_b)

        # Si le noeud A na pas de lien avec le noeud B
        if node_b not in self.__dictGraph[node_a]:
            self.__dictGraph[node_a].append([node_b, weight])
            self.__dictGraphConnect[node_a].append(node_b)

    def add_link(self, node_a, node_b, weight=1):
        """
        Ajoute un lien non orientee entre les deux noeud passer en paramètre sous la forme
        [valeur du neud, poid de la liaison]
        :param node_a:
        :param node_b:
        :param weight: Poids du lien par defaut 1
        :return: Rien
        """
        self.__nbLink += 1
        if node_a not in self.__dictGraph:
            self.add_node(node_a)
        if node_b not in self.__dictGraph:
            self.add_node(node_b)
        if node_b not in self.__dictGraph[node_a]:
            self.__dictGraph[node_a].append([node_b, weight])
            self.__dictGraphConnect[node_a].append(node_b)
        if node_a not in self.__dictGraph[node_b]:
            self.__dictGraph[node_b].append([node_a, weight])
            self.__dictGraphConnect[node_b].append(node_a)

    def get_node_neighbour(self, node):
        """
        Methode qui renvoie la liste de tout les noeud adjacent au noeud donee en paramètre
        :param node: Noeud pour obtenire c'est vosin
        :return: Liste des voisin du noeud donnee [noeud 1, ..., noeud n]
        """
        res = list()
        for n in self.__dictGraph[node]:
            res.append(n[self.NODE_VALUE])
        return res

    def get_node_neighbour_link_weight(self, node):
        """
        Methode qui renvoie le poids des liens voisin
        :param node:
        :return:
        """
        res = list()
        for n in self.__dictGraph[node]:
            res.append(n[self.NODE_LINK_WEIGHT])
        return res

    def get_node_neighbour_weight_and_value(self, node):
        """

        :return:
        """
        return self.__dictGraph[node]

    def get_all_node_connection(self, node):
        """
        Renvoie tout les connection du noeud
        Exemple: A --> B B est connecter a A maime si c'est un lie, orienter
        :param node:
        :return:
        """
        return self.__dictGraphConnect[node]

    def get_all_node_copie(self):
        """

        :return:
        """
        return deepcopy(self.tab_node)

    def get_all_node(self):
        """

        :return:
        """
        return self.tab_node

    def get_tab_node_filtre(self, filtre_func):
        """
        Renvoie une liste de neoud en fonction de la fonction de recher donne en paramètre
        :param filtre_func: fonction qui renvoie true si c'est le noeud que on veut
        :return:
        """
        return list(filter(lambda node: filtre_func(node), self.tab_node))

    def get_nb_link(self):
        """

        :return:
        """
        return self.__nbLink

    def remove_link(self, node1, node2):
        """

        :param node1:
        :param node2:
        :return:
        """
        pass

    def getDistBetweenNode(self, node1, node2):
        """

        :param node1:
        :param node2:
        :return:
        """
        pass

    def aStar(self, start_node, end_node):
        """

        :param start_node:
        :param end_node:
        :return:
        """
        pass

    def chemin_plus_court(self, start_node, end_node):
        """

        :param self:
        :param start_node:
        :param end_node:
        :return:
        """
        global best_road, best_dist
        # On mais [node_to_explor] car la case ou on commence est visite
        best_road = list()
        best_dist = -1

        def dfs(graph_cc, road, visit_node, node, end_node, nb_dist):
            """

            :param graph_cc: graph a explorer
            :param road: route courante
            :param visit_node: liste qui contien les noeud deja visiter
            :param node: neud courent
            :param end_node: noeud que on veut explorer
            :param nb_dist: distance parcouru
            :return:
            """
            global best_road, best_dist
            # Trouver le bue

            if best_dist != -1:
                # Cut off pour eviter une explosion combinatoire
                if nb_dist > best_dist:
                    # backtracking
                    road.pop(len(road) - 1)
                    visit_node.pop(len(visit_node) - 1)
                    return

            if node == end_node:
                print("Found solution with {} move".format(nb_dist))
                if nb_dist < best_dist or len(best_road) == 0:
                    best_road = deepcopy(road)
                    best_dist = nb_dist

                # on revien en arrière
                road.pop(len(road) - 1)
                # On retire les noeud visiter
                visit_node.pop(len(visit_node) - 1)
                return best_road

            for neighbour in graph_cc.get_node_neighbour_weight_and_value(node):
                # on prend que le noeud
                dist = neighbour[1]
                neighbour = neighbour[0]
                if neighbour not in visit_node:
                    road.append(neighbour)
                    visit_node.append(neighbour)
                    dfs(graph_cc, road, visit_node, neighbour, end_node, dist + nb_dist)

            # backtracking
            road.pop(len(road) - 1)
            visit_node.pop(len(visit_node) - 1)
            print(best_dist)
            return best_road

        return deepcopy(dfs(self, [start_node], [start_node], start_node, end_node, 0))

    def depth_first_search_node(self, node_to_explor):
        """
        fait une recherche en profondeur en parent du noeud donee
        :param node_to_explor: noeud de depart
        :return:
        """
        tab_noeud_explorer = list()

        def aux(visit_node, node):
            """

            :param visit_node: liste des noeud visite
            :param node:
            :return:
            """
            tab_noeud_explorer.append(node)
            for neighbour in self.get_node_neighbour(node):

                if neighbour not in visit_node:

                    print("- node ", node, " to ", neighbour)
                    visit_node.append(neighbour)
                    aux(visit_node, neighbour)

        # On mais [node_to_explor] car la case ou on commence est visite
        aux([node_to_explor], node_to_explor)

        return tab_noeud_explorer

    def breadth_first_search(self, node_to_explore):
        """

        :param node_to_explore:
        :return:
        """

        depth_cc = 1
        tab_neighbour_to_explore = [node_to_explore]
        tab_explore_node = [node_to_explore]

        # Tant que il y a des voisin a explorer
        while len(tab_neighbour_to_explore) > 0:

            print("Profondeur ", depth_cc, " ateint noeud de la largeur: ", tab_neighbour_to_explore)
            depth_cc += 1

            next_tab_neighbour = list()
            # Parcoure des noeud explorer en largeur
            for node in tab_neighbour_to_explore:
                # Parcoure des voisin des noeud explorer en largeur
                for node_explore in self.get_node_neighbour(node):
                    # Si se n'est pas un noeud déja explorer
                    if node_explore not in tab_explore_node:
                        tab_explore_node.append(node_explore)
                        next_tab_neighbour.append(node_explore)

            tab_neighbour_to_explore = deepcopy(next_tab_neighbour)

    def est_connexe(self, startNode):

        tab_node_explore = self.depth_first_search(startNode)
        tab_node_graph = self.get_all_node()

        # on parcour eles noeud de notre graph pour voie si on les a explorer avec la profondeur
        for node in tab_node_graph:
            if node not in tab_node_explore:
                return False
        return True

    def is_tree(self):
        """
        Methode qui renvoie si le graph est un arbre est donc il sera connex
        :return:
        """

        return (len(self.get_all_node()) - 1) == self.get_nb_linck()

    def __str__(self):

        result = ""

        for key in self.get_all_node():
            result += "node {}:\n".format(key)
            for neibhour in self.__dictGraph[key]:
                result += "\tneighbour {}: {}\n".format(str(neibhour[0]), neibhour[1])
            result += "\n\n"

        return result


if __name__ == '__main__':
    pass
