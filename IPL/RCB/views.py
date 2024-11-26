from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rcb(req):
    return HttpResponse('''<h1>Team Players List:</h1>
    <ol>
        <li>Virat Kohli</li>
        <li>Phil Salt</li>
        <li>Rajat Patidar</li>
        <li>Liam Livingstone</li>
        <li>Yash Dayal</li>
        <li>Suyash</li>
        <li>Jitesh Sharma</li>
        <li>Josh Hazelwood</li>
        <li>FaF Duplessis</li>
        <li>Mohammed Siraj</li>
        <li>Mahipol Lamror</li>
                        
                        ''')