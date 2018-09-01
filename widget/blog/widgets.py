from django import forms


class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'


class AutoCompleteSelect(forms.Select):
    template_name = 'widgets/autocomplete_select.html'

    class Media:
        css = {
            'all': [
                '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css',

            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs);
        context['style'] = 'min-width: 200px;'
        return context

    def __init__(self, ajax_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ajax_url = ajax_url

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['ajax_url'] = self.ajax_url
        return context

    def optgroups(self, name, value, attrs=None):
        existed_ids = [_id for _id in value if _id]
        self.choices.queryset = self.choices.queryset.filter(id__in=existed_ids)
        return super().optgroups(name, value, attrs=None)


class RateitjsWidget(forms.NumberInput):
    input_type = 'rating'
    template_name = 'widgets/rateitjs_number.html'

    class Media:
        css = {
            'all': [
                'widgets/rateit.js/rateit.css'
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'widgets/rateit.js/jquery.rateit.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({
            'min': '0',
            'max': 5,
            'step': 1,
        })
        return attrs
