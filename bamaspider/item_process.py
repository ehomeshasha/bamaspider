# -*- coding: utf-8 -*-

import types


def process_item(item, key):
    value = setEmptyIfnotExist(item, key)
    value = convertNum2Str(value)
    value = addslashes(value)
    return value

def setEmptyIfnotExist(item, key):
    if key not in item:
        item[key] = ""
    return item[key]

def convertNum2Str(value):
    if type(value) is types.IntType:
        value = str(value)
    elif type(value) is types.LongType:
        value = str(value)
    elif type(value) is types.FloatType:
        value = str(value)
    return value


# def addslashes(s):
#     l = ["\\", '"', "'", "\0", ]
#     for i in l:
#         if i in s:
#             s = s.replace(i, '\\'+i)
#     return s
def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)