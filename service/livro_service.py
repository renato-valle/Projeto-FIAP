from dao.livro_dao import LivroDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.autor_dao import AutorDAO
from model.livro import Livro


class LivroService:
    def __init__(self, categoria_dao: CategoriaDAO, editora_dao: EditoraDAO, autor_dao: AutorDAO) -> None:
        self.__livro_dao: LivroDAO = LivroDAO()
        self.__categoria_dao: CategoriaDAO = categoria_dao
        self.__editora_dao: EditoraDAO = editora_dao
        self.__autor_dao: AutorDAO = autor_dao

    def menu(self):
        print("""[Livros] Escolha uma das seguintes opções:
              1 - Listar todos os livros
              2 - Adicionar novo livro
              3 - Excluir livro
              4 - Ver livro por Id
              0 - Voltar ao menu anterior """)

        escolha = input('Digite a opção: ')
        if escolha == '0':
            return
        elif escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando livros...')

        try:
            livros = self.__livro_dao.listar()
            if len(livros) == 0:
                print('Nenhum livro encontrado!')
            else:
                for livro in livros:
                    print(livro)
        except Exception as e:
            print(f'Erro ao exibir os livros: {e}')

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando livro...')

        try:
            id = self.__livro_dao.ultimo_id() + 1
            titulo = input('Digite o titulo do livr: ')
            resumo = input('Digite o resumo do livro: ')
            ano = int(input('Digite o ano do livro: '))
            paginas = int(input('Digite a quantidade de páginas do livro: '))
            isbn = input('Digite o ISBN do livro: ')

            print('Categorias de livro:')

            lista_categorias = self.__categoria_dao.listar()
            for cat in lista_categorias:
                print(cat)

            id_categoria = int(input('Digite o ID da categoria do livro: '))
            categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            while categoria == None:
                print('Categoria inexistente!')
                id_categoria = int(input('Digite o ID da categoria do livro: '))
                categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            print('Editoras de livro:')

            lista_editoras = self.__editora_dao.listar()
            for ed in lista_editoras:
                print(ed)

            id_editora = int(input('Digite o ID da editora do livro: '))

            editora = self.__editora_dao.buscar_por_id(id_editora)

            while editora == None:
                print('Editora inexistente!')
                id_editora = int(input('Digite o ID da editora do livro: '))
                editora = self.__editora_dao.buscar_por_id(id_editora)

            print('Autores de Livro:')

            lista_autores = self.__autor_dao.listar()
            for aut in lista_autores:
                print(aut)

            id_autor = int(input('Digite o ID do autor do livro: '))
            autor = self.__autor_dao.buscar_por_id(id_autor)

            while autor == None:
                print('Autor inexistente!')
                id_autor = int(input('Digite o ID do autor do livro: '))
                autor = self.__autor_dao.buscar_por_id(id_autor)

            novo_livro = Livro(id, titulo, resumo, ano, paginas, isbn, categoria, editora, autor)

            self.__livro_dao.adicionar(novo_livro)
            print('Livro adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir novo livro: {e}')

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo livro...')

        try:
            livro_id = int(input('Digite o ID do livro para excluir: '))
            if self.__livro_dao.remover(livro_id):
                print('Livro excluído com sucesso!')
            else:
                print('Livro não encontrado!')
        except Exception as e:
            print(f'Erro ao excluir livro: {e}')

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nLivro por Id...')

        try:
            livro_id = int(input('Digite o ID do livro para buscar: '))
            livro = self.__livro_dao.buscar_por_id(livro_id)

            if livro == None:
                print('Livro não encontrado!')
            else:
                print(livro)
        except Exception as e:
            print(f'Erro ao exibir livro: {e}')

        input('Pressione uma tecla para continuar...')
