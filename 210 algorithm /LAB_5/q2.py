# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10UuSfNgGEUm8rLN1-HOpFXrA0EkxMTkP
"""

Act = ["Silent Disco","Bonfire","Street Play","Dancing Competition","Short Film Screening",
    "Rangoli","Scanvenger Hunt","Face Art","Solo Music","Group Music","Mime","Poetry Recitation"]

DL = [12,12,2,8,10,4,4,4,7,7,11,2]
Dur = [2,2,1,1,0.5,0.5,1.5,0.5,0.5,1,1,1]

Sch = dict(zip(Act, list(zip(Dur,DL))))
print(Sch)
def scheduler(Sch):
    sorted_Sch = {k: v for k, v in sorted(Sch.items(), key=lambda item: item[1][1])}
    schedule = []
    curr_time = 0
    penal = 0
    for i,j in sorted_Sch.items():
        schedule.append(i)
        print(j[1], curr_time+j[0])
        if j[1] <= j[0]+curr_time:
            penal+=50000*(curr_time-j[1])
        curr_time+=j[0]
    return schedule, abs(penal)

final, p= scheduler(Sch)
print(final)
print(p)