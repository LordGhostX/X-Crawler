from rest_framework.renderers import TemplateHTMLRenderer


class MyTemplateHTMLRenderer(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return {'data': data}