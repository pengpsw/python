#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

t = '19:05:30'
print('Test:', t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

def is_valid_email(addr):
    return  re.match(r'^[\w\.]+\@\w+\.\w{3}$',addr)

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')



def name_of_email2(addr):
    m=re.match(r'^<?(\w+\s?\w+)?>?(\s?\w+)?\@(\w+\.\w{3})$',addr)
    print(m.group(1))
    return m.group(1)

    # 测试:
assert name_of_email2('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email2('tom@voyager.org') == 'tom'
print('ok')