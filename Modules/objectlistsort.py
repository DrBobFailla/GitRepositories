"""Inputs a list of objects and sorts the list of objects based on a key within the object."""

__author__ = "Failla"
__date__ = "6/19/21"
def olsort(articlelist):
    articlelist.sort(key=lambda x: x.publishedat)
    return articlelist