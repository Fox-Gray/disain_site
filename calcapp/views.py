from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views import View

import uuid
import json

from .forms import *



# Create your views here.
def home(request):
    return render(request, 'calcapp/home.html')


def calcshirka(request):
    # присваиваю переменной значение формы для отправки переменной в html через рендер
    # тут уже прописываю условия заполнения формы и обработки
    if request.method == "POST":
        formshir = shirprint(request.POST)
        # Получаем текущего пользователя
        user = request.user
        # --------------------------------------
        num1 = request.POST.get("shir")
        num2 = request.POST.get("vis")
        chelam = request.POST.get("checklaminat")
        lamsum = 0
        cheplot = request.POST.get("checkplotter")
        dliploter = request.POST.get("dliplotter")
        viborkasum = 0
        cheviborka = request.POST.get("checkviborka")
        prokleikasum = 0
        cheprokbaner = request.POST.get("prokleikabaner")
        cheluversi = request.POST.get("luversi")
        kollichluversi = request.POST.get("kolvoluver")
        kolichekz = request.POST.get("kolvosh")
        matrulon = request.POST.get("matrul")
        offices = request.POST.get("ofise")
        viezdNaObjects = request.POST.get("viezdNaObject")
        commentZakaz = request.POST.get("commentZakazForm")

        summviezdNaObjects = 0
        if viezdNaObjects == 'on':
            summviezdNaObjects = 0.25
        else:
            summviezdNaObjects = 0

        sumofices = 0
        if offices == 'on':
            sumofices = 0.25
        else:
            sumofices = 0

        if cheluversi == 'on':
            kollichluversi = request.POST.get("kolvoluver")
            cheluversi1 = 'Да'
        else:
            kollichluversi = 0
            cheluversi1 = 'Нет'

        if cheprokbaner == 'on':
            prokleikasum = 20
            cheprokbaner1 = 'Да'
        else:
            prokleikasum = 0
            cheprokbaner1 = 'Нет'

        if cheviborka == 'on':
            viborkasum = 50
            cheviborka1 = 'Да'
        else:
            viborkasum = 0
            cheviborka1 = 'Нет'
        if chelam == 'on':
            lamsum = 113
            chelam1 = 'Да'
        else:
            lamsum = 0
            chelam1 = 'Нет'
        if cheplot == 'on':
            dliploter = request.POST.get("dliplotter")
            cheplot1 = 'Да'
        else:
            dliploter = 0
            cheplot1 = 'Нет'
        result = itogoshirka(num1, num2, matrulon, dliploter, kolichekz, lamsum, viborkasum,
                             prokleikasum, kollichluversi, sumofices, summviezdNaObjects)

        # Определяем, какая кнопка была нажата, ну и соответственно действие по ней
        if 'Send' in request.POST:
            return render(request, 'calcapp/calcshirka.html', {'result': result, "form": formshir})
        elif 'basket' in request.POST:
            # Проверяем, что пользователь аутентифицирован
            if user.is_authenticated:
                # код получения названия из цены
                if matrulon:
                    try:
                        material_obj = rulonmate.objects.get(cenamatzacup=matrulon)
                        material_name = material_obj.namemat  # Явно берём имя
                    except rulonmate.DoesNotExist:
                        material_name = "Материал не найден"
                else:
                    material_name = "Не выбрано"
                # =======================================
                Calculation.objects.create(
                    user=user,  # Передаем объект User
                    session_key=None,  # не нужно
                    matrul=material_name,
                    shir=num1,
                    vis=num2,
                    checklaminat=chelam1,
                    checkplotter=cheplot1,
                    dliplotter=dliploter,
                    checkviborka=cheviborka1,
                    prokleikabaner=cheprokbaner1,
                    luversi=cheluversi1,
                    kolvoluver=kollichluversi,
                    kolvosh=kolichekz,
                    result=result,
                    commentZakaz=commentZakaz
                )

                # Здесь сохранение в отдельную модель корзины
                return render(request, 'calcapp/calcshirka.html',
                              {'form': formshir}
                              )
            else:
                # Используем функцию‑помощник
                session_key = get_or_create_session_key(request)
                # код получения названия из цены
                if matrulon:
                    try:
                        material_obj = rulonmate.objects.get(cenamatzacup=matrulon)
                        material_name = material_obj.namemat  # Явно берём имя
                    except rulonmate.DoesNotExist:
                        material_name = "Материал не найден"
                else:
                    material_name = "Не выбрано"
                # =======================================
                Calculation.objects.create(
                    user=None,  # нет пользователя
                    session_key=session_key,
                    matrul=material_name,
                    shir=num1,
                    vis=num2,
                    checklaminat=chelam1,
                    checkplotter=cheplot1,
                    dliplotter=dliploter,
                    checkviborka=cheviborka1,
                    prokleikabaner=cheprokbaner1,
                    luversi=cheluversi1,
                    kolvoluver=kollichluversi,
                    kolvosh=kolichekz,
                    result=result,
                    commentZakaz=commentZakaz
                )
                # Здесь сохранение в отдельную модель корзины
                return render(request, 'calcapp/calcshirka.html',
                              {'form': formshir}
                              )
    else:
        formshir = shirprint()
        return render(request, "calcapp/calcshirka.html", {"form": formshir})