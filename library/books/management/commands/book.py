from lib2to3.pytree import Base
from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os


class Command(BaseCommand):
    help = "Populates the database with books"

    def handle(self, *args, **options):
        current_path = os.path.dirname(__file__)
        file_path = os.path.join(current_path, "books_book.sql")
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            cursor.execute(sql)
