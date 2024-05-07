class MenuService:
    def menu(self, tipo_objeto: str):
        print(f"""[{tipo_objeto}s] Escolha uma das seguintes opções:
              1 - Listar {tipo_objeto}s
              2 - Adicionar {tipo_objeto}
              3 - Excluir {tipo_objeto}
              4 - Ver {tipo_objeto} por Id
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

        self.menu(tipo_objeto)
