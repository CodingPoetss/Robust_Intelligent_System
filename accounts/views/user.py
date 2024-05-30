from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts import models


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            username = username.strip()

            try:
                user = models.UserInfo.objects.get(username=username)
            except models.UserInfo.DoesNotExist:
                return JsonResponse({"code": 401, "msg": "登录失败，请重试", "data": {}}, status=401)

            if password == user.password:
                return JsonResponse({"code": 200, "msg": "登录成功", "data": {"username": username}})
            else:
                return JsonResponse({"code": 401, "msg": "密码错误", "data": {}}, status=401)

    return JsonResponse({"code": 405, "msg": "仅支持POST请求", "data": {}}, status=405)


@csrf_exempt
def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            username = username.strip()

            try:
                user = models.AdminInfo.objects.get(username=username)
            except models.AdminInfo.DoesNotExist:
                return JsonResponse({"code": 401, "msg": "登录失败，请重试", "data": {}}, status=401)

            if password == user.password:
                return JsonResponse({"code": 200, "msg": "管理员登录成功", "data": {"username": username}})
            else:
                return JsonResponse({"code": 401, "msg": "密码错误", "data": {}}, status=401)

    return JsonResponse({"code": 405, "msg": "仅支持POST请求", "data": {}}, status=405)


@csrf_exempt
def user_register_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if not (username and pwd1 and pwd2):
            return JsonResponse({"code": 400, "msg": "所有字段都是必填的", "data": {}})

        if pwd1 != pwd2:
            return JsonResponse({"code": 400, "msg": "两次输入的密码不一致", "data": {}})
        else:
            if models.UserInfo.objects.filter(username=username).exists():
                return JsonResponse({"code": 400, "msg": "用户已存在", "data": {}})
            new_user = models.UserInfo(username=username, password=pwd1)
            new_user.save()
            return JsonResponse({"code": 200, "msg": "注册成功", "data": {"username": username}})

    return JsonResponse({"code": 405, "msg": "仅支持POST请求", "data": {}}, status=405)


@csrf_exempt
def admin_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if not (username and pwd1 and pwd2):
            return JsonResponse({"code": 400, "msg": "所有字段都是必填的", "data": {}})

        if pwd1 != pwd2:
            return JsonResponse({"code": 400, "msg": "两次输入的密码不一致", "data": {}})
        else:
            if models.AdminInfo.objects.filter(username=username).exists():
                return JsonResponse({"code": 400, "msg": "用户已存在", "data": {}})
            new_user = models.AdminInfo(username=username, password=pwd1)
            new_user.save()
            return JsonResponse({"code": 200, "msg": "注册成功", "data": {"username": username}})

    return JsonResponse({"code": 405, "msg": "仅支持POST请求", "data": {}}, status=405)


@csrf_exempt
def getAlluser(request):
    if request.method == 'GET':
        users = models.UserInfo.objects.all()
        user_list = [{"username": user.username, "password": user.password} for user in users]
        return JsonResponse({"code": 200, "msg": "get all user success", "data": user_list})
