import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def downloader(link):
    path = './videos/'

    # real script {
    try:
        r = requests.get(link).text
        soup = BeautifulSoup(r, 'html.parser')
        yt = YouTube(link)
        dir_path = path + yt.title + '.mp4'
        stream = yt.streams.first()
        stream.download(path)
        print('done')
        return {'stat':True, 'name': soup.title.text + '.mp4'}
    except Exception as e:
        print('error', e)
        return {'stat':False, 'error':e}

s = input('link: ')
downloader(s)
