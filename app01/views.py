from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')


# 关于介绍我们的自己html路径
def aboutUs(request):
    return render(request, 'aboutUs/index.html')

def us_history(request):
    return render(request, 'aboutUs/history.html')

def us_books(request):
    return render(request, 'aboutUs/books.html')

def us_software(request):
    return render(request, 'aboutUs/software.html')

def us_train(request):
    return render(request, 'aboutUs/train.html')

def us_news(request):
    return render(request, 'aboutUs/news.html')

def us_foreword(request):
    return render(request, 'aboutUs/foreword.html')

def us_join(request):
    return render(request, 'aboutUs/join.html')



# 关于研究方向的html路径

def researchDir(request):
    return render(request, 'researchDir/index.html')

def researchdeprivation(request):
    return render(request, 'researchDir/deprivation.html')

def researchmonitor(request):
    return render(request, 'researchDir/monitor.html')

def researchregulation(request):
    return render(request, 'researchDir/regulation.html')

def researcher(request):
    return render(request, 'researchers/index.html')

def researcher_teacher(request):
    return render(request, 'researchers/teachers.html')

def researcher_graduate(request):
    return render(request, 'researchers/graduate.html')

def researcher_visiting(request):
    return render(request, 'researchers/visiting.html')

def researcher_finish(request):
    return render(request, 'researchers/finish.html')

def liupeng(request):
    return render(request, 'researchers/teachers/liupeng.html')



# 关于培养方案的html路径
def cultivation(request):
    return render(request, 'cultivation/index.html')

def cultivation_graduate(request):
    return render(request, 'cultivation/graduate.html')




# 关于成果的html路径
def mainAch(request):
    return render(request, 'mainAch/index.html')

def mainAch_fund(request):
    return render(request, 'mainAch/fund.html')

def mainAch_paper(request):
    return render(request, 'mainAch/paper.html')

def mainAch_patent(request):
    return render(request, 'mainAch/patent.html')

def mainAch_prize(request):
    return render(request, 'mainAch/prize.html')





# 关于合作交流的html路径
def cooStudy(request):
    return render(request, 'cooStudy/index.html')

def cooStudy_visiting(request):
    return render(request, 'cooStudy/visiting.html')




# 睡眠工程的html路径
def sleepEng(request):
    return render(request, 'sleepEng/index.html')

def sleepEng_hardware(request):
    return render(request, 'sleepEng/hardware.html')

def sleepEng_service(request):
    return render(request, 'sleepEng/service.html')

def sleepEng_cooperation(request):
    return render(request, 'sleepEng/cooperation.html')


def dataset(request):
    return render(request, 'dataset_info/index.html')


