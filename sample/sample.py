#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import sys
import time
sys.path.append("..")
from Channel import *

channel_id = 'your_channel_id' #android
msg = '{"title":"Message from Push","description":"hello world"}'
#msg_ios = '{"aps":{"alert":"iOS Message from Push","sound":"","badge":1},"key1":"value1","key2":"value2"}'
opts = {'msg_type':1, 'expires':300} 

c = Channel()

try:
    ret = c.pushMsgToSingleDevice(channel_id, msg, opts)
    print('ret: ', end=' ')
    print(ret)
    print(c.getRequestId())
except ChannelException as e:
    print('[code]', end=' ')
    print(e.getLastErrorCode())
    print('[msg]', end=' ')
    print(e.getLastErrorMsg())
    print('[request id]', end=' ')
    print(c.getRequestId())

try:
    ret = c.pushMsgToAll(msg, opts)
    print('ret: ', end=' ')
    print(ret)
    print(c.getRequestId())
except ChannelException as e:
    print('[code]', end=' ')
    print(e.getLastErrorCode())
    print('[msg]', end=' ')
    print(e.getLastErrorMsg())
    print('[request id]', end=' ')
    print(c.getRequestId())

try:
    ret = c.pushMsgToTag('test_tag', msg, 1, opts)
    print('ret: ', end=' ')
    print(ret)
    print('[request id]', end=' ')
    print(c.getRequestId())
except ChannelException as e:
    print('[code]', end=' ')
    print(e.getLastErrorCode())
    print('[msg]', end=' ')
    print(e.getLastErrorMsg())
    print('[request id]', end=' ')
    print(c.getRequestId())
