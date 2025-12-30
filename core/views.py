from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from .models import Project, Hobby, Profile
from .forms import ProjectForm, HobbyForm, ProfileForm

def home(request):
    return render(request, 'home.html')

# Project CRUD Views
def project_list(request):
    """List all projects with search, filter, and pagination"""
    projects = Project.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
    
    # Filter functionality
    filter_option = request.GET.get('filter', '')
    now = timezone.now()
    if filter_option == 'recent':
        # Last 7 days
        projects = projects.filter(created_at__gte=now - timedelta(days=7))
    elif filter_option == 'this_month':
        # This month
        projects = projects.filter(created_at__month=now.month, 
                                   created_at__year=now.year)
    elif filter_option == 'this_year':
        # This year
        projects = projects.filter(created_at__year=now.year)
    elif filter_option == 'oldest':
        # Order by oldest first
        projects = projects.order_by('created_at')
    elif filter_option == 'newest':
        # Order by newest first (default)
        projects = projects.order_by('-created_at')
    
    # Default ordering if no filter is applied
    if not filter_option:
        projects = projects.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(projects, 6)  # Show 6 projects per page
    page = request.GET.get('page', 1)
    
    try:
        projects_page = paginator.page(page)
    except PageNotAnInteger:
        projects_page = paginator.page(1)
    except EmptyPage:
        projects_page = paginator.page(paginator.num_pages)
    
    context = {
        'projects': projects_page,
        'search_query': search_query,
        'filter_option': filter_option,
    }
    return render(request, 'projects/project_list.html', context)

def project_detail(request, pk):
    """Display a single project"""
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)

def project_create(request):
    """Create a new project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    context = {
        'form': form,
        'title': 'Create New Project'
    }
    return render(request, 'projects/project_form.html', context)

def project_update(request, pk):
    """Update an existing project"""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    
    context = {
        'form': form,
        'project': project,
        'title': 'Update Project'
    }
    return render(request, 'projects/project_form.html', context)

def project_delete(request, pk):
    """Delete a project"""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    
    context = {
        'project': project
    }
    return render(request, 'projects/project_confirm_delete.html', context)

# Hobby CRUD Views
def hobby_list(request):
    """List all hobbies with search, filter, and pagination"""
    hobbies = Hobby.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        hobbies = hobbies.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
    
    # Filter functionality
    filter_option = request.GET.get('filter', '')
    now = timezone.now()
    if filter_option == 'recent':
        # Last 7 days
        hobbies = hobbies.filter(created_at__gte=now - timedelta(days=7))
    elif filter_option == 'this_month':
        # This month
        hobbies = hobbies.filter(created_at__month=now.month, 
                                created_at__year=now.year)
    elif filter_option == 'this_year':
        # This year
        hobbies = hobbies.filter(created_at__year=now.year)
    elif filter_option == 'oldest':
        # Order by oldest first
        hobbies = hobbies.order_by('created_at')
    elif filter_option == 'newest':
        # Order by newest first (default)
        hobbies = hobbies.order_by('-created_at')
    
    # Default ordering if no filter is applied
    if not filter_option:
        hobbies = hobbies.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(hobbies, 6)  # Show 6 hobbies per page
    page = request.GET.get('page', 1)
    
    try:
        hobbies_page = paginator.page(page)
    except PageNotAnInteger:
        hobbies_page = paginator.page(1)
    except EmptyPage:
        hobbies_page = paginator.page(paginator.num_pages)
    
    context = {
        'hobbies': hobbies_page,
        'search_query': search_query,
        'filter_option': filter_option,
    }
    return render(request, 'hobbies/hobby_list.html', context)

def hobby_detail(request, pk):
    """Display a single hobby"""
    hobby = get_object_or_404(Hobby, pk=pk)
    context = {
        'hobby': hobby
    }
    return render(request, 'hobbies/hobby_detail.html', context)

def hobby_create(request):
    """Create a new hobby"""
    if request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hobby created successfully!')
            return redirect('hobby_list')
    else:
        form = HobbyForm()
    
    context = {
        'form': form,
        'title': 'Create New Hobby'
    }
    return render(request, 'hobbies/hobby_form.html', context)

def hobby_update(request, pk):
    """Update an existing hobby"""
    hobby = get_object_or_404(Hobby, pk=pk)
    
    if request.method == 'POST':
        form = HobbyForm(request.POST, instance=hobby)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hobby updated successfully!')
            return redirect('hobby_detail', pk=hobby.pk)
    else:
        form = HobbyForm(instance=hobby)
    
    context = {
        'form': form,
        'hobby': hobby,
        'title': 'Update Hobby'
    }
    return render(request, 'hobbies/hobby_form.html', context)

def hobby_delete(request, pk):
    """Delete a hobby"""
    hobby = get_object_or_404(Hobby, pk=pk)
    
    if request.method == 'POST':
        hobby.delete()
        messages.success(request, 'Hobby deleted successfully!')
        return redirect('hobby_list')
    
    context = {
        'hobby': hobby
    }
    return render(request, 'hobbies/hobby_confirm_delete.html', context)

# Profile CRUD Views
def profile_list(request):
    """List all profiles"""
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'profiles/profile_list.html', context)

def profile_detail(request, pk):
    """Display a single profile"""
    profile = get_object_or_404(Profile, pk=pk)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile_detail.html', context)

def profile_create(request):
    """Create a new profile"""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('profile_list')
    else:
        form = ProfileForm()
    
    context = {
        'form': form,
        'title': 'Create New Profile'
    }
    return render(request, 'profiles/profile_form.html', context)

def profile_update(request, pk):
    """Update an existing profile"""
    profile = get_object_or_404(Profile, pk=pk)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'form': form,
        'profile': profile,
        'title': 'Update Profile'
    }
    return render(request, 'profiles/profile_form.html', context)

def profile_delete(request, pk):
    """Delete a profile"""
    profile = get_object_or_404(Profile, pk=pk)
    
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('profile_list')
    
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile_confirm_delete.html', context)
