from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from datetime import datetime
from .forms import RawTodoForm
import sklearn
import pickle

# Create your views here.

items = ['apple',
 'buger',
 'chocolate',
 'donuts',
 'egg',
 'fish',
 'garlic',
 'honey',
 'ice cream',
 'jelly',
 'ketchup',
 'lemons',
 'mango',
 'oranges',
 'pasta',
 'yougurt',
 'quicee',
 ' carrot',
 'rice',
 'olive oil',
 ' yam',
 'popcorn',
 'nut',
 'tomato',
 'vegetables',
 'peri sauces',
 'mutton',
 'spaghetti',
 'wings',
 'Date']


filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the todo index.</h1>")

def get_purchases_by_date(request,year,month,day):
    try:

        dt = str(year)+"/"+str(month)+"/"+str(day)
        purchase_date = datetime.strptime(dt,'%y/%m/%d')
        products = Todo.objects.get(date=purchase_date).products
        return HttpResponse("<h1>Hello, today purchases are %s</h1>" % [x for x in products])

    except Exception as e:
        return HttpResponse(e)

def get_purchases(request):
    try:
        products = Todo.objects.all()
        products = [x.products for x in products]
        return HttpResponse("Hello, all purchases are %s" % products)
    except Exception as e:
        return HttpResponse(e)

def post_purchases(request):
    try:
        form = RawTodoForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, "create.html", context)


    except Exception as e:
        print(e)
        return HttpResponse(e)

def predictor(request):

    data = request.form

    dt = str(data["year"])+str(data["month"])+str(data["day"])
    prediction = model.predict([[int(dt)]])
    prediction = [int(round(x)) for x in prediction]
    needs =[]
    for x in range(0,len(prediction)):
        if prediction[x] == 1:
            needs.append(items[x])

    context = {
        'needs' : needs
    }
    return render(request, "predictor.html", context)

