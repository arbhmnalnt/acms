from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    """
    A simple dashboard view that serves as the home page.
    Displays key metrics and shortcuts to other sections.
    """
    # You can compute or pass any data needed for the dashboard here.
    context = {
        'user': request.user,
        # Add other context variables as needed.
    }   
    return render(request, 'core/dashboard.html', context)
