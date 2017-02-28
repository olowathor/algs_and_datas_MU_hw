#!/usr/bin/python3


###########################
# Dotaz studenta: 
# 
# 
###########################

# Chcete-li dostat odpoved, vlozte do nazvu souboru heslo KONTROLA.


# IB002 Extra domaci ukol 1.
#
# Vasi ulohou v tomto priklade je modifikovat jiz existujici strukturu
# oboustranne zretezeneho linearniho seznamu.
#
# Oboustranne zretezeny seznam je definovan ukazatelem first, ktery
# ukazuje na zacatek seznamu, a ukazatelem last, ktery ukazuje na konec
# seznamu.
#
# Seznam s uzly a, b, c, d, e, f vypada bezne takto (v nakresu
# vynechavame ukazatele first a last):
#       ___   ___   ___   ___   ___
#      /   \ /   \ /   \ /   \ /   \
#     a <-- b <-- c <-- d <-- e <-- f
#
# kde obloucky nad pismeny reprezentuji dopredne sipky (napr. a --> b),
# tedy ukazatele next.
#
# Nas modifikovany StrangeList pouziva pro reprezentaci stejne promenne,
# pouze ukazatele ukazuji jinam. Ukazatele next budou ukazovat ob jeden
# uzel, ukazatele prev zustanou zachovany. Po prevedeni predchoziho
# seznamu na StrangeList vznikne takovyto seznam (opet vynechavame
# ukazatele first a last):
#       _________   _________
#      /         \ /         \
#     a <-- b <-- c <-- d <-- e <-- f
#            \_________/ \_________/
#
# StrangeList je take definovan ukazatelem first, ktery ukazuje na jeho
# zacatek, a ukazatelem last, ktery ukazuje na jeho konec, v tomto pripade
# first - a, last - f.


# Ukol 1.
# Definujte datovou strukturu StrangeList.
# Muzete se inspirovat definici ze zakladniho domaciho ukolu.

# TODO

class StrangeNode:
    """Trida StrangeNode slouzi pro reprezentaci objektu v oboustranne
    spojovanem divnem seznamu.

    Atributy:
    value   reprezentuje ulozenou hodnotu/objekt
    next    reference na prvek v seznamu nacházející se za následujícím
    prev    reference na predchazejici prvek v seznamu
    """
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class StrangeList:
    """Trida StrangeList reprezentuje divne spojovany seznam.

    Atributy:
    first   reference na prvni prvek seznamu
    last    reference na posledni prvek seznamu
    """
    def __init__(self):
        self.first = None
        self.last = None


def strangeInsert(strangeList, value):
    """Metoda strangeInsert() vlozi na konec seznamu strangeList (za prvek last)
    novy uzel s hodnotou value. Vraci nove vlozeny objekt.
    """
    snode = StrangeNode()
    snode.value = value

    if strangeList.first is None:
        strangeList.first = snode
        strangeList.last = snode
    else:
        snode.prev = strangeList.last

        if strangeList.last.prev is not None:
            '''Existuji minimalne 3 uzly'''
            strangeList.last.prev.next = snode    

    strangeList.last = snode

    return snode


def strangeSearch(strangeList, value):
    """Metoda search() vraci referenci na prvni vyskyt uzlu s hodnotou
    value v seznamu strangeList. Pokud se hodnota v seznamu nenachazi,
    vraci None.
    """
    node = strangeList.last
    firstVal = None
    while node is not None: 
        if node.value != value:
            node = node.prev
        else:
            firstVal = node

    return firstVal


def strangeDelete(strangeList, snode):
    """Metoda delete() smaze uzel snode v seznamu strangeList."""
    if strangeList.first is strangeList.last:
        '''Existuje jeden/zadny uzel'''
        strangeList.first = None
        strangeList.last = None
    elif snode.prev is None:
        '''Uzel je prvni'''
        if snode.next is not None:
            '''Existuji minimalne 3 uzly'''
            strangeList.first.next.prev.prev = None
            strangeList.first = snode.next.prev
        else:
            '''Existuji 2 uzly'''
            strangeList.last.prev = None
            strangeList.first = strangeList.last
    elif snode.next is None:
        '''Uzel je posledni, nebo predposledni'''
        if snode is strangeList.last:
            '''Uzel je posledni'''
            if strangeList.last.prev.prev is not None:
                '''Existuji minimalne 3 uzly'''
                strangeList.last.prev.prev.next = None
                strangeList.last = snode.prev
        else:
            '''Uzel je predposledni'''
            if strangeList.last.prev.prev is not None:
                '''Existuji minimalne 3 uzly'''
                strangeList.last.prev.prev.next = None
                strangList.last.prev = snode.prev
        
    else:
        
        snode.prev.next = snode.next
        snode.next.prev = snode.prev

# Ukol 2.
# Implementujte metodu list_to_strange_list, ktera z oboustranne
# zretezeneho seznamu vytvori nas StrangeList.
# Reprezentaci oboustranne zretezeneho seznamu muzete prevzit ze
# zakladniho domaciho ukolu.

class Node:
    """Trida Node slouzi pro reprezentaci objektu v oboustranne
    spojovanem seznamu.

    Atributy:
    value   reprezentuje ulozenou hodnotu/objekt
    next    reference na nasledujici prvek v seznamu
    prev    reference na predchazejici prvek v seznamu
    """
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class LinkedList:
    """Trida LinkedList reprezentuje spojovany seznam.

    Atributy:
    first   reference na prvni prvek seznamu
    last    reference na posledni prvek seznamu
    """
    def __init__(self):
        self.first = None
        self.last = None

def insert(linkedList, value):
    """Metoda insert() vlozi na konec seznamu linkedList (za prvek last)
    novy uzel s hodnotou value. Vraci nove vlozeny objekt.
    """
    node = Node()
    node.value = value
    if linkedList.first is None:
        linkedList.first = node
    else:
        node.prev = linkedList.last

    linkedList.last = node
    return node


def print_list(linkedList):
    """Metoda print_list() vypise seznam linkedList."""
    node = linkedList.first
    while (node is not None):
        print(node.value)
        node = node.next


def search(linkedList, value):
    """Metoda search() vraci referenci na prvni vyskyt uzlu s hodnotou
    value v seznamu linkedList. Pokud se hodnota v seznamu nenachazi,
    vraci None.
    """
    node = linkedList.first
    while node is not None: 
        if node.value != value:
            node = node.next
        else:
            return node

    return node


def delete(linkedList, node):
    """Metoda delete() smaze uzel node v seznamu linkedList."""
    if linkedList.first is linkedList.last:
        linkedList.first = None
        linkedList.last = None
    elif node.prev is None:
        node.next.prev = None
        linkedList.first = node.next
    elif node.next is None:
        node.prev.next = None
        linkedList.last = node.prev
    else:
        node.prev.next = node.next
        node.next.prev = node.prev


def list_to_strange_list(linkedList):
    pass
    # TODO
    


# Ukol 3.
# Implementujte metodu check_strange_list, ktera zkontroluje, ze
# ukazatele first a last jsou nastaveny spravne.

def check_strange_list(strangeList):
    pass
    # TODO
