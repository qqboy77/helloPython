from django.http import HttpResponse
 
from TestModel.models import Test

def insertdb(request):
    request.encoding='utf-8'
    message = request.GET['name']
    test1 = Test(name=message)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def showdb(request):
    response1 = ""
    response = ""
    list = Test.objects.all()
    for var in list:
        response1 += var.name + ' '
    response = response1
    return HttpResponse("<p>"+response1+"</p>")
