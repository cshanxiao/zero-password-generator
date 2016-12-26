# -*- coding: utf8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2016年12月26日
'''

class Binutil(object):

    def __init__(self):
        pass
    
    def to_bytes(self, text):
        ur'''
        :summary: 从起始位置，每两个字母间插入'\x'
        '''
        text = text.replace(" ", "").replace("\t", "").strip()
        if len(text) % 2 != 0:
            return text
        items = []
        for i in range(len(text)):            
            if i % 2 == 0 and i != 0:
                continue
            items.append(text[i-1: i+1])
        return "\\x".join(items) 
    
    def _parse_head(self, data):
        pass
    
    def decode_cmd(self, data):
        "00000003  12  00  0090  01  0100000000000064000000000000"
        
        

if __name__ == "__main__":
    util = Binutil()
    print util.to_bytes("00000003  12  00  0090  01  0100000000000064000000000000")
    
    
    