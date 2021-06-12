from django.urls import include, path
from django.conf.urls import url
from .views import ProductListView, CategoryProductListView, ProductDetailView
from . import views

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('list/category/<str:category>/', CategoryProductListView.as_view(), name='category-product-list'),
    #path('product/comment/<int:pk>/', views.add_comment, name='add-comment'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('product/comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

]
