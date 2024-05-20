from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from matchingapp.models import Supply, Demand


# マッチング画面
class MatchingView(TemplateView):
    template_name = 'matchingapp/matching.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supplies'] = Supply.objects.filter(completed=False)
        # context['supplies'] = Supply.objects.all()
        context['demands'] = Demand.objects.filter(completed=False)
        # context['demands'] = Demand.objects.all()
        return context


# マッチング成立済み一覧画面
class MatchedView(TemplateView):
    template_name = 'matchingapp/matched.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supplies'] = Supply.objects.filter(completed=True)
        context['demands'] = Demand.objects.filter(completed=True)
        return context


# マッチングの実行
class UpdateDataView(View):
    def post(self, request, *args, **kwargs):
        try:
            demands = Demand.objects.filter(completed=False)
            supplies = Supply.objects.filter(completed=False)
            for demand in demands:
                for supply in supplies:
                    if demand.item == supply.item and demand.quantity <= supply.quantity:
                        demand.completed = True
                        supply.completed = True
                        demand.save()
                        supply.save()
                        break
            return JsonResponse({'status': 'success',
                                 'message': 'Title updated successfully.'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error',
                                 'message': str(e)})
