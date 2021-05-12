from django.http import HttpResponseRedirect

def my_login(func):
    def inner(*args,**kwargs):
        login_user_id = args[0].session.get('logined_username')
        if login_user_id:
            return func(*args,**kwargs)
        else:
            return HttpResponseRedirect("login")
    return inner