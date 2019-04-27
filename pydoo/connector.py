# -*- coding: utf-8 -*-


from .models import Environment


class Odoo(object):
    def __init__(self, url, db, username, password, transport=None, encoding=None, verbose=0, allow_none=0,
                 use_datetime=0, context=None, use_ssl=False):
        """

        :param url:
        :param db:
        :param username:
        :param password:
        :param transport:
        :param encoding:
        :param verbose:
        :param allow_none:
        :param use_datetime:
        :param context:
        """
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.transport = transport
        self.encoding = encoding
        self.verbose = verbose
        self.allow_none = allow_none
        self.use_datetime = use_datetime
        self.context = context
        self.use_ssl = use_ssl
        self._env = Environment(self, context=context)

    @property
    def env(self):
        """

        :return:
        :rtype: Environment
        """
        return self._env
