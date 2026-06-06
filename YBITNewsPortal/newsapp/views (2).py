from django.shortcuts import render

def movie_info(request):
    mydict={'head_msg' : 'Movies Information',
            'sub_msg1' : 'Salman Khan ready to marraige',
            'sub_msg2' : 'Shahrukh Khan ready to marraige',
            'sub_msg3' : 'Doomsday is coming',
            'images': [
                'images/salman.png',
                'images/sharukh.png',
                'images/doomsday.png',
            ],
    }
    return render(request, "news.html", context = mydict)

def sports_info(request):
    mydict={'head_msg' : 'Sports Information',
            'sub_msg1' : 'Football match today',
            'sub_msg2' : 'Basketball game tomorrow',
            'sub_msg3' : 'Tennis tournament next week',
            'images': [
                'images/image_bg.png',
                'images/photo.jpeg',
                'images/photo_upscayl_2x_upscayl-standard-4x.png',
            ],
    }
    return render(request, "news.html", context = mydict)

def politics_info(request):
    mydict={'head_msg' : 'Politics Information',
            'sub_msg1' : 'Elections coming soon',
            'sub_msg2' : 'New policies announced',
            'sub_msg3' : 'International summit next month',
            'images': [
                'images/WhatsApp Image 2026-06-06 at 3.53.14 PM.jpeg',
                'images/813ea4dad276f7fb7667a958117b0d84.jpg',
                'images/images (1).jpg',
            ],
    }
    return render(request, "news.html", context = mydict)


def index(request):
    mydict={'head_msg' : 'Welcome to YBIT News Portal'}
    return render(request, "index.html", context = mydict)