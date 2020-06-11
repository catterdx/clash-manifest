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
	'Xinjiang CT': '202.100.178.81',
	'Heilongjiang CU': '202.97.224.69',
	'Neimenggu CT': '222.74.1.200',
	'Jilin CM': '202.98.0.68',
	'Lhasa CM': 'speedtest1.xz.chinamobile.com', 
	'Urumqi CU': '4g.xj169.com',
	'Liaoning CT': '219.149.9.153',
	'Shandong CU': '202.102.152.3',
	'Beijing CT': 'st1.bjtelecom.net',
	'Hebei CT': '123.183.181.249',
	'Tianjin CT': '219.150.32.132', 
	'Gansu CT': '60.165.114.173',
	'Gansu CU': 'speedtest.bajianjun.com',
	'Shanxi CT': '219.149.145.21',
	'Xi an CU': 'xatest.wo-xa.com', 					
	'Ningxia CU': '221.199.9.35',
	'Qinhai CU': '221.207.32.94', 
	'Hefei CU' : '112.122.10.26',
	'Henan CM': '221.183.53.249',
	'Jiangsu CM': 'owa.eastcom-sw.com',
	'Jiangsu CT': '4gsuzhou1.speedtest.jsinfo.net',
	'Jinagxi CM': 'speedtest.nc.jx.chinamobile.com',
	'Zhejiang CT': '122.229.136.10',
	'Zhejiang CM': 'ltetest3.139site.com',
	'Hubei CU': '113.57.249.2',
	'Hunan CM': 'speedtest02.hn165.com',
	'Sichuan CT': '118.123.217.145', 
	'Fuzhou CU': 'upload1.testspeed.kaopuyun.com',
	'Shanghai CT': 'speedtest1.online.sh.cn', 
	'Shanghai CU': '5g.shunicomtest.com', 
	'Guangzhou CT': '114.67.22.1',
	'Guangdong CM': '120.237.53.17', 
	'Shenzhen CU': 'speedtest.75510010.com',
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
