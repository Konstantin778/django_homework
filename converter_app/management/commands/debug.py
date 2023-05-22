from django.core.management import BaseCommand

from converter_app.models import Converter, Currency, Settings




class Command(BaseCommand):
    help = 'Команда для дебага'

    def handle(self, *args, **options):
        # converter = Converter(name='app.currencyapi.com')
        # base_currency = Currency(id='RUB', value=1)
        # settings = Settings(base_currency=base_currency, converter=converter)
        # converter.save()
        # base_currency.save()
        # settings.save()
        # print('добавление успешно')

        currency = Currency(id='EUR', value=0.011616)
        currency.save()
        print('добавление успешно')
