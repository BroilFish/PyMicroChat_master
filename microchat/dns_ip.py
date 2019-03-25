'''访问'http://dns.weixin.qq.com/cgi-bin/micromsg-bin/newgetdns',
获取长ip/短ip地址.
'''

import requests
from bs4 import BeautifulSoup
from random import choice

# 登录返回-301自动切换DNS
dns_retry_times = 3

# 短链接ip池
short_ip = []

# 长链接ip池
long_ip = []

def get_ips():
    '''访问'http://dns.weixin.qq.com/cgi-bin/micromsg-bin/newgetdns',
    返回短链接ip列表short_ip，长链接ip列表long_ip.
    '''

    ret = requests.get(
        'http://dns.weixin.qq.com/cgi-bin/micromsg-bin/newgetdns')
    soup = BeautifulSoup(ret.text, "html.parser")
    short_weixin = soup.find(
        'domain', attrs={'name': 'short.weixin.qq.com'})
    [short_ip.append(ip.get_text()) for ip in short_weixin.select('ip')]
    long_weixin = soup.find(
        'domain', attrs={'name': 'long.weixin.qq.com'})
    [long_ip.append(ip.get_text()) for ip in long_weixin.select('ip')]
    
    return short_ip, long_ip

# 随机取出一个长链接ip地址
def fetch_longlink_ip():
    if not long_ip:
        get_ips()  
    return choice(long_ip)

# 随机取出一个短链接ip地址
def fetch_shortlink_ip():
    if not short_ip:
        get_ips()   
    return choice(short_ip)