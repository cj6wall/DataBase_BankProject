from django.shortcuts import render, redirect, render_to_response

from django.http import HttpResponse

from datetime import datetime

from .models import Data

from .form import BankdataForm

from .prediction import Predict

# Create your views here.

def index(request):
    data = Data.objects.order_by('-id') #呼叫model中的物件

    result, probility, word, test = Predict.do_prediction()

    context = {'bankdata' : data , 'Result' : result, 'Probility' : probility,'Word' : word, 'Test' : test} #傳到templates

    # return HttpResponse('Testing123')
    return render(request, 'index.html',  context)#傳到templates

def sign(request):
    bdata = Data.objects.all()

    if request.method == 'POST':
        dataform = BankdataForm(request.POST)

        if dataform.is_valid():
            new_comment = Data(id=request.POST['id'],name=request.POST['name'],
                age=request.POST['age'],marital=request.POST['marital'],
                education=request.POST['education'],housing=request.POST['housing'],
                balance=request.POST['balance'],loan=request.POST['loan'],
                duration=request.POST['duration'])
            new_comment.save()
            return redirect('index')

    else:
        dataform = BankdataForm()

    context = {'Dataform' : dataform , 'lendata' : bdata}

    # return HttpResponse('Testing123')
    return render(request, 'sign.html', context)

def bank(request):
    bdata = Data.objects.all()#Data是我在MySQL中table的名稱

    id = Data._meta.get_field('id').column
    name = Data._meta.get_field('name').column
    age = Data._meta.get_field('age').column
    marital = Data._meta.get_field('marital').column
    education = Data._meta.get_field('education').column
    balance = Data._meta.get_field('balance').column
    housing = Data._meta.get_field('housing').column
    loan = Data._meta.get_field('loan').column
    duration = Data._meta.get_field('duration').column
    y = Data._meta.get_field('y').column

    # tar = Data.objects.filter(age__contains='58')
    # print(tar)

    return render_to_response('bank.html', locals())
