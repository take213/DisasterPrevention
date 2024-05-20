from django.urls import path
from matchingapp.views import MatchingView, MatchedView, UpdateDataView

urlpatterns = [
    path('', MatchingView.as_view(), name="matching"),
    path('matched', MatchedView.as_view(), name="matched"),
    path('start-matching/', UpdateDataView.as_view(), name='update'),
]
