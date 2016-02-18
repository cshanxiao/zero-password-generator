# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 2016年2月17日
'''

import string
import random

class PasswordGenerator():
    def __init__(self):
        pass

    def _generate(self, random_chars, length):
        pwd = ""
        for _i in xrange(length):
            pwd += random.choice(random_chars)
        return pwd

    def generate_normal_password(self, digits=None, lowercase=None, uppercase=None,
                                 punctuation=None, length=8, count=1):
        random_chars = set()
        if digits:
            random_chars.update([char for char in string.digits])
        if lowercase:
            random_chars.update([char for char in string.lowercase])
        if uppercase:
            random_chars.update([char for char in string.uppercase])
        if punctuation:
            random_chars.update([char for char in string.punctuation])
        if not random_chars:
            random_chars.update([char for char in string.digits])

        return [self._generate(list(random_chars), length) for _i in xrange(count)]

    def generate_custom_password(self, custom_chars=None, custom_random_chars=None,
                                 length=8, count=1):
        if not custom_random_chars or not isinstance(custom_random_chars, list):
            custom_random_chars = [char for char in string.digits]
        pwds = []
        for _i in xrange(count):
            pwd = self._generate(custom_random_chars, length)
            if custom_chars and isinstance(custom_chars, dict):
                pwd = list(pwd)
                for position, char in custom_chars.items():
                    if position < 1 or position > length:
                        continue
                    pwd[position - 1] = str(char)[0]
                pwd = "".join(pwd)
            pwds.append(pwd)
        return pwds

