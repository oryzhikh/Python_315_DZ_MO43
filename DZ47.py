
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_catalog),
    path('category/', views.category_list),
    path('category/<int:category_id>/', views.category_detail),
]

# в основном файле urls.py вашего проекта
from django.urls import include, path

urlpatterns = [
    # другие маршруты вашего проекта
    path('blog/', include('blog.urls')),
]

# в файле views.py вашего приложения blog
from django.http import HttpResponse, Http404

categories = {
    1: "чилл территории python",
    2: "django, сложно, но можно!",
    3: "flask, бегите, глупцы!",
}

def blog_catalog(request):
    return HttpResponse("тут будет блог")

def category_list(request):
    categories_str = ", ".join([str(key) for key in categories.keys()])
    return HttpResponse(categories_str)

def category_detail(request, category_id):
    if category_id in categories:
        return HttpResponse(categories[category_id])
    else:
        raise Http404