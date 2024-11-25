from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'news'

# URLパターンを登録する変数
urlpatterns = [
    # newsアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    path('post/', views.CreateNewsView.as_view(), name='post'),

    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    path('news/<int:category>', views.CategoryView.as_view(), name='news_cat'),

    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),

    path('news-detail/<int:pk>', views.DetailView.as_view(), name='news_detail'),

    path('mypage/', views.MypageView.as_view(), name='mypage'),

    path('photo/<int:pk>/delete/', views.NewsDeleteView.as_view(), name = 'news_delete'),
]
