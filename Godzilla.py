# -*- coding: utf-8 -*-
# @Author  : Alphabug
# @Time    : 2021/11/12 16:50
# @PRODUCT : PyCharm
# @Function: Godzilla.py
# @Email   : alphabug@redteam.site
# 哥斯拉解密脚本 Java
import urllib
from Crypto.Cipher import AES
import base64,zlib,argparse
def decode(data,key):
    cipher = AES.new(key)
    data = base64.b64decode(data)
    return cipher.decrypt(data)
def ungzip(in_str):
    s = zlib.decompress(in_str, 16 + zlib.MAX_WBITS).decode()
    print("Decode:\n", s)
    return s
if __name__ == '__main__':
    alphabug = argparse.ArgumentParser(description="Godzilla Jsp Decoder,\tAuthor:Alphabug@RedTeam.site")
    alphabug.add_argument("-k","--key",help="Domain,For example: -k 3c6e0b8a9c15224a (Default:3c6e0b8a9c15224a)",default="3c6e0b8a9c15224a")
    alphabug.add_argument("-m","--mode",help="Email ,For example: -m post -d post_data | -m data -d return_data (Default:return_data)",default="return_data")
    alphabug.add_argument("-d","--data",help="Email ,For example: -m post -d 0mQU%2BS1pFnTz3ttVTnAgJf4rvU9E3tQySxwinpW%2F0fDyiB6qieU72U9P3PIb3i45CpP2Y9BsSVqc%2FVY2umWLyBCh%2F%2FphkKaNbf7RCjD4mzY%3D \n-m data -d 38F3ABE85948D564vfBIMcn2xlCZeTt3xKajRhv1UfDC5+KidKVHQV0TYeGnxL/CeXkYbegPI6tkcWYJnH10tRkuF/r0Z57m6xDziNeUjCtB8WEpN7K8wpQZmbwQvzA4JYKxQLfwVcZK6wO0U3oV1/JtcS+gBy7sFYq64K8hIoJZKXvF73ZSdcTNTNvGcnfeW7CWHuhQanjKoEVdescpdva1QVbxxLAiLTvjgquWISTy9ycQCqpi8DTgHRo=D7028F042ACDF2CA",required = True)
    args = alphabug.parse_args()

    key = args.key
    data = args.data
    mode = args.mode
    if mode == "return_data":
        data = data[16:-16]
    else:
        data = urllib.parse.unquote(data)
    # key = "3c6e0b8a9c15224a"
    # data = "38F3ABE85948D564vfBIMcn2xlCZeTt3xKajRhv1UfDC5+KidKVHQV0TYeGnxL/CeXkYbegPI6tkcWYJnH10tRkuF/r0Z57m6xDziNeUjCtB8WEpN7K8wpQZmbwQvzA4JYKxQLfwVcZK6wO0U3oV1/JtcS+gBy7sFYq64K8hIoJZKXvF73ZSdcTNTNvGcnfeW7CWHuhQanjKoEVdescpdva1QVbxxLAiLTvjgquWISTy9ycQCqpi8DTgHRo=D7028F042ACDF2CA"
    # data = "38F3ABE85948D5642EI9uUNhrXG14tB3MJ6cz5wDwxyVfNfqlqB2Xo8gXdIgfUf994dyGZwz5BHLp9nescU6LKj3qwWlxR8pGeQK5xP3g/LpRCCQ8nQRoblG2rmfxqhuPywgujqfB+n+sJhFuIXITN/Eo3ZV0JFYH+9ti2iuuabIYPOaQS1umnLBgM4iXjHJk767WIgG68a2tF76pplxf70vZHF4m6/MC3gyYBqgfK++vzBG9vK1FVAJ5+yw5OZGq7qEhcuyZSJIANl82e4NoVOl2HlmICi9UZVo7f03I7VzSGTsLmhuGE4zTxRtwd7Xbg02NFOK1wBMKvzJ91sDQ87yPZejCgO5d0ucIw==D7028F042ACDF2CA"
    result = decode(data,key)
    ungzip(result)
