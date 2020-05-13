from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    path('top/', views.top, name='top'),
    path('anken/', views.anken_list, name='anken_list'),
    path('task/', views.task, name='task'),
    path('anken/archiveanken/', views.archiveanken_list, name='archiveanken_list'),
    path('anken/weekanken/', views.weekanken_list, name='weekanken_list'),
    path('anken/add/', views.anken_edit, name='anken_add'),
    path('anken/mod/<int:anken_id>/', views.anken_edit, name='anken_mod'),
    path('anken/archive/<int:anken_id>/', views.anken_archive, name='anken_archive'),
    path('anken/archiveback/<int:anken_id>/', views.anken_archiveback, name='anken_archiveback'),
    path('anken/del/<int:anken_id>/', views.anken_del, name='anken_del'),


    path('sintyoku/<int:anken_id>/', views.SintyokuList.as_view(), name='sintyoku_list'),  # 一覧
    path('sintyoku/add/<int:anken_id>/', views.sintyoku_edit, name='sintyoku_add'),        # 登録
    path('task/add/<int:anken_id>/', views.task_edit, name='task_add'),        # 登録
    path('sintyoku/mod/<int:anken_id>/<int:sintyoku_id>/', views.sintyoku_edit, name='sintyoku_mod'),  # 修正
    path('sintyoku/del/<int:anken_id>/<int:sintyoku_id>/', views.sintyoku_del, name='sintyoku_del'),   # 削除


    path('task/top', views.task_top, name='task_top'),

]