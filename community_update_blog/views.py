from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import CommunityUpdate
from .forms import CommentForm


class CommunityUpdatesMostRecent(generic.TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updates = CommunityUpdate.objects.filter(status=1).order_by('-created_on')
        context['recent_posts'] = updates[:3]

        return context


class CommunityUpdateList(generic.ListView):

    model = CommunityUpdate
    queryset = CommunityUpdate.objects.filter(status=1).order_by('-created_on')
    template_name = 'community_update_list.html'
    paginate_by = 3

class CommunityUpdateDetail(View):

    def get(self, request, slug, **kwargs):
        queryset = CommunityUpdate.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.community_update_comment.filter(approved=True).order_by('created_on')
        template_name = 'community_update_detail.html'
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            template_name,
            {"post": post,
             "comments": comments,
             "commented": False,
             "liked": liked,
             "comment_form": CommentForm()}
        )

    def post(self, request, slug, **kwargs):
        queryset = CommunityUpdate.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.community_update_comment.filter(approved=True).order_by('created_on')
        template_name = 'community_update_detail.html'
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.commenter = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            template_name,
            {"post": post,
             "comments": comments,
             "commented": True,
             "liked": liked,
             "comment_form": CommentForm()}
        )


# Static Pages


def plan_page(request):
    """ View to display 3 year plan page """
    return render(request, "3-year-plan.html")


def exchange_page(request):
    """ View to display exchange page """
    return render(request, "exchange.html")
