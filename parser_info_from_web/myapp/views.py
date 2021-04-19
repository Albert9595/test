from django.shortcuts import render, redirect
from .models import JobVacancy
from django.views import View
from .tasks import parser_hh_vacans_api

# Create your views here.



class GetParsInfo(View):
    def get(self, request):
        shelf = JobVacancy.objects.all()
        return render(request, 'vacans_info.html', {'shelf': shelf})
    def post(self, request):
        context = {}
        City = request.POST["City"]
        Vacans = request.POST["Vacancy"]
        task = parser_hh_vacans_api.delay(Vacans, City)
        context['task_id'] = task.id
        context['task_status'] = task.status
        return render(request, 'vacans_info.html', context)

