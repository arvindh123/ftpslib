import ssl, socket , ftplib
class ftps_implicit(ftplib.FTP_TLS):
    """FTP_TLS subclass that automatically wraps sockets in SSL to support implicit FTPS."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sock = None

    @property
    def sock(self):
        """Return the socket."""
        return self._sock

    @sock.setter
    def sock(self, value):
        """When modifying the socket, ensure that it is ssl wrapped."""
        if value is not None and not isinstance(value, ssl.SSLSocket):
            value = self.context.wrap_socket(value)
        self._sock = value

# ftp_client = ftps_implicit()
# ftp_client.connect(host='ftp.example.com ', port=990)
# ftp_client.login(user='username', passwd='password')
# ftp_client.prot_p()
# print(ftp_client.pwd())
