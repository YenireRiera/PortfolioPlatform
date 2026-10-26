from django.urls import include, path


urlpatterns = [
    path(
        "",
        include("api.portfolio.urls"),
    ),

    path(
        "services/",
        include("api.services.urls"),
    ),
]