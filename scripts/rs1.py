from takeTest.models import Rquestion1
import csv


def run():
    with open('takeTest/rs1.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Rquestion1.objects.all().delete()

        for row in reader:
            print(row)
            x = Rquestion1(qn=row[0])
            x.save()