from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList.as_view(), name='book-lists'),
    path('<uuid:pk>/',BookDetails.as_view(), name='book-details'),
    path('search/',SearchBookList.as_view(), name ='search_results'),
]
