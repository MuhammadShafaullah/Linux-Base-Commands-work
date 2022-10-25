from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def home(request):
    names = {'one': 'Ali',
             'two': 'Rashid',
             'Three': 'Ahmad',
             'num': ['one','Apple','two','Banana'],
             'student_info':[
                             {'name':'Sohail','phone':'0306287969'},
                             {'name':'ALI','phone':'0306287969'},
                            ]
             }

    return render(request, 'course/base.html', names)


def math(request):

    a = 10+10
    today = datetime.datetime.today()

    return HttpResponse(f'Math function {a}')
