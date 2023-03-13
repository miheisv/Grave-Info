from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView  # , CreateView
from .models import Human


class HomeView(ListView):
    template_name = 'homepage/homepage.html'
    model = Human
    context_object_name = 'humans'
    paginate_by = 20

    def get_queryset(self):
        post_to_view = Human.objects.select_main()
        return post_to_view


class DetailView(DetailView):
    model = Human
    template_name = 'homepage/post.html'
    context_object_name = 'human'

    def get_object(self):
        return get_object_or_404(Human, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
