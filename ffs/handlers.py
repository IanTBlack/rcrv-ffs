import io
import logging
import socket
import time

class UDP():
    def __init__(self, ip: str, port: int) -> None:
        self.ip = str(ip)
        self.port = int(port)
        self._setup_message_stream()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def _setup_message_stream(self):
        datetime_format = '%Y-%m-%dT%H:%M:%S'
        message_format = '%(asctime)s.%(msecs)03dZ | %(name)-15s | %(levelname)-8s | %(message)s'
        fmt = logging.Formatter(message_format, datefmt=datetime_format)
        fmt.converter = time.gmtime
        self.log = logging.getLogger(self.ip)
        self.log.setLevel(logging.DEBUG)
        self.log_stream = io.StringIO()
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        stream = logging.StreamHandler(self.log_stream)
        stream.setFormatter(fmt)
        console.setFormatter(fmt)
        self.log.addHandler(stream)
        self.log.addHandler(console)


    def send_info(self,message):
        self.log.info(message)
        self.log_stream.truncate(0)
        self.log_stream.seek(0)
        self._socket.sendto(bytes(self.log_stream.getvalue(),'utf-8'),(self.ip, self.port))


    def send_debug(self,message):
        self.log.debug(message)
        self.log_stream.truncate(0)
        self.log_stream.seek(0)
        self._socket.sendto(bytes(self.log_stream.getvalue(), 'utf-8'), (self.ip, self.port))


    def send_warning(self,message):
        self.log.warning(message)
        self.log_stream.truncate(0)
        self.log_stream.seek(0)
        self._socket.sendto(bytes(self.log_stream.getvalue(), 'utf-8'), (self.ip, self.port))


    def send_critical(self,message):
        self.log.critical(message)
        self.log_stream.truncate(0)
        self.log_stream.seek(0)
        self._socket.sendto(bytes(self.log_stream.getvalue(), 'utf-8'), (self.ip, self.port))
