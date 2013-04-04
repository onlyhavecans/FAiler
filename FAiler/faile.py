#!/usr/bin/env python
import re
import os
from datetime import datetime
from FAiler.exceptions import FAError


class FAile():
    """
    Represents a file downloaded from FurAffinity.
    The base parameters of this class are public access read safe by design

    FAile.directory: the directory to the supplied file or pwd if not supplied
    FAile.filename: the full name of the supplied file. This never changes
    FAile.date: When this was uploaded
    FAile.artist: the name of the user who uploaded this
    FAile.name: the name of the submitted file
    FAile.fileType: The extension of the submitted file

    Some example files
    1201126929.[koh]_fooooom_toaster.jpg
    1362739849.wolfy-nail_2013-03-01-djzing.jpg
    """
    directory = None
    filename = None
    date = None
    artist = None
    name = None
    fileType = None

    def __init__(self, faFile):
        """
        This accepts both a standard name or with path to file.

        :param faFile: Name of or path to a file from FA
        :raise: FAError if the file name cannot be parsed.
        """
        self.directory = os.path.dirname(faFile)
        self.filename = os.path.basename(faFile)
        self._parse_name(self.filename)  # Raises on fail

    def __repr__(self):
        """
        :return: the original filename as a string
        """
        return str(self.filename)

    def _parse_name(self, name):
        """
        Don't repeat yourself.
        This assigns everything from the filename and raises FAError on fail
        :raises: FAError if name does not parse
        """
        faRe = re.compile(r'(\d+)\.([\w\[\]~.-]+?)_(\S+)\.(\w{2,4})')
        parsed = re.match(faRe, name)
        if parsed is None:
            raise FAError("Unable to parse file name: " + name)
        self.date, self.artist, self.name, self.fileType = parsed.groups()
        self.date = datetime.fromtimestamp(int(self.date))

    def clean_reupload(self):
        """
        Often enough someone downloads a file from FA and then re-uploads it
        This checks for that and changes the Number, User, & Name to that of
         the "original" uploader.
        The basename is kept unchanged

        ex;
        >>> from FAiler import FAile
        >>> f2 = FAile('1362168441.shim_1362116845.furball_shim_bday2013.jpg')
        >>> "{} - {}.{}".format(f2.artist, f2.name, f2.fileType)
        'shim - 1362116845.furball_shim_bday2013.jpg'
        >>> f2.clean_reupload()
        >>> "{0.artist} - {0.name}.{0.fileType}".format(f2)
        'furball - shim_bday2013.jpg'
        """
        try:
            self._parse_name("{0.name}.{0.fileType}".format(self))
        except FAError:
            pass  # We don't care if parse fails this time around
