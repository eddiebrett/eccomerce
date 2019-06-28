{"filter":false,"title":"urls.py","tooltip":"/ecommerce/urls.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":19,"column":34},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":98}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":34},"action":"insert","lines":["from cart import urls as urls_cart"],"id":99}],[{"start":{"row":20,"column":5},"end":{"row":20,"column":9},"action":"remove","lines":["cart"],"id":100},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["s"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["e"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":["a"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["r"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["c"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["h"]}],[{"start":{"row":20,"column":32},"end":{"row":20,"column":36},"action":"remove","lines":["cart"],"id":101},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["s"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["e"]},{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"insert","lines":["a"]},{"start":{"row":20,"column":35},"end":{"row":20,"column":36},"action":"insert","lines":["r"]},{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["c"]},{"start":{"row":20,"column":37},"end":{"row":20,"column":38},"action":"insert","lines":["h"]}],[{"start":{"row":30,"column":39},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":104},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":39},"action":"insert","lines":["url(r'^cart/', include(urls_cart)),"],"id":105}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":15},"action":"remove","lines":["cart"],"id":106},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["s"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":["e"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["a"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["r"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["c"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["h"]}],[{"start":{"row":31,"column":34},"end":{"row":31,"column":38},"action":"remove","lines":["cart"],"id":107},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"insert","lines":["s"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"insert","lines":["e"]},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"insert","lines":["a"]},{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"insert","lines":["r"]},{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["c"]},{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["h"]}],[{"start":{"row":0,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["\"\"\"ecommerce URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]",""],"id":108},{"start":{"row":0,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["\"\"\"ecommerce URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]",""]}]]},"ace":{"folds":[],"scrolltop":305,"scrollleft":0,"selection":{"start":{"row":33,"column":0},"end":{"row":33,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":43,"mode":"ace/mode/python"}},"timestamp":1561720469817,"hash":"649a8afd3202db0802da154c4d43fc862d863c79"}