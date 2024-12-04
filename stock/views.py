from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Book, AdditionalInfo, Review
import json


class BookListView(View):
    def get(self, request):
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            book = Book.objects.create(**data)
            return JsonResponse({"message": "Book created", "book_id": book.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class BookDetailView(View):
    def get(self, request, pk):
        try:
            book = Book.objects.values().get(pk=pk)
            return JsonResponse(book, safe=False)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

    def put(self, request, pk):
        try:
            data = json.loads(request.body)
            book = Book.objects.get(pk=pk)
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return JsonResponse({"message": "Book updated"})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return JsonResponse({"message": "Book deleted"}, status=204)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

class AdditionalInfoView(View):
    def get(self, request, book_id):
        info = list(AdditionalInfo.objects.filter(book_id=book_id).values())
        return JsonResponse(info, safe=False)

    def post(self, request, book_id):
        try:
            data = json.loads(request.body)
            data['book_id'] = book_id
            additional_info = AdditionalInfo.objects.create(**data)
            return JsonResponse({"message": "Additional info created", "id": additional_info.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class ReviewView(View):
    def get(self, request, book_id):
        reviews = list(Review.objects.filter(book_id=book_id).values())
        return JsonResponse(reviews, safe=False)

    def post(self, request, book_id):
        try:
            data = json.loads(request.body)
            data['book_id'] = book_id
            review = Review.objects.create(**data)
            return JsonResponse({"message": "Review created", "id": review.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)



