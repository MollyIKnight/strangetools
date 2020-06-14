from bilibili_api import video, Verify
import re
url=input('url: ')
#url='https://www.bilibili.com/video/BV1s64y1u7x6?from=search&seid=429942290358386679'

try:
    bvid = re.findall('/video/(BV[0-9a-zA-Z]+)',url)
    print(bvid)
except:
    print('did not find bvid')

'''my_video = video.VideoInfo(bvid)
video_info = my_video.get_video_info()
print(video_info)'''

bvid=bvid[0]


def bv2aid(bv: str):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608

    def dec(x):
        r = 0
        print(x)
        for i in range(6):
            r += tr[x[s[i]]] * 58 ** i
        return (r - add) ^ xor

    return dec(bv)

avid = bv2aid(bvid)
dll = 'https://bilibili.com/video/av'+str(avid)
#choose part: append: ?p=[2]
'''
print(dll)
thisvideo=video.VideoInfo(bvid)
#video_info=thisvideo.get_video_info()
#print(video_info)
dllurl = thisvideo.get_playurl(2)
f=open('f.txt','w')
f.write(dllurl)
f.close()'''