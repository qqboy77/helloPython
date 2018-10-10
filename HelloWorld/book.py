from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from bookManager.models import Book
from django.core import serializers
import json
# @require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'),book_author=request.GET.get('book_author'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# @require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    # response1 = ''
    # for var in books:
    #     response1 += var.book_name + ' '
    # response = response1
    # return HttpResponse("<p>"+response+"</p>")
    return JsonResponse(response)