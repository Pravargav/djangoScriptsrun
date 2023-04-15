from takeTest.models import Question3
import csv


def run():
    with open('takeTest/ts3.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Question3.objects.all().delete()

        for row in reader:
            print(row)
            x = Question3(qn=row[0])
            x.save()