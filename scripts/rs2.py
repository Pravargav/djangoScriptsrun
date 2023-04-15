from takeTest.models import Rquestion2
import csv


def run():
    with open('takeTest/rs2.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Rquestion2.objects.all().delete()

        for row in reader:
            print(row)
            x = Rquestion2(qn=row[0])
            x.save()