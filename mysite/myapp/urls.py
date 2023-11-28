from django.urls import path
from myapp.views import add_item, update_item, delete_item, ProductListView, ProductDetailView

app_name = 'myapp'

urlpatterns = [
    # path('', index, name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('additem/', add_item, name='additem'),
    path('updateitem/<int:id>/', update_item, name='update_item'),
    path('deleteitem/<int:id>/', delete_item, name='delete_item'),
]