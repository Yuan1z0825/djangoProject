"""djangoProject URL Configuration

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
from django.views.generic import RedirectView

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', RedirectView.as_view(url='/', permanent=False)),

    # 关于介绍我们的自己html路径
    path('aboutUs/index.html', views.aboutUs, name='aboutUs'),
    path('aboutUs/history.html', views.us_history, name='us_history'),
    path('aboutUs/books.html', views.us_books, name='us_books'),
    path('aboutUs/software.html', views.us_software, name='us_software'),
    path('aboutUs/train.html', views.us_train, name='us_train'),
    path('aboutUs/news.html', views.us_news, name='us_news'),
    path('aboutUs/foreword.html', views.us_foreword, name='us_foreword'),
    path('aboutUs/join.html', views.us_join, name='us_join'),


    #关于研究方向的html路径
    path('researchDir/index.html', views.researchDir, name='researchDir'),
    path('researchDir/deprivation.html', views.researchdeprivation, name='researchdeprivation'),
    path('researchDir/monitor.html', views.researchmonitor, name='researchmonitor'),
    path('researchDir/regulation.html', views.researchregulation, name='researchregulation'),


    #关于研究人员的html路径
    path('researchers/index.html', views.researcher, name='researcher'),
    path('researchers/teachers.html', views.researcher_teacher, name='reasercher_teacher'),
    path('researchers/graduate.html', views.researcher_graduate, name='reasercher_graduate'),
    path('researchers/visiting.html', views.researcher_visiting, name='reasercher_visiting'),
    path('researchers/finish.html', views.researcher_finish, name='reasercher_finish'),

    #关于培养方案的html路径
    path('cultivation/index.html', views.cultivation, name='cultivation'),
    path('cultivation/graduate.html', views.cultivation_graduate, name='cultivation_graduate'),

    #关于成果的html路径
    path('mainAch/index.html', views.mainAch, name='mainAch'),
    path('mainAch/fund.html', views.mainAch_fund, name='mainAch_fund'),
    path('mainAch/paper.html', views.mainAch_paper, name='mainAch_paper'),
    path('mainAch/patent.html', views.mainAch_patent, name='mainAch_patent'),
    path('mainAch/prize.html', views.mainAch_prize, name='mainAch_prize'),

    #关于合作交流的html路径
    path('cooStudy/index.html', views.cooStudy, name='cooStudy'),
    path('cooStudy/visiting.html', views.cooStudy_visiting, name='cooStudy_visiting'),

    #睡眠工程的html路径
    path('sleepEng/index.html', views.sleepEng, name='sleepEng'),
    path('sleepEng/hardware.html', views.sleepEng_hardware, name='sleepEng_hardware'),
    path('sleepEng/service.html', views.sleepEng_service, name='sleepEng_service'),
    path('sleepEng/cooperation.html', views.sleepEng_cooperation, name='sleepEng_cooperation'),

    #数据集的html路径
    path('dataset_info/index.html', views.dataset, name='dataset'),
]
