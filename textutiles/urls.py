"""textutiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import e1

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", e1.index, name="index"),
#     path("about", e1.about, name="about")
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", e1.index, name="index"),
    # path("removepunc", e1.removepunc, name="rempun"),
    # path("capitalizefirst", e1.capfirst, name="capfirst"),
    # path("newlineremove", e1.newlineremove, name="newlineremove"),
    # path("spaceremove", e1.spaceremove, name="spaceremove"),
    # path("charcount", e1.charcount, name="charcount"),
    path("analyze",e1.analyze, name="analyze")
]