from django.urls import path
from .views import ProductView,UserView, CategoryView, ProductFeatureView, FeatureView, CommentView, ImageView

app_name = "category"

urlpatterns = [
    path("product/<int:pk>/", ProductView.as_view(), name='product'),
    path("category/<int:pk>/", CategoryView.as_view(), name='category'),
    path("product-feature/<int:pk>/", ProductFeatureView.as_view(), name='product-feature'),
    path("feature/<int:pk>/", FeatureView.as_view(), name='feature'),
    path("comment/<int:pk>/", CommentView.as_view(), name='comment'),
    path("image/<int:pk>/", ImageView.as_view(), name='image'),
    path("user/<int:pk>/", UserView.as_view(), name='user'),
]