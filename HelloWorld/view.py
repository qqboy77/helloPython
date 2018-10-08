from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['world'] = '赵琦 你好!'
    context['condition'] = False
    return render(request, 'hello.html', context)
