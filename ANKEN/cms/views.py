from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import Anken, Sintyoku, Todo, Task
from cms.forms import AnkenForm, SintyokuForm, TodoForm, TaskForm
from django.views.generic.list import ListView
from django.utils import timezone
from datetime import date, datetime
from django.views import generic
# Create your views here.

def top(request):
    return render(request,
                  'cms/top.html')


def anken_list(request):
    """案件一覧"""
    # return HttpResponse('案件一覧')
    # ankens = Anken.objects.all().order_by('jutyu')
    ankens = Anken.objects.filter(archiveflag=False).order_by('kousinjikoku').reverse
    return render(request,
                  'cms/anken_list.html',
                  {'ankens': ankens})

def task(request):
    return render(request,
                  'cms/task.html')


def task_top(request):
    tasks = Task.objects.order_by('id').reverse
    return render(request,
                  'cms/task_top.html',
                  {'tasks': tasks})



def archiveanken_list(request):
    """過去案件一覧"""
    # return HttpResponse('案件一覧')
    # ankens = Anken.objects.all().order_by('jutyu')
    ankens = Anken.objects.filter(archiveflag=True).order_by('jutyu')
    return render(request,
                  'cms/archiveanken_list.html',
                  {'ankens': ankens})


def weekanken_list(request):
    """1週間案件一覧"""
    # return HttpResponse('案件一覧')
    # ankens = Anken.objects.all().order_by('jutyu')
    ankens = Anken.objects.filter(archiveflag=True).filter(kousinjikoku__icontains=date.today()).order_by('kousinjikoku').reverse
    # ankens = Anken.objects.filter(archiveflag=False).order_by('kousinjikoku').reverse


    return render(request,
                  'cms/weekanken_list.html',
                  {'ankens': ankens})


def anken_edit(request, anken_id=None):
    """案件の編集"""
    # return HttpResponse('案件の編集')
    if anken_id:
        anken = get_object_or_404(Anken, pk=anken_id)
    else:
        anken = Anken()

    if request.method == 'POST':
        form = AnkenForm(request.POST, instance=anken)
        if form.is_valid():
            anken = form.save(commit=False)
            anken.save()
            return redirect('cms:anken_list')
    else:
        form = AnkenForm(instance=anken)

    return render(request, 'cms/anken_edit.html', dict(form=form, anken_id=anken_id))


def anken_del(request, anken_id):
    """案件の削除"""
    # return HttpResponse('案件の削除')
    anken = get_object_or_404(Anken, pk=anken_id)
    anken.delete()
    return redirect('cms:anken_list')


def anken_archive(request, anken_id):
    """案件のアーカイブ"""
    anken = get_object_or_404(Anken, pk=anken_id)
    anken.archiveflag = True
    anken.save()
    return redirect('cms:anken_list')


def anken_archiveback(request, anken_id):
    """案件のアーカイブ"""
    anken = get_object_or_404(Anken, pk=anken_id)
    anken.archiveflag = False
    anken.save()
    return redirect('cms:anken_list')


class SintyokuList(ListView):
    context_object_name = 'sintyokus'
    template_name = 'cms/sintyoku_list.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        anken = get_object_or_404(Anken, pk=kwargs['anken_id'])
        sintyokus = anken.sintyokus.all().order_by('-kinyubi')
        self.object_list = sintyokus

        context = self.get_context_data(object_list=self.object_list, anken=anken)
        return self.render_to_response(context)



def sintyoku_edit(request, anken_id, sintyoku_id=None):
    """進捗の編集"""
    anken = get_object_or_404(Anken, pk=anken_id)  # 親の書籍を読む
    if sintyoku_id:   # impression_id が指定されている (修正時)
        sintyoku = get_object_or_404(Sintyoku, pk=sintyoku_id)
    else:               # impression_id が指定されていない (追加時)
        sintyoku = Sintyoku()

    if request.method == 'POST':
        form = SintyokuForm(request.POST, instance=sintyoku)      # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            sintyoku = form.save(commit=False)
            sintyoku.sintyoku = anken  # この感想の、親の書籍をセット
            sintyoku.save()
            anken.kousinjikoku = timezone.datetime.now()
            anken.save()
            return redirect('cms:sintyoku_list', anken_id=anken_id)
    else:    # GET の時
        form = SintyokuForm(instance=sintyoku)  # impression インスタンスからフォームを作成

    return render(request,
                  'cms/sintyoku_edit.html',
                  dict(form=form, anken_id=anken_id, sintyoku_id=sintyoku_id))


def sintyoku_del(request, anken_id, sintyoku_id):
    """感想の削除"""
    sintyoku = get_object_or_404(Sintyoku, pk=sintyoku_id)
    sintyoku.delete()
    return redirect('cms:sintyoku_list', anken_id=anken_id)


class TodoListView(generic.ListView):
    model = Todo
    paginate_by = 5


class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm



def task_edit(request, anken_id, task_id=None):
    """タスクの編集"""
    anken = get_object_or_404(Anken, pk=anken_id)  # 親の書籍を読む
    if task_id:   # task_id が指定されている (修正時)
        task = get_object_or_404(Task, pk=task_id)
    else:               # task_id が指定されていない (追加時)
        task = Task()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)      # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            task = form.save(commit=False)
            task.anken = anken  # この感想の、親の書籍をセット
            task.save()
            anken.kousinjikoku = timezone.datetime.now()
            anken.save()
            return redirect('cms:task', anken_id=anken_id)
    else:    # GET の時
        form = TaskForm(instance=task)  # impression インスタンスからフォームを作成

    return render(request,
                  'cms/task_edit.html',
                  dict(form=form, anken_id=anken_id, task_id=task_id))
