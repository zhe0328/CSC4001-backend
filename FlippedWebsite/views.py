from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pandas as pd
from django.db import connection
import json

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, "signup.html")


def index(request):
    return render(request, 'index.html')


def community(request):
    return render(request, 'Community.html')


def community_video(request):
    return render(request, 'Single_Video_Simplified_Page.html')


def trading(request):
    return render(request, 'trading.html')


def trading_video(request):
    return render(request, "trad_video.html")


def upload_video(request):
    return render(request, "Upload_Video.html")


def single_channel_home(request):
    return render(request, "Single_Channel_Home.html")


def single_channel_video(request):
    return render(request, "Single_Channel_Videos.html")


def single_channel_playlist(request):
    return render(request, "Single_Channel_Playlist.html")


def single_channel_channels(request):
    return render(request, "Single_Channel_Channels.html")


def login_validation(request):
    return_data = dict()
    if request.method == "POST":
        print("Temp!")
        post_body = request.body
        print(post_body)
        json_result = json.loads(post_body)
        username = json_result['username']
        password = json_result['password']
        cursor = connection.cursor()
        # username = request.Post.get('username',None)
        # password = request.Post.get('password',None)
        if username and password:
            username = username.strip()
            try:
                user_command = "select password from user where username = '{}'".format(
                    username)
                cursor.execute(user_command)
                user_list = pd.DataFrame(cursor.fetchall())
                for data in user_list.itertuples():
                    user_pwd = data[1]
                if user_pwd == password:
                    return_data["status"] = 100
                    return JsonResponse(return_data)
                    # return render(request,'index.html')
                else:
                    return_data["status"] = 200
                    return JsonResponse(return_data)
                    # return render(request,'login.html',{'error':'Wrong password!'})
            except:
                return_data["status"] = 300
                return JsonResponse(return_data)
                # return render(request,'login.html',{'error':'Username does not exist!'})

            finally:
                connection.close()
    return_data["status"] = 400
    return JsonResponse(return_data)
    # return render(request,'login.html',{'error':'Empty username or password!'})
