from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from matchingapp.models import Supply, Demand
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


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
            for demand in demands:
                supplies = Supply.objects.filter(completed=False)
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


class AddSupplyItem(CreateView):
    model = Supply
    # DBテーブルの全カラムの情報をfieldsに格納
    fields = '__all__'
    # 成功したときのリダイレクト先
    success_url = reverse_lazy('matching')


class AddDemandItem(CreateView):
    model = Demand
    # DBテーブルの全カラムの情報をfieldsに格納
    fields = '__all__'
    # 成功したときのリダイレクト先
    success_url = reverse_lazy('matching')


class UpdateSupplyItem(UpdateView):
    model = Supply
    # DBテーブルの全カラムの情報をfieldsに格納
    fields = '__all__'
    # 成功したときのリダイレクト先
    success_url = reverse_lazy('matching')


class UpdateDemandItem(UpdateView):
    model = Demand
    # DBテーブルの全カラムの情報をfieldsに格納
    fields = '__all__'
    # 成功したときのリダイレクト先
    success_url = reverse_lazy('matching')


class DeleteSupplyItem(DeleteView):
    model = Supply
    # DBテーブルの全カラムの情報をfieldsに格納
    fields = '__all__'
    # 成功したときのリダイレクト先
    success_url = reverse_lazy('matching')


class DeleteDemandItem(DeleteView):
    model = Demand
    # DBテーブルの全カラムの情報をfieldsに格納
    fields = '__all__'
    # 成功したときのリダイレクト先
    success_url = reverse_lazy('matching')