# -*- coding: utf-8 -*-
"""
Base classes for transports
"""

from .errors import TransportClosedError
from ..toolkit import iToolKit


class XmlServiceTransport:
    """XMLSERVICE transport base class"""

    def __init__(self, ctl: str = "*here *cdata", ipc: str = "*na"):
        """

        Parameters
        ----------
        ctl : str, optional
            XMLSERVICE control options, see
              http://yips.idevcloud.com/wiki/index.php/XMLService/XMLSERVICEQuick#ctl .
              The default is "*here *cdata".
        ipc : str, optional
            An XMLSERVICE ipc key for stateful conections, see
              http://yips.idevcloud.com/wiki/index.php/XMLService/XMLSERVICEConnect
              The default is "*na".

        Returns
        -------
        None.

        """
        self.ipc = ipc
        self.ctl = ctl

        self.trace_attrs = ["ipc", "ctl"]
        self._is_open = True

    def __del__(self):
        self.close()

    def trace_data(self) -> str:
        """
        Return formatted trace data

        Returns
        -------
        str
            trace data.

        """
        output = ""

        for i in self.trace_attrs:
            if isinstance(i, tuple):
                trace, attr = i
            else:
                trace = attr = i
            output += " {}({})".format(  # pylint: disable-msg=consider-using-f-string
                trace, getattr(self, attr)
            )

        return output

    def call(self, itool: iToolKit) -> str:
        """
        Call XMLSERVICE with accumulated actions.

        Attention:
          Subclasses should implement :py:func:`_call` to call XMLSERVICE
          instead of overriding this method.

        Parameters
        ----------
        itool : iToolKit
            An iToolkit object.

        Returns
        -------
        str
            The XML returned from XMLSERVICE.

        """
        self._ensure_open()

        return self._call(itool)

    def _call(self, itool: iToolKit):
        """Called by :py:func:`call`. This should be overridden by subclasses
        to the call function instead of overriding :py:func:`call` directly.
        """
        raise NotImplementedError

    def _ensure_open(self):
        """This should be called by any subclass function which uses
        resources which may have been released when `close` is called."""
        if not self._is_open:
            raise TransportClosedError()

    def close(self):
        """Close the connection now rather than when :py:func:`__del__` is
        called.

        The transport will be unusable from this point forward and a
        :py:exc:`itoolkit.transport.TransportClosedError` exception will be
        raised if any operation is attempted with the transport.

        Attention:
          Subclasses should implement :py:func:`_close` to free its resources
          instead of overriding this method.
        """
        self._close()
        self._is_open = False

    def _close(self):
        """Called by `close`. This should be overridden by subclasses to close
        any resources specific to that implementation."""
        pass  # pylint: disable-msg=unnecessary-pass
