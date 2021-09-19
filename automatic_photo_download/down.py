import urllib.request
from PIL import Image

def download_image(url):
    for i in range(1,18):
        file_name = 'image'+str(i)+'.png'
        urllib.request.urlretrieve(url+str(i)+".png", file_name)

download_image("http://contents.hufs.ac.kr/contents/univ/Y61614/2016/031/slidebook/pages/")

imglist = []
img1 = Image.open(r'C:\Users\choi\Desktop\goni\image1.png')
imgcon1 = img1.convert('RGB')
for i in range(2,18):
    img = Image.open(r'C:\Users\choi\Desktop\goni\image'+str(i)+'.png')
    imgcon = img.convert('RGB')
    imglist.append(imgcon)
imgcon1.save(r'C:\Users\choi\Desktop\goni\bio.pdf', save_all=True, append_images=imglist)
