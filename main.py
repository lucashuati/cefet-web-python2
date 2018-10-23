from classes import Autor, Livro, Biblioteca

def main():
    autor1 = Autor('José', 'Silva', '01/06/1985', nome_do_meio='Da')
    autor2 = Autor('Lucas','Corrêa', '08/07/1994')
    autor3 = Autor('Ana','Bueno', '30/07/1995', nome_do_meio='Andere')

    try:
        livro1 = Livro(titulo='', ano=2015, autores=[autor1, autor2])
    except ValueError as e:
        print(f'Erro ao criar livro: {e}')
    livro2 = Livro(titulo='Livro 1', ano=2000, autores=[autor1, autor3])
    livro3 = Livro(titulo='Livro 2', ano=1999, autores=[autor3, autor2])
    livro4 = Livro(titulo='Livro 3', ano=1999, autores=[autor3, autor2, autor1])

    biblioteca = Biblioteca(livros=[livro2, livro3, livro4])

    print(autor1)
    print(autor2)
    print(autor3)
    print(livro2)
    print(livro3)
    print(livro4)
    print(biblioteca.livros_por_autor)


if __name__ == '__main__':
    main()
