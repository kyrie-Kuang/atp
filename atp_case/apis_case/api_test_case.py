#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import unittest
import requests
import HTMLTestRunner
import time


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_api(self):
        sql = "SELECT api_name,api_url,api_method FROM web_apis WHERE api_name='test01'"
        # 建立数据库连接
        coon = pymysql.connect(
            user='root',
            password='123456',
            port=3306,
            host='127.0.0.1',
            db='atp'
        )

        cursor = coon.cursor()
        # 执行数据库操作
        exec = cursor.execute(sql)
        # 接收exec条返回结果行
        fm = cursor.fetchmany(exec)
        for i in fm:
            case_list = []
            case_list.append(i)
            api_case_list(case_list, self)

        coon.commit()
        cursor.close()
        coon.close()


def api_case_list(case_list, self):
    for case in case_list:
        try:
            case_id = case[0]
            case_url = case[1]
            case_method = case[2]
        except Exception as e:
            return 'error' % e

        if case_method == "get" and case_id == 1:
            res = requests.request('GET', case_url).json()
            self.assertEqual(res["error_code"], 0)
            self.assertEqual(res["stu_info"][1]['id'], 4083)


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S")

    test_unit = unittest.TestSuite()
    test_unit.addTest(ApiTestCase("test_api"))

    file_name = "F:\\atp_case\\api_case\\report\\" + now + "_api_report.html"

    fn = open(file_name, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fn,
        title=u'接口自动化测试报告',
        description=u'测试'
    )
    runner.run(test_unit)
