#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest
from utils.environment import Environment
from utils.shell import Shell
from utils.log import Log

"""
run all case:
    python3 run.py

run one module case:
    python3 run.py test/test_home.py

run case with key word:
    python3 run.py -k <keyword>

"""

if __name__ == '__main__':
    env = Environment()
    xml_report_path = env.get_environment_info().xml_report
    html_report_path = env.get_environment_info().html_report
    # 开始测试
    args = ['-s', '-q', '--alluredir', xml_report_path]
    self_args = sys.argv[1:]
    pytest.main(args + self_args)
    # 生成html测试报告
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)
    try:
        Shell.invoke(cmd)
        Log.e("Html测试报告生成成功")
    except Exception as e:
        Log.e("Html测试报告生成失败,确保已经安装了Allure-Commandline % s" % e)
