from django.shortcuts import render

def movie_info(request):
    mydict={'head_msg' : 'Movies Information',
            'sub_msg1' : 'Salman Khan ready to marraige',
            'sub_msg2' : 'Shahrukh Khan ready to marraige',
            'sub_msg3' : 'Doomsday is coming',
    }
    return render(request, "news.html", context = mydict)

def sports_info(request):
    mydict={'head_msg' : 'Sports Information',
            'sub_msg1' : 'Football match today',
            'sub_msg2' : 'Basketball game tomorrow',
            'sub_msg3' : 'Tennis tournament next week',
    }
    return render(request, "news.html", context = mydict)

def politics_info(request):
    mydict={'head_msg' : 'Politics Information',
            'sub_msg1' : 'Elections coming soon',
            'sub_msg2' : 'New policies announced',
            'sub_msg3' : 'International summit next month',
    }
    return render(request, "news.html", context = mydict)

def index(request):
    mydict={'head_msg' : 'Welcome to YBIT News Portal'}
    return render(request, "index.html", context = mydict)