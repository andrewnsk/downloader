from mock import patch, Mock, mock_open
import unittest
from downloader.sdow import get_file_size, download_file, resume_download_file, proc
import builtins


def mock_get(data):
    """Mock of requests.get. The object returned must have headers and iter_content properties."""
    response = Mock()

    def iter_content(chunk_size=1):
        """Mocking requests.get().iter_content."""
        rest = data
        while rest:
            chunk = rest[:chunk_size]
            rest = rest[chunk_size:]
            yield chunk

    response.headers = {'content-length': str(len(data)), 'Status': '200 OK', 'content-type': 'octet/stream'}
    response.iter_content = iter_content
    response.status_code = 200
    return response


class TestDownloader(unittest.TestCase):
    DATA = bytearray(range(128))

    @patch('requests.head', return_value=Mock(headers={'content-length': 4096, 'Status': '200 OK',
                                                       'content-type': 'application/json'},
                                              status_code=200))
    def test_get_file_size(self, *args):
        """call mocked function """
        self.assertEqual(get_file_size('mock.url'), 4096)

    @patch('requests.get', return_value=mock_get(DATA))
    @patch('builtins.open')
    def test_download_file(self, *args):
        """call mocked function """
        download_file('url', 'file')

    @patch('requests.get', return_value=mock_get(DATA))
    @patch('builtins.open')
    def test_resume_download_file(self, *args):
        """call mocked function """
        resume_download_file('mock.url', 'mock.file', '123-256', 500)

if __name__ == '__main__':
    unittest.main()
