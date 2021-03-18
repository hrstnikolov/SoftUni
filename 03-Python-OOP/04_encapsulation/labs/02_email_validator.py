import re


class EmailValidator:
    __EMAIL_SPLIT_REGEX = r'[@.]'

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    # hidden methods / скрити методи
    # също така: методи на инстанцията, ползват селф
    # (не статик или клас)
    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    # public method / публичен метод (може да се достъпва отвън)
    # по-подходящо би било да се казва is_valid
    # при is_valid очакваме True/False
    # при глагол validate очкваме действие = да вдигне грешка
    def validate(self, email):
        (name, mail, domain) = re.split(EmailValidator.__EMAIL_SPLIT_REGEX, email)
        return self.__validate_name(name) \
               and self.__validate_mail(mail) \
               and self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
