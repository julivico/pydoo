# -*- coding: utf-8 -*-

from .model import Model
from ..core import Connection


class Environment(object):
    def __init__(self, odoo, context={}):
        super(Environment, self).__init__()
        self._queue = {}
        self._odoo = odoo
        self.conn = Connection(odoo, context=context)

    @property
    def odoo(self):
        return self._odoo

    def __getitem__(self, name):
        return self._queue.setdefault(name, Model(name, self.conn))
