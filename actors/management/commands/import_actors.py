from datetime import datetime
import pandas as pd
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        dataframe = pd.read_csv(file_name)

        for _, row in dataframe.iterrows():
            name = row['name']
            birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
            nationality = row['nationality']

            self.stdout.write(self.style.NOTICE(name))

            Actor.objects.create(
                name=name,
                birthday=birthday,
                nationality=nationality,
            )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))
