from django.shortcuts import render
from book_api.models import Books
from django.http import JsonResponse
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
# def book_list(request):
#     books = Books.objects.all() # complex data
#     bookspython = list(books.values()) # simple data/python ds
#     return JsonResponse({
#         'books': bookspython
#     })

@api_view(['GET'])
def book_list(request):
    books = Books.objects.all() # complex data
    serializer = BookSerializer(books, many=True)
    return  Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def book(request,pk):
    try:
        book = Books.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





