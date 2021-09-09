from django.shortcuts import render





from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings

import datetime
import json
import requests
import uuid
import os

from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context = {"products":products})
    
    
def payment(request):
	return render(request,'payment.html')

