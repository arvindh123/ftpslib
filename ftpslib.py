import ssl, socket , ftplib
class ftps_implicit(ftplib.FTP_TLS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sock = None
    @property
    def sock(self):
        return self._sock
    @sock.setter
    def sock(self, value):
        if value is not None and not isinstance(value, ssl.SSLSocket):
            value = self.context.wrap_socket(value)
        self._sock = value
    def CustStorBinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
        self.voidcmd('TYPE I')
        with self.transfercmd(cmd, rest) as conn:
            while 1:
                buf = fp.read(blocksize)
                if not buf:
                    break
                conn.sendall(buf)
                if callback:
                    callback(buf)
            # shutdown ssl layer
            
            # if _SSLSocket is not None and isinstance(conn, _SSLSocket):
            #     # conn.unwrap()
            #     pass
           
        return self.voidresp()

# ftp_client = ftps_implicit()
# ftp_client.connect(host='ftp.example.com ', port=990)
# ftp_client.login(user='username', passwd='password')
# ftp_client.prot_p()
# print(ftp_client.pwd())
