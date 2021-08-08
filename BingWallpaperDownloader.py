
import requests
import random
import json
import os
import time
from datetime import datetime, timedelta

def GetRequestContent(address,payload=""):
    headers = requests.utils.default_headers()
    headers.update(
    {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    })
    r = requests.get(address,headers=headers,params=payload)
    return r.content

def DownloadPic(address,name):
    content = GetRequestContent(address)
    with open(name, "wb") as f:
        f.write(content)
        print("image download successful, saved in: "+name)
        return True

# api ref： https://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
# https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1 ,获取当天的bing壁纸

# bing page
base_url = "https://www.bing.com"
# bing pic get base url
base_pic_json_api = "https://www.bing.com/HPImageArchive.aspx"
# bing pic json api
today_pic_api = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

def GetBingBgUrl(params=[]):
    content = GetRequestContent(base_pic_json_api,payload=params)
    if len(content)!=0:
        decoded_contene = content.decode()
        json_data = json.loads(decoded_contene)
        url = base_url+json_data["images"][0]["url"]
        print("image url = ",url)
        return url
    return ""

mkt_list = ["zh-CN","en-US", "ja-JP", "en-AU", "en-UK", "de-DE", "en-NZ", "en-CA"]

# index is the bing image index from today , 1 is tomorrow, 2 for today-1 ...
def DownLoadBingImg(path,index=0):
    bing_pic_date = datetime.today() - timedelta(days = index )
    bing_pic_date = bing_pic_date.strftime("%Y_%m_%d")
    print(bing_pic_date)
    # all mkt is same pic
    # just get china 
    payload = {'format': 'js', 'idx': index,'n':1,'mkt':mkt_list[0]}
    bing_img_url = GetBingBgUrl(payload)
    # get bing image
    DownloadPic(bing_img_url,path+bing_pic_date+".jpg")
    
# download all 8 day bing wallpaper

def DownloadAllDayBingImg(path):
    count = 7
    while count >=0:
        DownLoadBingImg(path,count)
        count = count - 1

def main():
    print(os.listdir("./"))
    if not "bing_bg" in os.listdir("./"):
        os.makedirs("./bing_bg/")
    DownloadAllDayBingImg("./bing_bg")
if __name__ == "__main__":
    main()