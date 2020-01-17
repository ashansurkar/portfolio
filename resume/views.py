from django.shortcuts import render
from .models import resume
# Create your views here.
def res_display(request):
    res = resume.objects.first()
    print(res)
    # field_obj = resume._meta.get_fields('file')
    # print(field_obj.value_from_object(res))
    # pdf_res = pdf_view(res.file)
    return render(request,'resumes/resume.html',{'res':res})

def pdf_view(file):
    with open(file, 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed
