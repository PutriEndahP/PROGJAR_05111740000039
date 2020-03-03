import threading
import logging
import requests
import datetime
import os

def worker(nomor):
    waktu = datetime.datetime.now()
    logging.warning(f"saya worker nomor {nomor}")
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()


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
    download_gambar('https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg')
    download_gambar('https://cdn0-production-images-kly.akamaized.net/i7MJAqQ8-ZM9-BkSO5cAZCfyJpE=/0x0:1197x1596/640x853/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/2971440/original/004271000_1574142781-Disney_Frozen_II_Poster.jpg')
    

