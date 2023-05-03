from django.core.management.base import BaseCommand, CommandParser
from loveRelay.models import Gift
import pandas as pd

class Command(BaseCommand):
    help = 'Import gifts from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help='Path of the Excel file.')
        
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        df = pd.read_excel(file_path)
        print(df)

        for index, row in df.iterrows():
            gift_name = row['项目']
            remain_num = row['数量']
            single_price = row['单价']

            Gift.objects.create(
                name = gift_name,
                remain_num = remain_num,
                price = single_price
            )

            print("Gift add: (%s, %d, %f)" %(gift_name, remain_num, single_price))
        
        self.stdout.write(self.style.SUCCESS("Gift imported successfully."))