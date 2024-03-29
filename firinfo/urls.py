from django.urls import path

from . import views


urlpatterns = [
    path('to/<int:fir_id>/<int:admin_id>', views.firinfo, name="firinfo"),
    path('applyfir/<int:user_id>', views.applyfir, name="applyfir"),
    path('to/<int:fir_id>/<int:admin_id>/', views.fircomplete, name="fircomplete"),
    path('to/<int:fir_id>/<int:admin_id>/<int:criminal_id>', views.fircomplete, name="fircomplete"),
]