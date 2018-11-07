import urllib.request
import time


class Assertions(object):

    @staticmethod
    def assert_url_open(url):
        opener = urllib.request.build_opener()
        # opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
        try:
            response = opener.open(url)
            status_code = response.status_code
            assert 200 <= status_code < 300
            print(url + '没问题')
        except urllib.error.HTTPError:
            print(url + ' HTTPError')
            time.sleep(1)
        except urllib.error.URLError:
            print(url + ' URLError')
            time.sleep(1)
            raise
        time.sleep(0.1)
