from takeTest.models import Option1,Rquestion1
import csv


def run():
    with open('takeTest/rsop1.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Option1.objects.all().delete()
        i=1
        j=1
        for row in reader:
            print(row)
            
            q =Rquestion1.objects.get(pk=j)
            i=i+1
            if i%4==1:
              j=j+1
            q.option1_set.create(op=row[0])