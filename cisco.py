def create_menu():
    # Display the menu title and options
    print("MANTENEDOR LIBRO")
    print("-" * 10)
    print("[1] Agregar libro")
    print("[2] Editar libro")
    print("[3] Eliminar libro")
    print("[4] Buscar libro")
    print("[5] Volver")
    print("-" * 10)

def display_book_list(books):
    # Print the book list header
    print("Listado de libros:")
    print("-" * 50)
    print(f"| {'ID':<10} | {'Titulo':<30} | {'AutorID':<10} | {'CategorialD':<10} | {'AnoPublicacion':<10} |")
    print("-" * 50)

    # Print each book's details
    for book in books:
        print(f"| {book['ID']:<10} | {book['Titulo']:<30} | {book['AutorID']:<10} | {book['CategorialD']:<10} | {book['AnoPublicacion']:<10} |")
    print("-" * 50)
