menu = [{'title': "About", 'url_name': 'about'},
        ]


class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}
    paginate_by=3

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context_data(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context
