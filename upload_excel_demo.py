# -*- coding: utf-8 -*-
import requests


def upload_excel():
    upload_url = 'http://10.4.24.93:10010/webapi/excel/brand/order/import'
    header = {
        'a': '1',
        'p': '1',
        'c': '-1',
        't': '1619677887708',
        's': 'r!@r#6#$r56##$6s$%',
        'loginUserId': '37',
        'v': '0.0.1',
        'loginToken': '2f2ad62e16ad4717a021416ed9943c21',

    }
    files = {'file': open('D:\\1.xlsx', 'rb')}
    upload_res = requests.post(upload_url, files=files, headers=header)
    print(upload_res.json())


if __name__ == '__main__':
    upload_excel()
