from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name = "main_page"),
    path('import/', views.import_people_from_excel, name='import'),
    path('current_birthday/', views.CurrentBirthdayListView.as_view(), name="current_birthday"),
    path('tick_person/<int:person_id>', views.chocolate_tick, name='tick_person')

]