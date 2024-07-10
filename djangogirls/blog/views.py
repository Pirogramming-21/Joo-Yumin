from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {}) # 요청을 넘겨받아 render 메서드 호출

