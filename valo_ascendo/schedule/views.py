from django.shortcuts import render
from django.views import View

from . import models


class ScheduleView(View):
    def get(self, request):
        context = {'finals': models.Final.objects.all(), 'semi_finals': models.SemiFinal.objects.all(),
                   'qrtrs': models.QuarterFinal.objects.all(), 'prelims': models.KnockOut.objects.all()}

        return render(request, 'index.html', context)


schedule_view = ScheduleView.as_view()
