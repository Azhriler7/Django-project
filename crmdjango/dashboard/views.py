from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from .forms import RecordForm

def home(request):
    records = Record.objects.all()
    return render(request, 'dashboard/dashboard.html', {'records': records})

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecordForm()
    return render(request, 'dashboard/create_record.html', {'form': form})

def view_record(request, id):
    record = get_object_or_404(Record, id=id)
    return render(request, 'dashboard/view_record.html', {'record': record})

def update_record(request, id):
    record = get_object_or_404(Record, id=id)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view_record', id=record.id)
    else:
        form = RecordForm(instance=record)
    return render(request, 'dashboard/update_record.html', {'form': form, 'record': record})

def delete_record(request, id):
    record = get_object_or_404(Record, id=id)
    if request.method == 'POST':
        record.delete()
        return redirect('home')
    return render(request, 'dashboard/delete_record.html', {'record': record})
