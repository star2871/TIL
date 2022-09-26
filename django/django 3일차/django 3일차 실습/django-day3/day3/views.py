from django.shortcuts import render
import random

# Create your views here.
def index(request):

    return render(request, "index.html")


def print_number(request, id):

    if id % 2 == 0:
        num = "짝수"
        if id == 0:
            num = "0"
    else:
        num = "홀수"

    context = {"num": num, "id": id}

    return render(request, "number.html", context)


def print_calculation(request, a, b):
    num_sum = a + b
    num_sub = a - b
    num_mul = a * b
    num_div = a // b

    context = {
        "sum": num_sum,
        "sub": num_sub,
        "mul": num_mul,
        "div": num_div,
        "a": a,
        "b": b,
    }

    return render(request, "calculator.html", context)


def print_past(request):
    now = request.GET.get("now")
    names = ["이순신", "주몽", "루피", "왕건"]
    images = {
        "이순신": "https://w.namu.la/s/f7e191c108090d585c33a0c2e5d07d4cad14b196bc39db0d3ba62c5f95ca272580c44e2fe588825de1def96e834e14ec642cf5a389e56c07a8b44cd252b784e251003603ee62fdd5e2c9742da725205b0208e9e2f405ea2430081288ccae35ac",
        "주몽": "http://ojsfile.ohmynews.com/STD_IMG_FILE/2011/0207/IE001276414_STD.jpg",
        "루피": "https://post-phinf.pstatic.net/MjAyMTAzMjhfNyAg/MDAxNjE2OTMxMDk0NDY1.j4JGIt_LNKXTAwJK4qFYS1egSxvvsO3qODiE6axIvowg.KtMKJiObYIkNxP7cYDTOyKUSAT7a-FDFCLPS-rOVsR8g.JPEG/unnamed_%281%29.jpg?type=w1200",
        "왕건": "https://t1.daumcdn.net/cfile/tistory/995156435C81D1EE1D",
    }
    name = random.choice(names)

    context = {
        "name": name,
        "image": images.get(name),
        "now": now,
    }
    return render(request, "past.html", context)


def print_name(request):
    return render(request, "name.html")


def print_lorem(request):
    return render(request, "lorem.html")


def lorem_show(request):
    cnt_para = int(request.GET.get("para"))
    cnt_words = int(request.GET.get("words"))

    # lorems = [[] for _ in range(cnt_para)]
    lorems = [[] for _ in range(cnt_para)]
    ran_words = [
        "바나나",
        "짜장면",
        "사과",
        "바나나",
        "딸기",
    ]

    for i in range(len(lorems)):
        while len(lorems[i]) < cnt_words:
            word = random.choice(ran_words)
            lorems[i].append(word)

    context = {"lorems": lorems}
    return render(request, "lorem_show.html", context)
