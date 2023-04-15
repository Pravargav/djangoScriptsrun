from takeTest.models import Option2,Rquestion2
import csv


def run():
    with open('takeTest/rsop2.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Option2.objects.all().delete()
        i=1
        j=1
        for row in reader:
            print(row)
            
            q =Rquestion2.objects.get(pk=j)
            i=i+1
            if i%4==1:
              j=j+1
            q.option2_set.create(op=row[0])