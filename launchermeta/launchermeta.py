from __future__ import print_function
import urllib
import json

from .version import Version

__title__ = 'LauncherMeta'
__author__ = 'TheDestruc7i0n'
__version__ = '0.0.1'


class LauncherMeta(object):
    def __init__(self):
        self.url = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'
        self.launchermeta = None
        self.update_launchermeta()

    @staticmethod
    def get_url(url):
        """
        Gets a url and converts to json

        :param url: url to get
        :returns: json
        :rtype: json
        """
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        return data

    def _get_by_id(self, id):
        """
        Gets a version by ID

        :param id: id to get
        :returns: a dict of the version
        :rtype: dict
        """
        versions = self.launchermeta['versions']
        for v in versions:
            if v['id'] == id:
                return v
        return False

    def get_launchermeta(self):
        """
        Gets the launchermeta from the Mojang url

        :returns: json of launchermeta
        :rtype: json
        """
        launchermeta = self.get_url(self.url)
        return launchermeta

    def update_launchermeta(self):
        """
        Updates the launchermeta

        :returns: True
        :rtype: bool
        """
        self.launchermeta = self.get_launchermeta()
        return True

    def get_latest_snapshot(self):
        """
        Gets the latest snapshot version

        :returns: a Version instance
        :rtype: Version
        """
        latest_version = self.launchermeta['latest']['snapshot']
        latest_version_dict = self._get_by_id(latest_version)
        latest_data = self.get_url(latest_version_dict['url'])
        latest = Version(latest_data)
        return latest

    def get_latest_release(self):
        """
        Gets the latest release version

        :returns: a Version instance
        :rtype: Version
        """
        latest_version = self.launchermeta['latest']['release']
        latest_version_dict = self._get_by_id(latest_version)
        latest_data = self.get_url(latest_version_dict['url'])
        latest = Version(latest_data)
        return latest

    def get_version_by_id(self, id):
        """
        Gets a version by id

        :param id: id to get by
        :returns: a Version instance
        :rtype: Version
        """
        version_dict = self._get_by_id(id)
        if not version_dict:
            raise Exception('Invalid version!')
        else:
            version_data = self.get_url(version_dict['url'])
            version = Version(version_data)
            return version
