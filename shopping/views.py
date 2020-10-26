from django.shortcuts import render

# Create your views here.
from django.views import View
from .forms import SearchForm
from .models import Product


#会員登録しているユーザーには会員登録時に指定した名前を表示する。
#GET:商品検索、
#POST:カートに入れたときの処理(ただし、会員登録をしていないと受け付けない)
class ShoppingView(View):

    def reference(self):

        search_form = SearchForm()

        return search_form

    def search(self,word):

        search_result = Product.objects.filter(name__contains=word)

        return search_result

    def get(self, request, *args, **kwargs):

        search_form = self.reference()

        if "search_word" in request.GET:
            search_result   = self.search(request.GET["search_word"])
        else:
            search_result   = None

        #商品検索時の処理
        context = { "search_form":search_form,
                    "search_result":search_result,
                    }

        return render(request,"shopping/index.html",context)

    def post(self, request, *args, **kwargs):


        #TODO:商品をカートに入れた時、アカウントのカートに追加する。

        search_form = self.reference()
        context = { "search_form":search_form,
                    }

        return render(request,"shopping/index.html",context)

index       = ShoppingView.as_view()

#TODO:ショッピングカート確認ページをレンダリングするビューを作る


