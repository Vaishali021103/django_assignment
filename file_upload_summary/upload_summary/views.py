import pandas as pd
from django.core.mail import send_mail
from .forms import UploadFileForm
import os
from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            summary_report = generate_summary_report(file_path)
            send_summary_email(summary_report)
    else:
        form = UploadFileForm()
    return render(request, 'upload_summary/upload_file.html', {'form': form})

def handle_uploaded_file(file):
    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, file.name)
    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path

def generate_summary_report(file_path):
    import pandas as pd
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Logic to group by 'Cust State' and 'DPD' and count occurrences
    summary_report = df.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')  
    
    # Convert DataFrame to tab-separated string
    summary_report_str = summary_report.to_string(index=False, sep='\t')
    
    return summary_report_str

def send_summary_email(summary_report):
    subject = 'Python Assignment - Vaishali'
    message = summary_report
    sender = 'vaishalisirimalla@example.com'  x
    recipient_list = ['sirimallavaishali7@gmail.com', 'harsh.sarda@somaiya.edu']
    send_mail(subject, message, sender, recipient_list)