import http.client
import urllib.parse

# params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})


def partial_download(hostname, path):
    params = ''
    headers = {}
    conn = http.client.HTTPConnection(hostname)
    conn.request("HEAD", path, params, headers)

    response = conn.getresponse()
    print(response.status, response.reason, response.headers)
    conn.close()
    if response.getheader('Accept-Ranges') == "bytes":
        return True


def download(hostname, path):
    params = ''
    headers = {'Range': 'bytes=0-5'}
    conn = http.client.HTTPConnection(hostname)
    conn.request("GET", path, params, headers)

    response = conn.getresponse()
    print(response.status, response.reason, response.headers)
    data = response.read()
    print(response.getheader('Accept-Ranges:'))
    print(data)
    conn.close()


"""
Content-Type: image/jpeg
Content-Length: 290070
Last-Modified: Sun, 20 Nov 2016 11:26:07 GMT
Connection: keep-alive
ETag: "5831884f-46d16"
Accept-Ranges: bytes
"""

if __name__ == '__main__':
    hostname = "127.0.0.1:80"
    path = "/header.jpg"
    print(partial_download(hostname, path))
