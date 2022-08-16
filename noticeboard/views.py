from django.shortcuts import render
from noticeboard.models import Notice
from django.views import generic, View
from django.views.generic.edit import DeleteView, UpdateView
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

        if notice_form.is_valid():
            notice_form.instance.creator = request.user.username
            notice_form.save()
        else:
            notice_form = NoticeForm()

        return render(
            request,
            "noticeboard.html",
            {"notice_added": True,
             "notice_form": NoticeForm()}
        )

class DeleteNotice(DeleteView):

    model = Notice

    success_url = "/noticeboard"

    template_name = "notice_confirm_delete.html"

class UpdateNotice(UpdateView):
     model = Notice
     fields = ['title', 'description', 'contact_number', 'contact_email', 'location', 'background_image']
     template_name = 'notice_update_form.html'
     success_url = "/noticeboard"


class Noticeboard(generic.ListView):

    model = Notice
    queryset = Notice.objects.filter(approved=True).order_by('created_on')
    template_name = 'noticeboard.html'
    paginate_by = 2