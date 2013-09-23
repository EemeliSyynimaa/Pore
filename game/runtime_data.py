# -*- coding: utf-8 -*-
__author__ = 'eeneku'

from engine import resource_manager


class RuntimeData(object):
    """
    A class to store runtime data.
    """

    def __init__(self):
        self.res = resource_manager.ResourceManager()