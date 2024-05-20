from django.urls import path
from matchingapp.views import MatchingView, MatchedView, UpdateDataView, AddSupplyItem, AddDemandItem, UpdateSupplyItem, UpdateDemandItem, DeleteSupplyItem, DeleteDemandItem

urlpatterns = [
    path('', MatchingView.as_view(), name="matching"),
    path('matched', MatchedView.as_view(), name="matched"),
    path('start-matching/', UpdateDataView.as_view(), name='update'),
    path('add-supply-item/', AddSupplyItem.as_view(), name='add-supply-item'),
    path('add-demand-item/', AddDemandItem.as_view(), name='add-demand-item'),
    path('edit-supply-item/<int:pk>/', UpdateSupplyItem.as_view(), name='edit-supply-item'),
    path('edit-demand-item/<int:pk>/', UpdateDemandItem.as_view(), name='edit-demand-item'),
    path('delete-supply-item/<int:pk>/', DeleteSupplyItem.as_view(), name='delete-supply-item'),
    path('delete-demand-item/<int:pk>/', DeleteDemandItem.as_view(), name='delete-demand-item'),

]
