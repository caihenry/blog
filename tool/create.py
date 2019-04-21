# encoding=utf-8
#########################################################################
# file: create.py
# create a new post
#
# content:
#
#     title: 文章标题
#     id: p2
#     date: 2018-10-27 00:36:22
#     updated: 2018-10-27 00:36:22
#     categories: 散文
#     tags: 感悟
#     keywords:
#     description: 内容简介
#     permalink:
#     ---
#       正文
#########################################################################
import sys
import os
import time


def get_dir_file_count(path):
    return sum([len(files) for _, _, files in os.walk(path)])



if __name__ == '__main__':
    if len(sys.argv) > 1:
        title = sys.argv[1]
        post_dir = os.path.join(os.path.split(os.path.abspath(__file__))[0], '../source/_posts')
        now_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        content = '''title: 文章标题
id: p{}
date: {}
updated: {}
categories: 散文
tags: 感悟
keywords:
description: 内容简介
permalink:
---
  正文'''.format(get_dir_file_count(post_dir) + 1, now_str, now_str)
        new_post = os.path.join(post_dir, '{}.md'.format(title))
        with open(new_post, 'w') as f:
            f.write(content)
    else:
        print 'usage: python create.py <title>'

