#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :Copyright (c) 2016 By Zhenglong Wu.
    :license: Mozilla Public License, v. 2.0.
    :@anchor: Zhenglong Wu <itdevwu6@gmail.com>.

    This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
    If a copy of the MPL was not distributed with this file.
    You can obtain one at http://mozilla.org/MPL/2.0/.

    ----------
    A Fast User Agent Generater in Python.
    Random generate different User Agents of sorts of browsers.
    Written in Python 3.5.

"""
import random


def uasingle():
    Mozilla_ver = 'Mozilla' + str(random.choice(['/4.0 ', '/5.0 ']))
    # system_PC = random.choice(['Windows','Windows NT 6.1','Windows NT 6.0','Windows NT 10.0' 'Macintosh', 'compatible'])
    # system_MOBILE = random.choice(['BlackBerry', 'compatible', 'iPhone', 'iPad'])
    instruction_set = random.choice(['x64', 'x86'])
    Platform = random.choice(['Windows','Windows NT 6.1','Windows NT 6.0','Windows NT 10.0' 'Macintosh', 'compatible'])
    language = random.choice(['en-US', 'zh-tw', 'ja-jp', 'zh-CN', 'sv-SE', 'pt-PT', 'bn-BD', 'de', 'es', 'fr', 'ca', 'cs'])
    Chrome_ver = 'Chrome/' + str(random.randint(14, 54)) + '.' + str(random.randint(200,5000)) + '.' + str(random.randint(1,199))
    Safari_ver = 'Safari/' + str(random.randint(419, 602))
    # Firefox_ver =
    WebKit_ver = ' AppleWebKit/' + str(random.randint(530, 602)) +' (KHTML, like Gecko) '
    version = WebKit_ver + random.choice([Chrome_ver, Safari_ver])
    uagent = str(Mozilla_ver + '(%s; U; %s; %s)' + version) % (Platform, instruction_set, language)
    return uagent

def ualist(num=2):
    counter = 0
    ua_list = []
    while counter < num:
        ua_list.append(uasingle())
        counter = counter + 1
    return ua_list
