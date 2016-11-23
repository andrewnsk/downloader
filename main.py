import requests
from tqdm import tqdm
import os.path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("url", help="url for file", type=str)
args = parser.parse_args()
url = args.url
local_filename = url.split('/')[-1]


def get_file_size(url):

    r = requests.head(url)
    if r.status_code == requests.codes.ok:
        return r.headers['content-length']


def download_file(url, local_filename):

    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        print(r.headers['content-type'], r.status_code, end='\n')
        if r.headers['content-length']:
            if int(r.headers['content-length']) > 1023:
                total_size = int(int(r.headers['content-length']) / 1024)
            else:
                total_size = int(r.headers['content-length'])

    with open(local_filename, 'wb') as f:
        # for chunk in r.iter_content(chunk_size=1024):
        for chunk in tqdm(r.iter_content(chunk_size=1024),
                          total=total_size,
                          unit=' Kb',
                          bar_format='{l_bar}{bar}{r_bar}',
                          miniters=10):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    f.close()
    return True


def resume_download_file(url, local_filename, bytes_range, estimate_size):
    headers = {'Range': 'bytes={0}'.format(bytes_range)}
    r = requests.get(url, stream=True, headers=headers)
    print('resume downloading')
    with open(local_filename, 'ab') as f:
        # for chunk in r.iter_content(chunk_size=1024):
        for chunk in tqdm(r.iter_content(chunk_size=1024),
                          total=estimate_size,
                          unit=' Kb',
                          bar_format='{l_bar}{bar}{r_bar}'):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    f.close()
    return True

if __name__ == '__main__':

    if os.path.exists(local_filename):
        print('file exist')
        local_file_size = os.path.getsize(local_filename)
        remote_file_size = int(get_file_size(url))
        print('Local size:', local_file_size)
        print('Remote size:', remote_file_size)
        estimate_size = round((remote_file_size - local_file_size) / 1024)
        if local_file_size >= remote_file_size:
            print('Nothing to do')
            sys.exit(1)
        bytes_range = '{0}-{1}'.format(local_file_size, remote_file_size)
        print('Range in:', bytes_range)
        resume_download_file(url, local_filename, bytes_range, estimate_size)
    else:
        download_file(url, local_filename)





