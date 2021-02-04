from django.shortcuts import render

from app.functionCSV import dict_list


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}
    list_of_dict = dict_list()
    context = {'month': list_of_dict}

    return render(request, template_name, context)
