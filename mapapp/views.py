from django.shortcuts import render

# Create your views here.
# mapapp/views.py
import json
from django.shortcuts import render


def index(request):
    # Example data - replace with your actual data
    data = [
        {'lat': 51.505, 'lon': -0.09, 'name': 'Location 1'},
        {'lat': 51.515, 'lon': -0.1, 'name': 'Location 2'},
        {'lat': 51.525, 'lon': -0.11, 'name': 'Location 3'}
    ]

    # Convert Python object (list of dictionaries) to JSON
    json_data = json.dumps(data)

    return render(request, 'mapapp/index.html', {'data': json_data})
