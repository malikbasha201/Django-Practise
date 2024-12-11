from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def superstar(req):
    return HttpResponse('''<h1>Upcomig Movies:</h1>
                        <ol>
                            <li>GUNTURKARAM</li>
                            <li>SARKARU VARI PATA</li>
                            <li>SSMB RAJAMOULI</li>
                        </ol>    ''')
