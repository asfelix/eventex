from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Alexsandro Felix', cpf='12345678901',
                    email='eventex.to@ffelix.eti.br', phone='45-99999-9999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'eventex.from@ffelix.eti.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['eventex.from@ffelix.eti.br', 'eventex.to@ffelix.eti.br']


        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Alexsandro Felix',
            '12345678901',
            'eventex.to@ffelix.eti.br',
            '45-99999-9999'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
