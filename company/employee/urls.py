from django.urls import path
from .import views
urlpatterns=[

    path('',views.home,name='home'),
    path('employees/',views.all_emp,name='all_emp'),
    path('registration/',views.registration,name='registration'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('remove_emp/<int:id>/',views.remove_emp,name='remove_emp'),
    path('update_form/<int:id>/',views.update_form,name='update_form'),
    path('update_form_data/<int:id>/',views.update_form_data,name='update_form_data'),
    
]