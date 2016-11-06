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

    Example file.
    Random generate different User-Agent of sorts of browser.
    Written in Python 3.5.

"""
import UAGenerater as uag

# single ua
print(uag.uasingle())

# listed 1000 ua save in a flie
f = open('user-agent.txt', 'w+')
f.write(str(uag.ualist(1000)))
f.close()
