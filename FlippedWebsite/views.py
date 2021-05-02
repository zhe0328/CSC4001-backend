from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pandas as pd
from django.db import connection
 
# def hello(request):
#     return HttpResponse("Hello world ! ")

# def select_user(request):
#     cursor = connection.cursor()
#     user_command = "select * from csc4001.user"
#     cursor.execute(user_command)
#     user_list = pd.DataFrame(cursor.fetchall())
#     print(user_list)
#     return_data = dict()
#     return_data["temp"]=1
#     return JsonResponse(return_data)

def login(request):
    return render(request,'login.html')