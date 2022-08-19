from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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
        template_name = 'community_update_detail.html'
        comments = post.community_update_comment.filter(approved=True).order_by('created_on')
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
        template_name = 'community_update_detail.html'
        comments = post.community_update_comment.filter(approved=True).order_by('created_on')
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

class CommunityUpdateLike(View):

    def post(self, request, slug):
        post = get_object_or_404(CommunityUpdate, slug = slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('community_update_detail', args=[slug]))

