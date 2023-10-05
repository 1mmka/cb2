from django.shortcuts import render
from .models import Book
from .validators import BookPriceValidator,BookTitleValidator
from django.http import HttpResponse
from django.core.exceptions import ValidationError

# Create your views here.
def CreateBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        
        try:
            BookTitleValidator(title)
            BookPriceValidator(price)
            return HttpResponse('все ок')
        except ValidationError:
            return HttpResponse('не ок')
    else:
        return render(request=request,template_name='book.html',context=None)