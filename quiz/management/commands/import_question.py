# your_project/your_app/management/commands/import_questions.py
from django.core.management.base import BaseCommand
from quiz.models import Question
import pandas as pd

class Command(BaseCommand):
    help = 'Import questions from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path of the Excel file')
        parser.add_argument('question_type', type=int, help='The kind of question: \
                                                             1: basic computer knowledge \
                                                             2: basic CPC history knowledge \
                                                             3: basic blood donation knowledge')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        question_kind = kwargs['question_type']
        category = ''
        if question_kind == 1:
            category = 'computer'
        elif question_kind == 2:
            category = 'blood'
        else:
            category = 'party'

        df = pd.read_excel(file_path)
        print(df)
        for index, row in df.iterrows():
            print(index)
            print(row)
            question = row['问题']
            option_a = row['选项A']
            option_b = row['选项B ']
            option_c = row['选项C']
            option_d = row['选项D']
            answer = row['答案']
            Question.objects.create(
                text=question,
                category = category,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                answer=answer
            )
        self.stdout.write(self.style.SUCCESS('Questions imported successfully.'))
