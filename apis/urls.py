from django.urls import path
from .views import movie, menu, image

urlpatterns = [
    # path('', team.movie),
    path('menu', menu.get_menu),
    path('movie', movie.MovieView.as_view()),
    # path('image', image.image),
    # path('imagetext', image.image_text),
    path('image', image.ImageView.as_view()),
]
