from django.contrib import admin
from .models import (
    Profile, SkillCategory, Skill, Education, Project, 
    Achievement, Certification, Hobby, Contact
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone', 'linkedin', 'github', 'twitter', 'location')
    fieldsets = (
        (None, {
            'fields': ('name', 'role', 'introduction', 'career_objective', 'image', 'email', 'phone', 'linkedin', 'github', 'twitter', 'location')
        }),
    )
    search_fields = ['name', 'role', 'email']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category', 'proficiency']
    search_fields = ['name', 'category__name']
    ordering = ['category', 'order']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'cgpa', 'location']
    list_filter = ['start_date', 'end_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    ordering = ['-end_date', '-start_date']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'created_at']
    list_filter = ['status', 'featured', 'created_at']
    search_fields = ['title', 'description', 'tech_stack']
    ordering = ['-featured', '-created_at']
    prepopulated_fields = {'short_description': ('title',)}

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'achievement_type', 'organization', 'date']
    list_filter = ['achievement_type', 'date']
    search_fields = ['title', 'description', 'organization']
    ordering = ['-date']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'issue_date', 'expiry_date']
    list_filter = ['issue_date', 'expiry_date']
    search_fields = ['name', 'issuer', 'skills_covered']
    ordering = ['-issue_date']

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"
