from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import qrcode
from . import models
# @method_decorator(login_required(login_url='accounts/login/'), name='dispatch')
def dashboard(request):
    ctx={}
    ctx['employees'] = models.Employee.objects.all()
    return render(request, 'dashboard.html', ctx)

#Todo: вкладка с генератором, создать qr для выхода входа, изменять статус работника 

def create_qr(request, mode):
    if mode == 'log_in':
        img = qrcode.make('http://192.168.111.172:8000/qr/log_in')
        qr = "static/qr/qr.png"
        img.save(qr)
        ctx={}
        ctx['qr'] = qr
        return render(request, 'qr.html', ctx)
    elif mode == 'log_out':
        img = qrcode.make('http://192.168.111.172:8000/qr/log_out')
        qr = "static/qr/qr.png"
        img.save(qr)
        ctx={}
        ctx['qr'] = qr
        return render(request, 'qr.html', ctx)
    else:
        img = qrcode.make('http://192.168.111.172:8000/qr/rest')
        qr = "static/qr/qr.png"
        img.save(qr)
        ctx={}
        ctx['qr'] = qr
        return render(request, 'qr.html', ctx)
        
def create_qr_page(request):
    return render(request, 'create_qr_page.html')


def log_in(request):
    vlad = models.Employee.objects.get(name='Vlad0n1m')
    vlad.status = 'on_work'
    vlad.save()

    return render(request, 'log_in.html')


def log_out(request):
    vlad = models.Employee.objects.get(name='Vlad0n1m')
    vlad.status = 'not_work'
    vlad.save()
    
    return render(request, 'log_out.html')


def rest(request):
    vlad = models.Employee.objects.get(name='Vlad0n1m')
    vlad.status = 'rest'
    vlad.save()
    return render(request, 'rest.html')