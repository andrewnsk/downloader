import http.client
import urllib.parse
import httplib2
import sys

# params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


def connect(hostname, path='/', params='', headers={'Connection': 'keep-alive'}):
    conn = http.client.HTTPConnection(hostname)
    conn.request("HEAD", path, params, headers)
    response = conn.getresponse()
    return response


def get_length(response):
    length = response.getheader('Content-Length')
    return int(length)


def is_accept_ranges(response):
    if response.getheader('Accept-Ranges') == "bytes":
        return True


def download(hostname, path):
    if not is_accept_ranges(hostname, path):
        sys.exit(1)
    params = ''
    headers = {'Range': 'bytes=0-5'}
    conn = http.client.HTTPConnection(hostname)
    conn.request("GET", path, params, headers)

    response = conn.getresponse()
    print(response.status, response.reason, response.headers)
    data = response.read()
    print(response.getheader('Accept-Ranges:'))
    print(data)


def close(connection):
    connection.close()


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
    localhost = connect(hostname, path)
    length = get_length(localhost)
    if is_accept_ranges(localhost):
        print('Accept-Ranges OK,', 'filesize:', length)
        sys.exit(0)

    else:
        print('host does not support multiple threads')
        sys.exit(1)
