# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Class and other objects that must be defined before core can be
imported.

"""

from abc import ABC


class Object(ABC):
    """Abstract base class for objects."""

    def __str__(self):
        """Generic string formatter."""

        return str(self.__class__) + ": " + str(self.__dict__)
