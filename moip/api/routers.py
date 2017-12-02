from rest_framework.routers import DefaultRouter

from moip.api import views

router = DefaultRouter()
router.register("subscription", views.SubscriptionsView)
