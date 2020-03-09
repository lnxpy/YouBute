from django.shortcuts import render, redirect
from django.http import HttpResponse
from .tasks import *
from .models import Activity
from os import path

# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST:
            url = request.POST.get("url","")
            conf = downloader(url)
            if conf['stat']:
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                context = {
                            'status': conf['stat'],
                            'path':'media/videos/%s'%conf['name'],
                            }
                loc = location(ip)
                Activity.objects.create(
                    activity_user = request.user,
                    activity_vid = conf['title'],
                    activity_addr = ip,
                    activity_loc = '(%s)%s %s LAT %s - LONG %s'%(loc['countryCode'], loc['country'],loc['timezone'],loc['lat'],loc['lon']),
                    activity_reg = loc['regionName'],
                    activity_isp = loc['isp'],
                    activity_url = url,
                    activity_path = context['path']
                )
                return render(request, 'web/download.html', context)
            else:
                context = {
                            'status': conf['stat'],
                            'error': conf['error'],
                            }
                return render(request, 'web/download.html', context)
    else:
        return render(request, 'web/index.html', context={})
