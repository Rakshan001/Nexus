# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumni
from .forms import AlumniUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required
def alumni_profile(request):
    alumni = get_object_or_404(Alumni, user=request.user)
    
    if not alumni.is_alumni:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('home')

    return render(request, 'alumni_details/alumni-profile.html', {'alumni': alumni})

@login_required
def update_alumni_profile(request):
    alumni = get_object_or_404(Alumni, user=request.user)

    if not alumni.is_alumni:
        messages.error(request, "You are not authorized to update this profile.")
        return redirect('home')

    if request.method == 'POST':
        form = AlumniUpdateForm(request.POST, request.FILES, instance=alumni)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('alumni_profile')
    else:
        form = AlumniUpdateForm(instance=alumni)
    
    return render(request, 'alumni_details/update-alumni-profile.html', {'form': form, 'alumni': alumni})











# *****************************



from django.shortcuts import render, get_object_or_404
from .models import Alumni
import datetime

def alumni_list(request):
    current_year = datetime.datetime.now().year
    graduation_years = Alumni.objects.values_list('graduation_year', flat=True).distinct().order_by('-graduation_year')

    # Get alumni for the current year
    alumni_current_year = Alumni.objects.filter(graduation_year=current_year)[:5]

    # Get alumni for previous years
    alumni_previous_years = {}
    for year in graduation_years:
        if year < current_year:
            alumni_previous_years[year] = Alumni.objects.filter(graduation_year=year)[:5]

    return render(request, 'alumni_details/alumni_list.html', {
        'current_year': current_year,
        'alumni_current_year': alumni_current_year,
        'alumni_previous_years': alumni_previous_years,
        'graduation_years': graduation_years,
    })










from django.shortcuts import render, redirect
from .models import Alumni

def alumni_by_year(request, graduation_year):
    # Fetch all distinct branches for the filter dropdown
    branches = Alumni.objects.values_list('branch', flat=True).distinct()

    # Get the selected branch from the GET parameters (if any)
    selected_branch = request.GET.get('branch', '')

    # Check if the filter form was submitted for graduation year
    if 'graduation_year' in request.GET and request.GET['graduation_year']:
        graduation_year = int(request.GET.get('graduation_year'))
        return redirect('alumni_by_year', graduation_year=graduation_year)

    # If graduation_year is provided in the URL, fetch alumni for that year
    alumni = Alumni.objects.filter(graduation_year=graduation_year)

    # If a branch is selected, filter the alumni based on the selected branch
    if selected_branch:
        alumni = alumni.filter(branch=selected_branch)

    # Fetch all distinct graduation years for the filter dropdown
    graduation_years = Alumni.objects.values_list('graduation_year', flat=True).distinct()

    return render(request, 'alumni_details/alumni_by_year.html', {
        'alumni': alumni,
        'current_year': graduation_year,
        'graduation_years': graduation_years,
        'branches': branches,  # For the branch filter dropdown
        'selected_branch': selected_branch,  # To keep track of the selected branch
    })






# ********************************
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Alumni


def autocomplete(request):
    if 'term' in request.GET:
        qs = Alumni.objects.filter(first_name__icontains=request.GET.get('term'))|Alumni.objects.filter(last_name__icontains=request.GET.get('term'))  
        names = list()
        for alumni in qs:
            names.append(f"{alumni.first_name} {alumni.last_name}")
        return JsonResponse(names, safe=False)
    return render(request, 'alumni_details/search.html')

def alumni_search(request):
    query = request.GET.get('alumni', '')
    alumni_list = None
    if query:
        alumni_list = Alumni.objects.filter(first_name__icontains=query.split()[0], last_name__icontains=query.split()[-1])
    return render(request, 'alumni_details/alumni_search_results.html', {'alumni_list': alumni_list})