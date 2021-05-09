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
    return render(request, 'community_video.html')


def trading(request):
    return render(request, 'trading.html')


def trading_video(request):
    return render(request, "trad_video.html")


def upload_video(request):
    return render(request, "Upload_Video.html")


def single_channel_home(request):
    return render(request, "Single_Channel_Home.html")


def login_validation(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        username = json_result['username']
        password = json_result['password']
        cursor = connection.cursor()
        if username and password:
            username = username.strip()
            try:
                user_sql = "select password from user where username = %s"
                cursor.execute(user_sql, username)
                user_list = pd.DataFrame(cursor.fetchall())
                user_pwd = user_list.iloc[0, 0]
                if user_pwd == password:
                    return_data["status"] = 100
                    return JsonResponse(return_data)
                else:
                    return_data["status"] = 200
                    return JsonResponse(return_data)
            except:
                return_data["status"] = 300
                return JsonResponse(return_data)
            finally:
                connection.close()
    return_data["status"] = 400
    return JsonResponse(return_data)


def create_user(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        username = json_result['username']
        password = json_result['password']
        email = json_result['email']
        gender = json_result['gender']
        cursor = connection.cursor()
        username = username.strip()
        try:
            user_sql = "select * from user where username = %s"
            cursor.execute(user_sql, username)
            user_list = pd.DataFrame(cursor.fetchall())
            if user_list.empty:
                user_sql = "insert into user (username, password, email, gender) values (\'%s\',\'%s\',\'%s\',\'%s\')" % (
                    username, password, email, gender)
                cursor.execute(user_sql)
                return_data["status"] = 100
                return JsonResponse(return_data)
            else:
                return_data["status"] = 200
                return JsonResponse(return_data)
        except:
            return_data["status"] = 300
            return JsonResponse(return_data)
        finally:
            connection.close()

    return_data["status"] = 400
    return JsonResponse(return_data)


def upload_video_info(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        username = json_result['username']
        link = json_result['link']
        time = json_result['time']
        title = json_result['title']
        price = json_result['price']
        t_type = json_result['type']
        deadline = json_result['deadline']
        summary = json_result['summary']
        cursor = connection.cursor()

        try:
            video_sql = "insert into video (link, time) values (\'%s\',\'%s\')" % (
                link, time)
            cursor.execute(video_sql)
            select_video = "select video_id from video where link = %s"
            cursor.execute(select_video, link)
            video_list = pd.DataFrame(cursor.fetchall())
            select_type = "select type_id from type where name = %s"
            cursor.execute(select_type, t_type)
            type_list = pd.DataFrame(cursor.fetchall())
            select_user = "select user_id from user where username = %s"
            cursor.execute(select_user, username)
            user_list = pd.DataFrame(cursor.fetchall())
            if video_list.empty == False:
                video_id = video_list.iloc[0, 0]
                type_id = type_list.iloc[0, 0]
                publisher_id = user_list.iloc[0, 0]

                task_sql = "insert into task (publisher_id, video_id, title, type_id, price, summary, deadline) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % (
                    publisher_id, video_id, title, type_id, price, summary, deadline)
                cursor.execute(task_sql)

                profolio_sql = "insert into protfolio (user_id, video_id, title) values (\'%s\',\'%s\',\'%s\')" % (
                    publisher_id, video_id, title)
                cursor.execute(profolio_sql)

                return_data["status"] = 100
                return JsonResponse(return_data)
        except:
            return_data["status"] = 300
            return JsonResponse(return_data)
        finally:
            connection.close()


def add_transaction(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        username = json_result['username']
        title = json_result['title']

        cursor = connection.cursor()
        try:
            user_sql = "select user_id from user where username = %s"
            cursor.execute(user_sql, username)
            user_list = pd.DataFrame(cursor.fetchall())
            user_id = user_list.iloc[0, 0]
            task_sql = "select task_id from task where title = %s"
            cursor.execute(task_sql, title)
            task_list = pd.DataFrame(cursor.fetchall())
            task_id = task_list.iloc[0, 0]

            trans_sql = "insert into transaction (task_id, accomplisher_id, status) values (\'%s\',\'%s\', 'waiting')" % (
                task_id, user_id)
            cursor.execute(trans_sql)
            return_data["status"] = 100
            return JsonResponse(return_data)
        except:
            return_data["status"] = 200
            return JsonResponse(return_data)
        finally:
            connection.close()


def show_trade_platform(request):
    return_data = dict()
    if request.method == "GET":
        try:
            cursor = connection.cursor()
            task_sql = "select * from task"
            cursor.execute(task_sql)
            task_list = pd.DataFrame(cursor.fetchall())
            for data in task_list.itertuples():
                key = data[1]
                task_info = list()

                video_id = data[3]
                video_sql = "select time from video where video_id = %s"
                cursor.execute(video_sql, video_id)
                video_list = pd.DataFrame(cursor.fetchall())
                video_time = video_list.iloc[0, 0]
                task_info.append(data[4])  # title
                type_id = data[5]
                type_sql = "select name from type where type_id = %s"
                cursor.execute(type_sql, type_id)
                type_list = pd.DataFrame(cursor.fetchall())
                type_name = type_list.iloc[0, 0]
                task_info.append(type_name)  # type_name
                task_info.append(data[6])  # price
                task_info.append(data[8])  # deadline
                task_info.append(video_time)  # time
                return_data[key] = task_info
            return JsonResponse(return_data)
        except:
            return_data["status"] = 200
            return JsonResponse(return_data)
        finally:
            connection.close()


def show_trade_video(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        task_id = json_result['task_id']
        try:
            cursor = connection.cursor()
            task_sql = "select * from task where task_id = %d;" % (task_id)
            cursor.execute(task_sql)
            task_list = pd.DataFrame(cursor.fetchall())
            key = task_list.iloc[0, 0]
            user_id = task_list.iloc[0, 1]
            video_id = task_list.iloc[0, 2]
            title = task_list.iloc[0, 3]
            type_id = task_list.iloc[0, 4]
            price = task_list.iloc[0, 5]
            summary = task_list.iloc[0, 6]
            deadline = task_list.iloc[0, 7]
            user_sql = "select username from user where user_id = %d;" % (
                user_id)
            cursor.execute(user_sql)
            user_list = pd.DataFrame(cursor.fetchall())
            username = user_list.iloc[0, 0]
            return_data['publisher_name'] = username
            video_sql = "select link from video where video_id = %d;" % (
                video_id)
            cursor.execute(video_sql)
            video_list = pd.DataFrame(cursor.fetchall())
            video_link = video_list.iloc[0, 0]
            return_data['title'] = title
            type_sql = "select name from type where type_id = %d" % (type_id)
            cursor.execute(type_sql)
            type_list = pd.DataFrame(cursor.fetchall())
            type_name = type_list.iloc[0, 0]
            return_data['type'] = type_name
            return_data['price'] = price
            return_data['summary'] = summary
            return_data['deadline'] = deadline
            return_data['video_link'] = video_link
            return JsonResponse(return_data)
        except:
            return_data["status"] = 200
            return JsonResponse(return_data)
        finally:
            connection.close()


def show_todo_list(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        username = json_result['username']
        cursor = connection.cursor()
        try:
            user_sql = "select user_id from user where username = %s"
            cursor.execute(user_sql, username)
            user_list = pd.DataFrame(cursor.fetchall())
            accomplisher_id = user_list.iloc[0, 0]
            transaction_sql = "select task_id from transaction where accomplisher_id = %s and status = 'waiting'"
            cursor.execute(transaction_sql, accomplisher_id)
            transaction_list = pd.DataFrame(cursor.fetchall())
            task_id = transaction_list.iloc[0, 0]
            task_sql = "select task_id, video_id, title, deadline from task where task_id = %d;" % (
                task_id)
            cursor.execute(task_sql)
            task_list = pd.DataFrame(cursor.fetchall())
            task_id = task_list.iloc[0, 0]
            video_id = task_list.iloc[0, 1]
            title = task_list.iloc[0, 2]
            deadline = task_list.iloc[0, 3]
            video_sql = "select time from video where video_id = %s"
            cursor.execute(video_sql, video_id)
            video_list = pd.DataFrame(cursor.fetchall())
            video_time = video_list.iloc[0, 0]

            return_data['username'] = username
            # return_data['task_id'] = task_id
            return_data['title'] = title
            return_data['deadline'] = deadline
            return_data['time'] = video_time
            return JsonResponse(return_data)

        except:
            return_data["status"] = 200
            return JsonResponse(return_data)
        finally:
            connection.close()


def update_todo_list(request):
    return_data = dict()
    if request.method == "POST":
        post_body = request.body
        json_result = json.loads(post_body)
        task_id = json_result['task_id']
        cursor = connection.cursor()
        try:
            transaction_sql = "update transaction set status = 'finished' where task_id = %d;" % (
                task_id)
            cursor.execute(transaction_sql)
            return_data["status"] = 100
            return JsonResponse(return_data)
        except:
            return_data["status"] = 200
            return JsonResponse(return_data)
        finally:
            connection.close()
