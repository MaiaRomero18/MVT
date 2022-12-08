from django.shortcuts import render
from app_MVT.models.familiar import familiar
import datetime

class familiar_View:
    def autogenerar_listar_familiares(request):
        fm1 = familiar.create('Gloria','Almonte','73','glogloalmonte@gmail.com','01161842635',datetime.date(1949, 6, 29))
        fm2 = familiar.create('Claudia','Figueroa','42','claudiafigueroa@gmail.con','01136023514', datetime.date(1982, 3, 14))
        fm3 = familiar.create('Gabriel', 'Carpio', '38', 'carpiogabriel@gmail.con', '01155654863', datetime.date(1989, 6, 12))
    
        fm1.save()
        fm2.save()
        fm3.save()
        return render(request, 'autogenerador_listar_fammiliares.html', {'familiares': [fm1, fm2, fm3]})