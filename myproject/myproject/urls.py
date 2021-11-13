"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('A_a/', myapp.views.A_a, name='A_a'),
    path('A_b/', myapp.views.A_b, name='A_b'),
    path('A_c/', myapp.views.A_c, name='A_c'),
    path('A/', myapp.views.A, name='A'),
    path('B/', myapp.views.B, name='B'),
    path('B_a/', myapp.views.B_a, name='B_a'),
    path('B_b/', myapp.views.B_b, name='B_b'),
    path('act/', myapp.views.act, name='act'),
    path('content/', myapp.views.content, name='content'),
    path('create/', myapp.views.create, name='create'),
    path('dance/', myapp.views.dance, name='dance'),
    path('music/', myapp.views.music, name='music'),
    path('nature/', myapp.views.nature, name='nature'),
    path('picture/', myapp.views.picture, name='picture'),
    path('Qna/', myapp.views.Qna, name='Qna'),
    path('idea/', myapp.views.idea, name='idea'),
    path('society/', myapp.views.society, name='society'),
    path('sports/', myapp.views.sports, name='sports'),
    path('', myapp.views.start, name='start'), path('start/', myapp.views.startend, name='start'),
    path('volunteer/', myapp.views.volunteer, name='volunteer'),
    path('list/', myapp.views.listall, name='list'),


]

