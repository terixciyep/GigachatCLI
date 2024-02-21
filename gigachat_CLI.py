"""Пример работы с чатом через gigachain"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import AUTHORIZATION

def start_cli(data):
    chat = GigaChat(credentials=f'{AUTHORIZATION}', verify_ssl_certs=False)

    messages = [(SystemMessage(
        content=f"""Ты бот-справочник по информации о компании, их достижений и успешных примеров их деятельности.
            Названия кейсов и ссылки для них находятся в списке с множествами: {data}, можешь брать различные из них и использовать в своих ответах.
            Компания называется EORA, мы применяем мышинное обучение для внедрения в различный бизнес.
            Пример вопроса 1: Какие успешные кейсы вы имеете?
            Пример ответа 1: Например, мы создали {data[0][1]} Источник {data[0][0]}
            Пример вопроса 2: Назови пару успешных кейсов компании.
            Пример ответа 2: Например, мы создали {data[1][1]},, а так же {data[2][1]} Источники {data[1][0]}, {data[2][0]}
            Пример вопроса 3: С какими технологиями вы работаете?
            Пример ответа 3: Наша компания занимается внедрением Data science в бизнес-задачи, например, мы создали {data[3][1]} или {data[4][1]}.Источники {data[3][0]},{data[4][0]}.
            В конце своих ответов ты даешь ссылки на упомянутые тобою кейсы. Они содержатся в тех же множествах, что и сами названия кейсов.
            Пример: Источники (перечисление источников){data[0][0]}. 
            Ограничь количество упомянутых кейсов до 2 штук.           
            """
    ))]

    while(True):
        user_input = input("User: ")
        messages.append(HumanMessage(content=user_input))
        res = chat(messages)
        messages.append(res)
        print("Bot: ", res.content)