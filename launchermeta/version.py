from __future__ import print_function

from .download import Download

__title__ = 'Version'
__author__ = 'TheDestruc7i0n'
__version__ = '0.0.1'


class Version:
    def __init__(self, data):
        self.raw = data

    def get_libraries(self):
        """
        Will return the libraries of the version, in raw JSON

        :return: a dict of libraries
        :rtype: list
        """
        return self.raw['libraries']

    def get_client_download(self):
        """
        Get the client download

        :return: a Download instance
        :rtype: Download
        """
        dl = self.raw['downloads']['client']
        return Download(dl)

    def get_server_download(self):
        """
        Get the server download

        :return: a Download instance
        :rtype: Download
        """
        dl = self.raw['downloads']['server']
        return Download(dl)
