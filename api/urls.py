from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('address', views.PropertyAddressView, basename='address')
router.register('images', views.PropertyImageView, basename='image')
router.register('reviews', views.PropertyReviewView, basename='review')
urlpatterns = router.urls