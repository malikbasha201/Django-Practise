from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chennai(req):
    return HttpResponse('''<h1>Team Players List:</h1>
    <ol>
        <li>Ruturaj Gaikwad</li>
        <li>Devon Convey</li>
        <li>Rachin Ravindra</li>
        <li>Shivam Dubey</li>
        <li>MS Dhoni</li>
        <li>Ravindra Jadeja</li>
        <li>Ravichandran Ashwin</li>
        <li>Deepak Chahar</li>
        <li>Matheesha Pathirana</li>
        <li>Noor Ahmed</li>
        <li>Khaleel Ahmed</li>
                        
                        ''')