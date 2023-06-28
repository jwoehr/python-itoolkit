# -*- coding: utf-8 -*-
import warnings
import os
from ..transport.http import HttpTransport
from ..toolkit import iToolKit


class iRestCall(HttpTransport):  # noqa N801
    """
    Transport XMLSERVICE calls over standard HTTP rest.
    """

    def __init__(
        self,
        iurl: str,
        iuid: str,
        ipwd: str = None,
        idb2: str = 0,
        ictl: str = 0,
        ipc: str = 0,
        isiz: str = 0,
    ):
        """
        Example:
          from itoolkit.rest.irestcall import *
          itransport = iRestCall(url,user,password)

        Parameters
        ----------
        iurl : str
            XMLSERVICE url, eg. https://example.com/cgi-bin/xmlcgi.pgm.
        iuid : str
            Database user profile name.
        ipwd : str, optional
            Database user profile password
            -- or --
            env var PASSWORD (export PASSWORD=mypass). The default is None.
        idb2 : str, optional
            Database (WRKRDBDIRE *LOCAL). The default is 0.
        ictl : str, optional
            XMLSERVICE control ['*here','*sbmjob'. The default is 0.
        ipc : str, optional
            XMLSERVICE route for *sbmjob '/tmp/myunique'. The default is 0.
        isiz : str, optional
            XMLSERVICE expected max XML output size. The default is 0.

        Returns
        -------
        None.

        """
        warnings.warn(
            "iRestCall is deprecated, " "use itoolkit.transport.HttpTransport instead",
            category=DeprecationWarning,
            stacklevel=2,
        )

        if not ictl:
            ictl = "*here *cdata"

        if not ipc:
            ipc = "*na"

        if not ipwd:
            ipwd = os.environ["PASSWORD"]

        if not idb2:
            idb2 = "*LOCAL"

        if isiz not in (0, self.OUT_SIZE):
            msg = "isiz is deprecated, changed to {}".format(self.OUT_SIZE)
            warnings.warn(msg, category=DeprecationWarning, stacklevel=2)

        super().__init__(
            url=iurl, user=iuid, password=ipwd, database=idb2, ctl=ictl, ipc=ipc
        )

    def call(self, itool: iToolKit) -> str:
        """
        Call XMLSERVICE with accumulated actions.

        Parameters
        ----------
        itool : iToolkit
            An iToolkit object.

        Returns
        -------
        str
            The XML returned from XMLSERVICE.

        """

        return super().call(itool)
