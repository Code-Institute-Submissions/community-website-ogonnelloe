from django.shortcuts import render
from noticeboard.models import Notice
from django.views import generic, View
from .forms import NoticeForm


class AddNotice(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_notice.html',
            {"notice_added": False,
             "notice_form": NoticeForm()}
        )

    def post(self, request, *args, **kwargs):

        notice_form = NoticeForm(data=request.POST)

        print(notice_form)

        notice_form.save()

        # if notice_form.is_valid():
        #
        #
        # else:
        #     notice_form = NoticeForm()

        return render(
            request,
            "add_notice.html",
            {"notice_added": True,
             "notice_form": NoticeForm()}
        )

class Noticeboard(generic.ListView):

    model = Notice
    queryset = Notice.objects.filter(approved=True).order_by('created_on')
    template_name = 'noticeboard.html'
    paginate_by = 2
