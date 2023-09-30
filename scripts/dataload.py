from takeTest.models import Question
import csv


def run():
    with open('takeTest/data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

    
        Question.objects.all().delete()

        for row in reader:
            print(row)
            x = Question(qn=row[0])
            x.save()