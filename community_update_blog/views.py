from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import CommunityUpdate


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

        return render(
            request,
            template_name,
            {"post": post}
        )

# Static Pages


def plan_page(request):
    """ View to display 3 year plan page """
    return render(request, "3-year-plan.html")


def exchange_page(request):
    """ View to display exchange page """
    return render(request, "exchange.html")
