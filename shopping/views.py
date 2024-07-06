from django.shortcuts import render,redirect

from django.views import View
from .models import Product

from django.db.models import Q

class IndexView(View):
    def get(self, request, *args, **kwargs):
        query                   = Q() 
        context                 = {}

        if "search_word" in request.GET:
            words   = request.GET["search_word"].replace("　"," ").split()

            for word in words:
                if word == "":
                    continue

                query &= Q(name__icontains=word)
                
        context["products"] = Product.objects.filter(query)

        return render(request,"shopping/index.html",context)

    def post(self, request, *args, **kwargs):


        return redirect("shopping:index")

index       = IndexView.as_view()


