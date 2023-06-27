# -*- coding: utf-8 -*-
import warnings
from ..transport.direct import DirectTransport


class iLibCall(DirectTransport):  # noqa N801 gotta live with history
    """
    Transport XMLSERVICE direct job call (within job/process calls).

    """

    def __init__(
        self,
        ictl: str = "*here *cdata",
        ipc: str = "*na",
        iccsid: str = 0,
        pccsid: str = 1208,
    ):
        """
        Parameters
        ----------
        ictl : str, optional
            XMLSERVICE control ['*here','*sbmjob']. The default is '*here *cdata'.
        ipc : str, optional
            XMLSERVICE job route for *sbmjob '/tmp/myunique'. The default is '*na'.
        iccsid : str, optional
            XMLSERVICE EBCDIC CCSID (0 = default jobccsid). The default is 0.
        pccsid : str, optional
            XMLSERVICE ASCII CCSID. The default is 1208.

        Raises
        ------
        ValueError
            On incorrect iccsid or pccsid.

        Returns
        -------
        None.

        """
        warnings.warn(
            "iLibCall is deprecated, " "use itoolkit.transport.DirectTransport instead",
            category=DeprecationWarning,
            stacklevel=2,
        )

        if iccsid != 0:
            raise ValueError("iccsid must be 0 (job ccsid)")

        if pccsid != 1208:
            raise ValueError("pccsid must be 1208 (UTF-8)")

        super().__init__(ctl=ictl, ipc=ipc)

    def call(self, itool) -> str:
        """
        Call XMLSERVICE with accumulated actions.

        Parameters
        ----------
        itool : TYPE
            An iToolkit object.

        Returns
        -------
        str
            The XML returned from XMLSERVICE.

        """
        return super().call(itool)
