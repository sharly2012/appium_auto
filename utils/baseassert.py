#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import urllib.request
import time
from utils.logger import Logger

logger = Logger(logger="Assertions").get_log()


class Assertions(object):

    @staticmethod
    def assert_url_open(url):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
        try:
            opener.open(url)
            logger.info("The %s can be open" % url)
        except urllib.error.HTTPError as hte:
            logger.error("HTTPError %s" % hte)
            time.sleep(1)
        except urllib.error.URLError as ue:
            logger.error('URLError %s' % ue)
            time.sleep(1)
        time.sleep(0.1)


if __name__ == '__main__':
    aaa = Assertions()
    aaa.assert_url_open("https://www.baiwwdu.com")
