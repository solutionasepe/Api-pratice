from django.urls import path, include
from . import views

urlpatterns = [  
    path("<int:pk>/", views.ProductDetailViews.as_view(), name="product-detail"),
    path("<int:pk>/update", views.ProductUpdate.as_view(), name="product-update"),
    path("<int:pk>/delete", views.ProductDelete.as_view(), name="product-delete"),
    path("", views.ProductCreateViews.as_view(), name="product-create"),
    # path("", views.product_alt_view, name="product-create"),
    # path("<int:pk>/", views.product_alt_view, name="product-detail"),
]