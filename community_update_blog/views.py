from django.shortcuts import render
from django.views import generic
from .models import CommunityUpdate

class CommunityUpdateList(generic.ListView):
    model = CommunityUpdate
    queryset = CommunityUpdate.objects.filter(status=1).order_by('-created_on')
    template_name = 'community_updates.html'
    paginate_by = 3


class CommunityUpdatesMostRecent(generic.TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updates = CommunityUpdate.objects.filter(status=1).order_by('-created_on')
        context['recent_posts'] = updates[0:3]

        return context

# Static Pages


def plan_page(request):
    """ View to display 3 year plan page """
    return render(request, "3-year-plan.html")


def exchange_page(request):
    """ View to display exchange page """
    return render(request, "exchange.html")
