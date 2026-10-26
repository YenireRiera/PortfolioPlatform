from django.urls import include, path

from .views import ContactMessageCreateAPIView


urlpatterns = [
    path(
        "",
        ContactMessageCreateAPIView.as_view(),
        name="contact-message-create",
    ),

]