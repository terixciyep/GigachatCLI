from gigachat_CLI import start_cli
from parsing import pars_cases

url = 'https://eora.ru/cases'

if __name__ == "__main__":
    data = pars_cases(url)
    start_cli(data)
