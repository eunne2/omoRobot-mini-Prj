import json
from time import timezone
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Info


# Create your views here.


def index(request):
    info = Info.objects.all()
    return render(
        request, "index/index.html",
        {"info": info, }
    )


def test(request):
    return render(
        request, "insert/write4.html",

    )


def result(request):
    info = Info.objects.all()
    return render(
        request, "index/result.html",
        {"info": info, }
    )


def edit(request):
    info = Info.objects.all()
    if request.user.is_authenticated:
        return render(
            request, "index/edit.html",
            {"info": info, }
        )
    else:
        return render(
            request, "index/result.html",
            {"info": info,
             "e": "로그인하세요", }
        )


def insert(request):
    return render(request, "insert/write5.html")


def delete(request, pk):
    delete_info = Info.objects.get(pk=pk)
    delete_info.delete()
    info = Info.objects.all()
    return render(
        request, "index/edit.html",
        {"info": info, }
    )


def deletes(request):
    if request.method == "POST":
        if request.POST.get("check"):
            for i in request.POST.getlist("check"):
                delete_info = Info.objects.get(pk=i)
                delete_info.delete()

        info = Info.objects.all()
        return render(
            request, "index/edit.html",
            {"info": info, })
    else:
        return render(
            request, "index/edit.html",
        )


def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('..')
        else:
            return render(request, "..", {'error': "username or password is incorrect."})
    else:
        return render(request, "..")


def logout(request):
    auth.logout(request)
    return redirect('..')


@csrf_exempt
def save(request, num):
    if request.method == 'POST':
        if num == 1:
            data = json.loads(request.body)
            info = Info()
            info.bat = data
            info.save()

            context = {
                'result': data,
            }
            return JsonResponse(context)
        elif num == 2:
            data = json.loads(request.body)
            info = Info()
            info.color_r = data["r"]
            info.color_g = data["g"]
            info.color_b = data["b"]
            info.save()

            context = {
                'result': data,
            }
            return JsonResponse(context)
        elif num == 3:
            data = json.loads(request.body)
            info = Info()
            info.encoder_l = data["encoder_l"]
            info.encoder_r = data["encoder_r"]
            info.save()

            context = {
                'result': data,
            }
            return JsonResponse(context)


def introduce(request):
    info = Info.objects.all()
    return render(
        request, "index/introduce.html",
        {"info": info, }
    )


def details(request, num):
    if num == 0:
        return render(
            request, "detail/detail.html"
        )
    elif num == 1:
        return render(
            request, "detail/details1.html"
        )
    elif num == 2:
        return render(
            request, "detail/details2.html"
        )
    elif num == 3:
        return render(
            request, "detail/details3.html"
        )
    elif num == 4:
        return render(
            request, "detail/details4.html"
        )
    elif num == 5:
        return render(
            request, "detail/details5.html"
        )
    elif num == 6:
        return render(
            request, "detail/details6.html"
        )
