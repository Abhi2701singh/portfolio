from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import (
    Profile, Skill, SkillCategory, Education, Project, 
    Achievement, Certification, Hobby, Contact
)
from .forms import ContactForm

def home(request):
    """Home page view"""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_achievements = Achievement.objects.all()[:3]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'recent_achievements': recent_achievements,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    profile = Profile.objects.first()
    
    context = {
        'profile': profile,
    }
    return render(request, 'main/about.html', context)

def skills(request):
    """Skills page view"""
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    
    # Calculate statistics
    total_skills = 0
    total_proficiency = 0
    skill_count = 0
    
    for category in skill_categories:
        for skill in category.skills.all():
            total_skills += 1
            total_proficiency += skill.proficiency
            skill_count += 1
    
    avg_proficiency = round(total_proficiency / skill_count) if skill_count > 0 else 0
    
    # Calculate circular progress values for skills
    for category in skill_categories:
        for skill in category.skills.all():
            # Calculate stroke-dasharray for circular progress
            # Circumference = 2 * π * radius (54px radius)
            # stroke-dasharray = (proficiency * circumference / 100) circumference
            circumference = 2 * 3.14159 * 54  # 339.292
            skill.stroke_dasharray = (skill.proficiency * circumference / 100)
    
    context = {
        'skill_categories': skill_categories,
        'total_skills': total_skills,
        'avg_proficiency': avg_proficiency,
    }
    return render(request, 'main/skills.html', context)

def education(request):
    """Education page view"""
    education_list = Education.objects.all()
    
    context = {
        'education_list': education_list,
    }
    return render(request, 'main/education.html', context)

def projects(request):
    """Projects page view"""
    projects_list = Project.objects.all()
    
    # Filtering
    status_filter = request.GET.get('status')
    if status_filter:
        projects_list = projects_list.filter(status=status_filter)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        projects_list = projects_list.filter(
            title__icontains=search_query
        ) | projects_list.filter(
            description__icontains=search_query
        ) | projects_list.filter(
            tech_stack__icontains=search_query
        )
    
    # Pagination
    paginator = Paginator(projects_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'search_query': search_query,
    }
    return render(request, 'main/projects.html', context)

def achievements(request):
    """Achievements page view"""
    achievements_list = Achievement.objects.all()
    
    # Filtering by type
    type_filter = request.GET.get('type')
    if type_filter:
        achievements_list = achievements_list.filter(achievement_type=type_filter)
    
    context = {
        'achievements_list': achievements_list,
        'type_filter': type_filter,
    }
    return render(request, 'main/achievements.html', context)

def certifications(request):
    """Certifications page view"""
    certifications_list = Certification.objects.all()
    
    context = {
        'certifications_list': certifications_list,
    }
    return render(request, 'main/certifications.html', context)

def hobbies(request):
    """Hobbies page view"""
    hobbies_list = Hobby.objects.all()
    
    context = {
        'hobbies_list': hobbies_list,
    }
    return render(request, 'main/hobbies.html', context)

def contact(request):
    """Contact page view"""
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message to database
            contact = form.save()
            
            # Send email notification
            try:
                # Prepare email context
                context = {
                    'name': contact.name,
                    'email': contact.email,
                    'message': contact.message,
                    'created_at': contact.created_at.strftime('%B %d, %Y at %I:%M %p')
                }
                
                # Render email template
                email_html = render_to_string('main/email/contact_message.html', context)
                
                # Debug: Print email settings
                print(f"Email settings:")
                print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
                print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
                print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
                print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
                
                # Send email
                send_mail(
                    subject=f'New Contact Message from {contact.name}',
                    message=f'''
Name: {contact.name}
Email: {contact.email}
Message: {contact.message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Send to yourself
                    html_message=email_html,
                    fail_silently=False,
                )
                
                messages.success(request, 'Thank you for your message! I will get back to you soon.')
                
            except Exception as e:
                # If email fails, still save to database but show warning
                messages.warning(request, f'Message saved but email notification failed. Error: {str(e)}')
                print(f"Email error details: {e}")
                import traceback
                traceback.print_exc()
            
            return redirect('main:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'main/contact.html', context)
