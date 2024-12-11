from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def powerstar(req):
    return HttpResponse('''<h1>Upcomig Movies:</h1>
                        <ol>
                            <li>HARIHARAVEERAMALLU</li>
                            <li>ORIGINAL GANGSTER</li>
                            <li>USTAAD BHAGATH SINGH</li>
                        </ol>    ''')
