# implement tuple
# are immutable - doesn't support item assignment
# check if it creates a new tuple - with a new memory address!

# side note: if we dynamcially resize an array does that still
# use the same memory address of previous elements


from __future__ import annotations
from icecream import ic
from itertools import chain
from typing import Any, Iterable


class Tuple1:
    """
    Named differently to standard Python Tuple class ot distinguish it  
    """

    def __init__(self, items: Iterable[Any]):
        self._items = list(items)

    def __repr__(self) -> str:
        # we need to override this because otherwise it's going to
        # give the memory address of where it is stored
        return str(self)

    def __str__(self) -> str:
        # repr here is not same the Tuple repr of 'x' for strings, numbers etc unless
        # if x is a Tuple e.g. like Tuple([2, 3]) in Tuple([Tuple([2, 3]), Tuple([4, 5])]) then yes it'd be calling the
        # repr we defined above
        return "(" + ", ".join(repr(x) for x in self._items) + ")"

    def __add__(self, other: Tuple1):
        # extends tuple by appending it
        # generator implementation.
        # here we are creating an iterator using chain and then passing it into the Tuple1 class
        # create a new tuple1 because Tuples are immutable and don't share the same memory address
        return Tuple1(chain([*self._items, *other._items]))

        # # list method
        # new_items = self._items.copy()
        # new_items.extend(other._items)
        # return Tuple(new_items)  # this prints our repr defined above

    def __mul__(self, n: int):
        new_items = []
        for _ in range(n):
            new_items.extend(self._items)
        return Tuple1(new_items)

