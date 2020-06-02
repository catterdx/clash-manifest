#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
 Author 雨落无声（Github: https://github.com/ylws-4617)
 Reference:
 1. https://www.s0nnet.com/archives/python-icmp
 2. http://www.pythoner.com/357.html
'''

import commands

def ping(host):
    cmd = "ping "+ str(host) + " -c2 -W 2"
    result = commands.getoutput(cmd)
    result = result.split()
    result = result[-2].split("/")[0]
    if result.isalpha():
        result = False
    return float(result)

STYLE = {
    'fore': {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
        'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37,
    },
    'back': {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
        'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47,
    },
    'mode': {
        'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7,
    },
    'default': {
        'end': 0,
    }
}


def use_style(string, mode='', fore='', back=''):
    mode = '%s' % STYLE['mode'][mode] if STYLE['mode'].has_key(mode) else ''
    fore = '%s' % STYLE['fore'][fore] if STYLE['fore'].has_key(fore) else ''
    back = '%s' % STYLE['back'][back] if STYLE['back'].has_key(back) else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)

D = {
    'Zhengzhou CM': '5ghenan.ha.chinamobile.com', 
    'Jinan CU': '202.102.152.3',
    'Tianjin CT': '219.150.32.132', 
    'Jinan CU': 'jnltwy.com', 
    'Xinjiang CM': 'speedtest1.xj.chinamobile.com',
    'Nanjin CM': 'owa.eastcom-sw.com',
    'Lhasa CM': 'speedtest1.xz.chinamobile.com', 
    'Changchun CM': '202.98.0.68',
    'Shenzhen CU': 'speedtest.75510010.com', 
    'Lanzhou CU': 'speedtest.bajianjun.com', 
    'Xining CU': '221.207.32.94', 
    'Hefei CU' : '112.122.10.26',
    'Wuhan CU': '113.57.249.2', 
    'Nanchang CM': 'speedtest.nc.jx.chinamobile.com', 
    'Chongqing': 'speedtest1.cqccn.com', 
    'Shanghai CT': 'speedtest1.online.sh.cn',
    'Huhehaote CT': '222.74.1.200',
    'Urumqi CU': '4g.xj169.com',
    'Hangzhou CT': '122.229.136.10',
    'Xi an CU': 'xatest.wo-xa.com', 
    'Ningbo CM': 'ltetest3.139site.com',
    'Taiyuan CM': 'testsx.njgean.com', 
    'Nanjin CT': '4gsuzhou1.speedtest.jsinfo.net', 
    'Changsha CT': 'mygod998.vicp.net',
    'Beijing CT': 'st1.bjtelecom.net',
    'Chengdu CT': 'speed.westidc.com.cn', 
    'Shenyang CM': 'speedtest1.ln.chinamobile.com',
    'Ningxia CU': '221.199.9.35',
    'Fuzhou CU': 'upload1.testspeed.kaopuyun.com'
    }

string =list()
d=dict()

for x in D:
    host=D[x]
    result = ping(host)


    if result == False:
        latency_str = use_style(str("Fail"), fore='red')
    elif float(result) <= 60:
        latency_str =use_style(str(round(result,2)) + " ms",fore='green')
    elif float(result) <= 130:
        latency_str = use_style(str(round(result,2))+" ms",fore='yellow')
    else:
        latency_str = use_style(str(round(result,2))+" ms", fore='red')

    d[x] = float(result)

    string.append((x,latency_str))
    if len(string) == 3:
        print("{0:12}: {1:20}{2:12}: {3:20}{4:12}: {5:20}".format(string[0][0],string[0][1],string[1][0],string[1][1],string[2][0],string[2][1]))
        string = list()


if len(string) == 2:
    print("{0:12}: {1:20}{2:12}: {3:20}".format(string[0][0],string[0][1],string[1][0],string[1][1]))

if len(string) == 1:
    print("{0:12}: {1:20}".format(string[0][0],string[0][1]))
