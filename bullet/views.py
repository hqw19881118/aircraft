# coding=utf-8
# Create your views here.
import os
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q, Sum
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from bullet.models import BulletInfo

BULLET_TEMPLATES_DIR = os.path.join('bullet', 'templates')


class BulletListView(ListView):
    model = BulletInfo
    template_name = os.path.join(BULLET_TEMPLATES_DIR, 'bulletinfo_list.html')
    # paginate_by = 2

    def get_queryset(self):
        # # 模糊匹配
        made_in = self.request.GET.get('made_in', '')
        return BulletInfo.objects.filter(made_in__contains=made_in)

        # # 精确匹配
        # made_in = self.request.GET.get('made_in')
        # if made_in:
        #     return BulletInfo.objects.filter(made_in=made_in)
        # else:
        #     return BulletInfo.objects.all()

        # 多条件精确匹配
        # made_in = self.request.GET.get('made_in')
        # bullet_price = self.request.GET.get("bullet_price")
        # arg_dict = {'made_in': made_in, 'bullet_price__gte': bullet_price}
        # kwargs = {}
        # for k, v in arg_dict.iteritems():
        #     if not v:
        #         kwargs[k] = v
        # return BulletInfo.objects.filter(**kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(BulletListView, self).get_context_data(**kwargs)
    #     made_in = self.request.GET.get('made_in', '')
    #     context['made_in'] = made_in
    #     return context


class BulletCreateView(CreateView):
    model = BulletInfo
    success_url = reverse_lazy('bullet-list')
    template_name = os.path.join(BULLET_TEMPLATES_DIR, 'bulletinfo_form.html')


class BulletUpdateView(UpdateView):
    model = BulletInfo
    success_url = reverse_lazy('bullet-list')
    template_name = os.path.join(BULLET_TEMPLATES_DIR, 'bulletinfo_update_form.html')


class BulletDeleteView(DeleteView):
    model = BulletInfo
    success_url = reverse_lazy('bullet-list')
    template_name = os.path.join(BULLET_TEMPLATES_DIR, 'bulletinfo_confirm_delete.html')


