import threading
import logging
import requests
import datetime
import os

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':
    daftar_gambar = [
        'https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
        'https://www.pngfind.com/pngs/m/422-4223072_this-free-icons-png-design-of-rose-17.png',
        'http://pngimg.com/uploads/rose/rose_PNG67024.png'
        
    ]
    
threads = []
for i in daftar_gambar:
    t = threading.Thread(target=download_gambar,args=(i,))
    threads.append(t)
    t.start()
