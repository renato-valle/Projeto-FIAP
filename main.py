import datetime
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from service.autor_service import AutorService
from service.livro_service import LivroService


categoria_service = CategoriaService()
editora_service = EditoraService()
autor_service = AutorService()
livro_service = LivroService(categoria_service.categoria_dao, editora_service.editora_dao, autor_service.autor_dao)


def getDate(a):
    now = datetime.datetime.now() + datetime.timedelta(days=a)
    return now.strftime('%d') + '-' + now.strftime('%m') + '-' + now.strftime('%Y')


def menu_principal():
    print('')
    print("********************************************************************")
    print('                      LIBRARY MANAGEMENT SYSTEM                     ')
    print("Data: ",getDate(0))
    print("********************************************************************")
    print('')
    print('[Menu Principal] Escolha uma das seguintes opções:\n'
            '1 - Categorias\n'
            '2 - Editoras\n'
            '3 - Autores\n'
            '4 - Livros\n'
            '0 - Sair do programa\n')

    escolha = input('Digite a opção: ')

    if escolha == '0':
        print('Obrigado, até logo!')
        return
    elif escolha == '1':
        categoria_service.menu()
    elif escolha == '2':
        editora_service.menu()
    elif escolha == '3':
        autor_service.menu()
    elif escolha == '4':
        if len(categoria_service.categoria_dao.listar()) > 0 and \
            len(editora_service.editora_dao.listar()) > 0 and \
            len(autor_service.autor_dao.listar()) > 0:
            livro_service.menu()
        else:
            print('É necessário ter ao menos uma categoria, uma editora e um autor cadastrado!')

    else:
        print('Opção inválida! Por favor, tente novamente.')

    menu_principal()


if __name__ == '__main__':
    menu_principal()
