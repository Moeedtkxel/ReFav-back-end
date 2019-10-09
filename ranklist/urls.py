from django.urls import path, re_path
from .views import DisplayAllRankLists, RankListViaURL

urlpatterns = [
    re_path(r'^ranklists/$', DisplayAllRankLists.as_view(), name='RankLists view'),
    re_path(r'^ranklists/view/', RankListViaURL.as_view(), name='product-edit'),
]
