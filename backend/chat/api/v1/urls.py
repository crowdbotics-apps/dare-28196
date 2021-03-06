from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MessageViewSet,
    ThreadViewSet,
    ForwardedMessageViewSet,
    ThreadActionViewSet,
    MessageActionViewSet,
    ThreadMemberViewSet,
)

router = DefaultRouter()
router.register("thread", ThreadViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("message", MessageViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("threadaction", ThreadActionViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
