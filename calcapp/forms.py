from django import forms

class shirprint(forms.Form):

    matrul = forms.ChoiceField(
        label="Наименование материала",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    shir = forms.DecimalField(label="ширина материала в (м)", initial=0, max_value=1.5)
    vis = forms.DecimalField(label="высота материала в (м)", initial=0)
    checklaminat = forms.BooleanField(label="ламинация (нет/да)", required=False)
    checkplotter = forms.BooleanField(label="плоттерная резка (нет/да)", required=False)
    dliplotter = forms.DecimalField(label="длина плоттерки в (м.п)", initial=0)
    checkviborka = forms.BooleanField(label="выборка (нет/да)", required=False)
    prokleikabaner = forms.BooleanField(label="проклейка банера (нет/да)", required=False)
    luversi = forms.BooleanField(label="люверсы (нет/да)", required=False)
    kolvoluver = forms.IntegerField(label="Количество люверсов (шт. на 1 метр)", initial=0)
    kolvosh = forms.IntegerField(label="Количество экземпляров (шт)", initial=1)
    ofise = forms.BooleanField ( label = "Услуги офиса (нет/да)" , required = False )
    viezdNaObject = forms.BooleanField(label="Выезд на объект (нет/да)", required=False)
    commentZakazForm = forms.CharField(label="Коментарий к заказу", max_length= 255, required=False)

    # _______________________________________________________
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

