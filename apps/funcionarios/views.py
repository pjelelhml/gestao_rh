import io

from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from django.views.generic.base import View, TemplateView
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa



from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_button'] = _("Employee report")
        return context

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatorio de funcionarios')

    funcionarios = Funcionario.objects.filter(
        empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s | Hora Extra: %.2f'

    p.drawString(0, 800, '_' * 150)

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (
            funcionario.nome, funcionario.total_horas_extra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')


class PdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio.html'

def relatorio_funcionarios(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    p.drawString(200, 200, "Ol?? mundo")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')


class PdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio.html'
