from django.shortcuts import render

# Create your views here.
def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'html/index.html',context=params)