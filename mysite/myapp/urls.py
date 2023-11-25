from django.urls import path
from myapp.views import index, indexItem, add_item, update_item, delete_item

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', indexItem, name='detail'),
    path('additem/', add_item, name='additem'),
    path('updateitem/<int:id>/', update_item, name='update_item'),
    path('deleteitem/<int:id>/', delete_item, name='delete_item'),
]