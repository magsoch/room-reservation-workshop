from django.shortcuts import render, redirect
from core.models import Room
from django.views import View

# Create your views here.
def room_new_view(request):
    if request.method == "POST":
        name = request.POST['name']
        capacity = int(request.POST['capacity'])
        has_projector = bool(request.POST.get('has_projector'))
        room = Room.objects.create(name=name,
                                   capacity=capacity,
                                   has_projector=has_projector)
        return redirect('room/{}'.format(room.id))
    else:
        return render(request, 'room_new.html')

def room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def room_detail_view(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'room.html', {'room': room})

class RoomModifyView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'room_edit.html', {'room': room})
    def post(self, request, id):
        room = Room.objects.get(id=id)
        room.name = request.POST['name']
        room.capacity = int(request.POST['capacity'])
        room.has_projector = bool(request.POST.get('has_projector'))
        room.save()
        return redirect('/room/{}'.format(room.id))

class RoomDeleteView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'room_delete.html', {'room': room})
    def post(self, request, id):
        room = Room.objects.get(id=id)
        room.delete()
        return redirect('/')

