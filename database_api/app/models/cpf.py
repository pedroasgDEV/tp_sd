import random

class Cpf:
    def __init__(self, cpf="NOCPF"):
        if cpf == "NOCPF": self.cpf = self.generate_cpf()
        else: self.cpf = cpf
        self.description = self.__str__()

    def generate_cpf(self):
        cpf = [random.randint(0, 9) for _ in range(9)]
        cpf.append(self.calculate_digit(cpf))
        cpf.append(self.calculate_digit(cpf))
        return ''.join(map(str, cpf))

    def calculate_digit(self, cpf):
        length = len(cpf)
        sum_ = sum(cpf[i] * (length + 1 - i) for i in range(length))
        remainder = sum_ % 11
        return 0 if remainder < 2 else 11 - remainder

    def __str__(self):
        cpf_str = ''.join(map(str, self.cpf))
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"