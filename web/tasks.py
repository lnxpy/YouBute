from youbute.celery import app
from pytube import YouTube
import requests
from youbute.settings import MEDIA_ROOT
from random import randint as rnd
from datetime import date

@app.task
def downloader(link):
    path = MEDIA_ROOT + '/videos/'

    try:
        yt = YouTube(link)
        name = 'youbute-%s-%s'%(str(date.today()),''.join([str(rnd(0,9)) for i in range(9)]))
        stream = yt.streams.first()
        stream.download(path, filename=name)
        return {'stat':True, 'name': name + '.mp4', 'title': yt.title}
    except Exception as e:
        return {'stat':False, 'error':e}

@app.task
def location(addr):
    return requests.get('http://ip-api.com/json/%s'%addr).json()
