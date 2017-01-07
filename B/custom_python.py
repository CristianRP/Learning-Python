#!/usr/bin/env python3
# -*- coding:utf8 -*-

sentinel = '' # ends when this string is seen
lines = '\n'.join(iter(input, sentinel))

print(lines.split("\n"))