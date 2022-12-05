import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
)


MENU_DISPLAY = (
    "Selecione uma das opções a seguir:\n "
    "0 - Popular o banco com notícias;\n "
    "1 - Buscar notícias por título;\n "
    "2 - Buscar notícias por data;\n "
    "3 - Buscar notícias por tag;\n "
    "4 - Buscar notícias por categoria;\n "
    "5 - Listar top 5 notícias;\n "
    "6 - Listar top 5 categorias;\n "
    "7 - Sair.\n "
)

OPTIONS = [
    "Digite quantas notícias serão buscadas: ",
    "Digite o título: ",
    "Digite a data no formato aaaa-mm-dd: ",
    "Digite a tag: ",
    "Digite a categoria: "
]


# def populate_database(amount):
#     return get_tech_news(amount)


FUNCTIONS = [
    get_tech_news,
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
    top_5_news,
    top_5_categories
]


def menu_caller(option):
    if len(OPTIONS) > option:
        option2 = input(OPTIONS[option])
        return FUNCTIONS[option](option2)

    return FUNCTIONS[option]()


# Requisito 12:
def analyzer_menu():
    try:
        option = int(input(MENU_DISPLAY))

        if option in range(0, 7):
            return menu_caller(option)
        elif option == 7:
            print("Sair.")
        else:
            raise ValueError("Opção inválida")
    except ValueError as e:
        print(str(e), file=sys.stderr)
