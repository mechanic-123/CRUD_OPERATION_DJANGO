from django.urls import path
from .views import Crud


urlpatterns = [
    path("",Crud.create_task, name="create_task"),
    path('list/',Crud.list_task, name='list_task'),
    path('list/<int:id>/',Crud.list_id ,name="list_id"),
    path('update/<int:id>',Crud.update , name="update"),
    path('delete/<int:id>/', Crud.delete , name='delete')
]
