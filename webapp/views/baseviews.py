from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse
from django.template import loader

from webapp.models import AppNews
from webapp.sql.db_sql import Sql


def index(request):
    """Index page"""
    template = loader.get_template("webapp/index.html")
    news = AppNews.objects.all().order_by("-news_date")
    return HttpResponse(template.render(
        {
            "news": news,
        },
        request=request,
    ))


def legalmention(request):
    """Legal mentions page"""
    template = loader.get_template("webapp/legalmention.html")
    return HttpResponse(template.render(request=request))


@staff_member_required
def create_news(request):
    """"""
    template = loader.get_template("webapp/create_news.html")
    return HttpResponse(template.render(request=request))


@staff_member_required
def ajax_create_news(request):
    """"""
    current_user = request.user
    get_title = request.GET.get("title")
    get_content = request.GET.get("content")
    news_data = {
        "title": get_title,
        "content": get_content,
        "user": current_user,
    }
    Sql.add_news(news_data)
    return JsonResponse({"response": "success"})


@staff_member_required
def ajax_destroy_news(request):
    """"""
    get_news = request.GET.get("news")
    Sql.destroy_news(get_news)
    return JsonResponse({"response": "success"})
