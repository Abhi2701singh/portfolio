from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    introduction = models.TextField()
    career_objective = models.TextField()
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profile"

class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, blank=True)  # For FontAwesome icons
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    proficiency = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Skill proficiency level (1-100)"
    )
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        ordering = ['category', 'order']

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=100)
    key_coursework = models.TextField(help_text="Enter key coursework separated by commas")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

    class Meta:
        ordering = ['-end_date', '-start_date']

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('planned', 'Planned'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    tech_stack = models.TextField(help_text="Enter technologies separated by commas")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

class Achievement(models.Model):
    TYPE_CHOICES = [
        ('hackathon', 'Hackathon'),
        ('competition', 'Competition'),
        ('arts', 'Arts'),
        ('academic', 'Academic'),
        ('leadership', 'Leadership'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    achievement_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateField()
    organization = models.CharField(max_length=200)
    certificate_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='achievements/', null=True, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date', 'order']
        verbose_name_plural = "Achievements"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    skills_covered = models.TextField(help_text="Enter skills covered separated by commas")
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    certificate_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certifications/', null=True, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.issuer}"

    class Meta:
        ordering = ['-issue_date', 'order']

class Hobby(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hobbies"
        ordering = ['order']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-created_at']
