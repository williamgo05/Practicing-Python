estoque = []

def no_duplicity(product_code):
    for produto in estoque:
        if produto["Code"] == product_code:
            return True
    return False

def cadastro():
    product_code = int(input("Code: "))
    if no_duplicity(product_code):
        print("\n*** Produto já cadastrado ***\n")
        return
    name = input("Name: ")
    price = float(input("Price: "))
    if price < 0:
        print("\n*** Preço não pode ser negativo! ***\n")
        return
    quantity = int(input("Quantity: "))
    if quantity < 0:
        print("\n*** Quantidade não pode ser negativa! ***\n")
        return
    produto = {
    "Code": product_code,
    "Name": name,
    "Price": price,
    "Quantity": quantity
    }
    estoque.append(produto)
    print("\n### Produto cadastrado com sucesso ###\n")
    print(f'Code: {produto["Code"]}\nName: {produto["Name"]}\nPrice: R$ {produto["Price"]:.2f}\nQuantity: {produto["Quantity"]}\n')

def soma():
    total_quantity = sum(produto["Quantity"] for produto in estoque)
    print(f"Estoque total: {total_quantity}\n")


while True:
    digito = int(input("Digite:\n[1] cadastrar um novo produto;\n[2] listar total da soma dos produtos cadastrados;\n[0] sair do sistema!\n"))
    if digito == 1:
        cadastro()
    elif digito == 2:
        soma()
    elif digito == 0:
        print("\nSaindo do sistema!\n")
        break
    else:
        print("\nOpção inválida!\n")
