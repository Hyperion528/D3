# from django.shortcuts import render
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from .models import New, Category
from datetime import datetime
 
 
class NewList(ListView):
    model = New #модель, объекты которой мы будем выводить
    template_name = 'news.html'  #указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты 
    context_object_name = 'news'  
    queryset = New.objects.order_by('-id')
 
    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context
 
 
# создаём представление, в котором будут детали конкретного отдельного товара
class NewDetail(DetailView):
    model = New # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html'  # название шаблона будет product.html
    context_object_name = 'new'  # название объекта. в нём будет

