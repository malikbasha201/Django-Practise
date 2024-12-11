from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def srh(req):
    return HttpResponse('''<h1>Team Players List:</h1>
    <ol>
        <li>Travis Head</li>
        <li>Abisehk Sahrma</li>
        <li>Ishan Kishan</li>
        <li>Henrich Klaseen</li>
        <li>Nitish Kumar </li>
        <li>Pat Cummins</li>
        <li>Mohamme Shami</li>
        <li>Harshal Patel</li>
        <li>Adam Zampa</li>
        <li>Buvaneshwar</li>
        <li>Ben Cutting</li>
                        
                        ''')
