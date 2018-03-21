from urllib.request import urlopen
from time import sleep,strftime,localtime
from json import loads
from os import path,walk,remove
from PIL import Image

img_path='D:/Documents/BingWallpaper/'

def ClearImage():
    for root, dirs, files in walk(img_path):
        for name in files:
            if name.endswith('.jpg'):
                remove(img_path+name)
                    
def GetWallpaper():
    times=0
    for times in range(10):
        try:
            img_json=urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=-1&n=1&mkt=zh-cn')
            break
        except Exception:
            sleep(10)
    img_json=loads(img_json.read())
    img_url='https://www.bing.com'+img_json["images"][0]["url"]
    img_date=img_json["images"][0]["startdate"]
    while not path.exists(img_path+img_date+'.jpg') and times<30:
        try:
            img=urlopen(img_url).read()
            with open(img_path+img_date+'.jpg','wb') as f:
                f.write(img)
        except Exception:
            times+=1
            sleep(10)
    bmp_img=Image.open(img_path+img_date+'.jpg')
    bmp_img.save(img_path+'Wallpaper.bmp',"BMP")

if __name__=="__main__":
    if not path.exists(img_path+strftime("%Y%m%d",localtime())+'.jpg'):
        ClearImage()
        GetWallpaper()
