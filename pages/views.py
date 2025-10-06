from django.shortcuts import render
from datetime import date

# Sample data (no database yet)
announcements = [
    {"id": 1, "title": "Midterm Exam Schedule", "content": "The midterm exams will start next week. Please check your subjects for the specific schedule.", "date_posted": date(2025, 10, 5)},
    {"id": 2, "title": "New Library Books Arrived", "content": "We have added new reference materials in the library. Visit and borrow anytime.", "date_posted": date(2025, 10, 3)},
]

def home(request):
    return render(request, 'pages/home.html')

def announcement_list(request):
    return render(request, 'pages/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = next((a for a in announcements if a["id"] == id), None)
    return render(request, 'pages/announcement_detail.html', {'announcement': announcement})

