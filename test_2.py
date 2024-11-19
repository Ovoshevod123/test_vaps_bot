import ssl
from python_socks.sync import Proxy

proxy = Proxy.from_url('socks5://192.252.208.70:14282')
print(1)
sock = proxy.connect(dest_host='check-host.net', dest_port=443)
print(2)
sock = ssl.create_default_context().wrap_socket(
 sock=sock,
 server_hostname='check-host.net'
)
print(3)
request = (
 b'GET /ip HTTP/1.1\r\n'
    b'Host: check-host.net\r\n'
    b'Connection: close\r\n\r\n'
)
print(4)
sock.sendall(request)
response = sock.recv(4096)
print(response)