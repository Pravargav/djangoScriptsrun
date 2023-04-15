from takeTest.models import Question4
import csv


def run():
    with open('takeTest/ts4.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Question4.objects.all().delete()

        for row in reader:
            print(row)
            x = Question4(qn=row[0])
            x.save()