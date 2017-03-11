from __future__ import print_function
import urllib

__title__ = 'Download'
__author__ = 'TheDestruc7i0n'
__version__ = '0.0.1'


class Download:
    def __init__(self, download):
        self.raw = download

    def get_file_url(self):
        """
        Gets the raw file url

        :returns: file url
        :rtype: str
        """
        return self.raw['url']

    def download_to(self, to, check_sha1 = True):
        """
        Downloads the file to a location

        :param to: location to download to
        :param check_sha1: should check if sha1 matches
        :returns: tuple of the location and headers
        :rtype: tuple
        """
        return urllib.urlretrieve(self.get_file_url(), to)
