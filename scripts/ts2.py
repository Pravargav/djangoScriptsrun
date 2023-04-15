from takeTest.models import Question2
import csv


def run():
    with open('takeTest/ts2.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Question2.objects.all().delete()

        for row in reader:
            print(row)
            x = Question2(qn=row[0])
            x.save()