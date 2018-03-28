#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BazeGraph import *


def plui():
    """
    Fonction test qui determine la probabiliter qu'il pleux sachant que le solle est mouiller
    :return:
    """

    # Creation du graph
    baze = BazeGraph()
    # creation des neouds
    nuage = Node("nuage")
    rain = Node("rain")
    arroser = Node("arroser")
    sole_mouiller = Node("sole mouiller")

    # Schéma du graph qui sera crée
    #                       Nuage
    #                     /       \
    #                arroser       Plui
    #                     \       /
    #                    solle mouiller
    # nuage --> arroser
    baze.link_node(nuage, arroser)

    # nuage --> rain
    baze.link_node(nuage, rain)

    # Arroser --> Solle mouiller
    baze.link_node(arroser, sole_mouiller)
    # Pluis --> Solle mouiller
    baze.link_node(rain, sole_mouiller)

    # nuage = False, nuage = True
    nuage.set_proba(0.5, 0.5)

    # Nuage = False & Arroser = False, Nuage = False & Arroser = True
    # Nuage = True & Arroser = False, Nuage = True & Arroser = True
    arroser.set_proba(0.5, 0.5, 0.9, 0.1)
    rain.set_proba(0.8, 0.2, 0.2, 0.8)

    # ordre des colomne (arroser, rain, solle mouiller)
    sole_mouiller.set_proba(1, 0, 0.1, 0.9, 0.1, 0.9, 0.01, 0.99)

    # on mais notre solle mouiller a True comme evidence
    sole_mouiller.set_true()

    # on ajoute le sole mouiller comme observation (sa valeur ne va pas bouger)
    baze.set_observation(sole_mouiller)

    # pn veut savoir la probailiter de p(rain | sole mouiller)
    plui_true, plui_false = baze.get_proba(rain)
    print("Proba: p(Plui=True|Sole mouiller) = ", plui_true)
    print("Proba: p(Plui=False|Sole mouiller) = ", plui_false)


def arrosage():
    """
    Fonction Test qui determine la probabiliter que l'on est arroser
    sachan que le sole sois mouiller et que se sois nuageux
    :return:
    """

    # Creation du graph
    baze = BazeGraph()
    # creation des neouds
    nuage = Node("nuage")
    rain = Node("rain")
    arroser = Node("arroser")
    sole_mouiller = Node("sole mouiller")

    # Schéma du graph qui sera crée
    #                       Nuage
    #                     /       \
    #                arroser       Plui
    #                     \       /
    #                    solle mouiller
    # nuage --> arroser
    baze.link_node(nuage, arroser)

    # nuage --> rain
    baze.link_node(nuage, rain)

    # Arroser --> Solle mouiller
    baze.link_node(arroser, sole_mouiller)
    # Pluis --> Solle mouiller
    baze.link_node(rain, sole_mouiller)

    # nuage = False, nuage = True
    nuage.set_proba(0.5, 0.5)

    # Nuage = False & Arroser = False, Nuage = False & Arroser = True
    # Nuage = True & Arroser = False, Nuage = True & Arroser = True
    arroser.set_proba(0.5, 0.5, 0.9, 0.1)
    rain.set_proba(0.8, 0.2, 0.2, 0.8)

    # ordre des colomne (arroser, rain, solle mouiller)
    sole_mouiller.set_proba(1, 0, 0.1, 0.9, 0.1, 0.9, 0.01, 0.99)

    # on mais nuage a True comme evidence
    nuage.set_true()
    # on mais notre solle mouiller a True comme evidence
    sole_mouiller.set_true()

    # on ajoute le sole mouiller et buageux comme observation (sa valeur ne va pas bouger)
    baze.set_observation(sole_mouiller, nuage)

    # puis on veut savoir la probailiter de p(aroser | nuageux, sole mouiller)
    nuageux_true, nuageux_false = baze.get_proba(arroser)
    print("Proba: p(Arroser=True|Nuage, Sole mouiller) = ", nuageux_true)
    print("Proba: p(Arroser=False|Nuage, Sole mouiller) = ", nuageux_false)


if __name__ == '__main__':
    arrosage()
