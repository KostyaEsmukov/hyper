# -*- coding: utf-8 -*-
"""
hyper/common/exceptions
~~~~~~~~~~~~~~~~~~~~~~~

Contains hyper's exceptions.
"""


class ChunkedDecodeError(Exception):
    """
    An error was encountered while decoding a chunked response.
    """
    pass


class InvalidResponseError(Exception):
    """
    A problem was found with the response that makes it invalid.
    """
    pass


class SocketError(IOError):
    """
    An error occurred during socket operation.
    """
    pass


class LineTooLongError(Exception):
    """
    An attempt to read a line from a socket failed because no newline was
    found.
    """
    pass


# Create our own ConnectionResetError.
try:  # pragma: no cover
    # Python 3
    ConnectionResetError = ConnectionResetError
except NameError:  # pragma: no cover
    # Python 2
    class ConnectionResetError(IOError):
        """
        A HTTP connection was unexpectedly reset.
        """


class TLSUpgrade(Exception):
    """
    We upgraded to a new protocol in the NPN/ALPN handshake.
    """
    def __init__(self, negotiated, sock):
        super(TLSUpgrade, self).__init__()
        self.negotiated = negotiated
        self.sock = sock


class HTTPUpgrade(Exception):
    """
    We upgraded to a new protocol via the HTTP Upgrade response.
    """
    def __init__(self, negotiated, sock):
        super(HTTPUpgrade, self).__init__()
        self.negotiated = negotiated
        self.sock = sock


class MissingCertFile(Exception):
    """
    The certificate file could not be found.
    """
    pass


# Create our own ConnectionError.
try:  # pragma: no cover
    ConnectionError = ConnectionError
except NameError:  # pragma: no cover
    class ConnectionError(IOError):
        """
        An error occurred during connection to a host.
        """


class ProxyError(ConnectionError):
    """
    An error occurred during connection to a proxy.
    """
    pass
