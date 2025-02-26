import mysql.connector
from mysql.connector import Error

def create_connection():
    """Cria uma conexão com o banco de dados MySQL."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=' 192.168.0.18',
            port='3306',
            user='root',
            password='root',
            database='BD_AVIOES'
        )
        print("Conexão com o MySQL bem-sucedida")
    except Error as e:
        print(f"Erro '{e}' ocorreu")

    return connection

def create_cliente(connection, id, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, country, postalCode, salesRepEmployeeNumber, creditLimit):
    """Insere um novo cliente na tabela TB_CLIENTES."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_CLIENTES (id, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state,country, postalCode, salesRepEmployeeNumber, creditLimit) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (id, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, country, postalCode, salesRepEmployeeNumber, creditLimit))
    connection.commit()
    print("Cliente adicionado com sucesso")

def read_clientes(connection):
    """Lê todos os clientes da tabela TB_CLIENTES."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_CLIENTES")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

def update_cliente(connection, id, customerName, phone):
    """Atualiza um cliente existente na tabela TB_CLIENTES."""
    cursor = connection.cursor()
    query = "UPDATE TB_CLIENTES SET customerName = %s, phone = %s WHERE id = %s"
    cursor.execute(query, (customerName, phone, id))
    connection.commit()
    print("Cliente atualizado com sucesso")

def delete_cliente(connection, id):
    """Deleta um cliente da tabela TB_CLIENTES."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_CLIENTES WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Cliente deletado com sucesso")
    
def create_detalhe_pedido(connection, id_orderNumber, id_productCode,quantityOrdered,priceEach,orderLineNumber):
    """Insere um novo detalhe pedido na tabela TB_DETALHES_PEDIDOS."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_DETALHES_PEDIDOS (id_orderNumber, id_productCode, quantityOrdered, priceEach, orderLineNumber) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id_orderNumber, id_productCode,quantityOrdered,priceEach,orderLineNumber))
    connection.commit()
    print("Detalhe pedido adicionado com sucesso")

def read_detalhe_pedido(connection):
    """Lê todos os detalhes da tabela TB_DETALHES_PEDIDOS."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_DETALHES_PEDIDOS")
    detalhes = cursor.fetchall()
    for detalhe in detalhes:
        print(detalhe)

def update_detalhe_pedido(connection, id_orderNumber, priceEach, quantityOrdered):
    """Atualiza um cliente existente na tabela TB_CLIENTES."""
    cursor = connection.cursor()
    query = "UPDATE TB_DETALHES_PEDIDOS SET priceEach = %s, quantityOrdered = %s WHERE id_orderNumber = %s"
    cursor.execute(query, (priceEach, quantityOrdered, id_orderNumber))
    connection.commit()
    print("Pedido atualizado com sucesso")

def delete_detalhe_pedido(connection, id_orderNumber):
    """Deleta um cliente da tabela TB_DETALHES_PEDIDOS."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_DETALHES_PEDIDOS WHERE id_orderNumber = %s"
    cursor.execute(query, (id_orderNumber,))
    connection.commit()
    print("Detalhe pedido deletado com sucesso")
    

def create_empregados(connection, id, lastName,firstName,extension,email, officeCode, reportsTo, jobTittle):
    """Insere um novo detalhe pedido na tabela TB_EMPREGADOS."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_EMPREGADOS (id, lastName,firstName,extension,email, officeCode, reportsTo, jobTittle) VALUES (%s, %s, %s, %s,%s,%s, %s, %s)"
    cursor.execute(query, (id, lastName,firstName,extension,email, officeCode, reportsTo, jobTittle))
    connection.commit()
    print("Empregado adicionado com sucesso")

def read_empregados(connection):
    """Lê todos os detalhes da tabela TB_EMPREGADOS."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_EMPREGADOS")
    empregados = cursor.fetchall()
    for empregado in empregados:
        print(empregado)

def update_empregado(connection, id, firstName, lastName):
    """Atualiza um cliente existente na tabela TB_EMPREGADOS."""
    cursor = connection.cursor()
    query = "UPDATE TB_EMPREGADOS SET firstName = %s, lastName = %s WHERE id = %s"
    cursor.execute(query, (firstName, lastName, id))
    connection.commit()
    print("Empregado atualizado com sucesso")

def delete_empregado(connection, id):
    """Deleta um cliente da tabela TB_EMPREGADOS."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_EMPREGADOS WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Empregado deletado com sucesso")
    
def create_escritorios(connection, id, city,state,country,phone, addressLine1, addressLine2, postalCode, territory):
    """Insere um novo detalhe pedido na tabela TB_ESCRITORIOS."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_ESCRITORIOS (id, city,state,country,phone,addresLine1,addresLine2, postalCode, territory) VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s)"
    cursor.execute(query, (id, city,state,country,phone, addressLine1, addressLine2, postalCode, territory))
    connection.commit()
    print("Escritorio adicionado com sucesso")

def read_escritorios(connection):
    """Lê todos os detalhes da tabela TB_ESCRITORIOS."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_ESCRITORIOS")
    escritorios = cursor.fetchall()
    for escritorio in escritorios:
        print(escritorio)

def update_escritorios(connection, id, city, phone):
    """Atualiza um cliente existente na tabela TB_ESCRITORIOS."""
    cursor = connection.cursor()
    query = "UPDATE TB_ESCRITORIOS SET city = %s, phone = %s WHERE id = %s"
    cursor.execute(query, (city, phone, id))
    connection.commit()
    print("Escritorio atualizado com sucesso")

def delete_escritorios(connection, id):
    """Deleta um cliente da tabela TB_ESCRITORIOS."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_ESCRITORIOS WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Escritorio deletado com sucesso")

def create_linhas_produto(connection, id, htmlDescription,image,textDescription):
    """Insere um novo detalhe pedido na tabela TB_LINHAS_DE_PRODUTO."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_LINHAS_DE_PRODUTO (id, htmlDescription,image,textDescription) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, htmlDescription,image,textDescription))
    connection.commit()
    print("linhas de produto adicionado com sucesso")

def read_linhas_produto(connection):
    """Lê todos os detalhes da tabela TB_LINHAS_DE_PRODUTO."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_LINHAS_DE_PRODUTO")
    linhas = cursor.fetchall()
    for linha in linhas:
        print(linha)

def update_linhas_produto(connection, id, htmlDescription, image):
    """Atualiza um cliente existente na tabela TB_LINHAS_DE_PRODUTO."""
    cursor = connection.cursor()
    query = "UPDATE TB_LINHAS_DE_PRODUTO SET htmlDescription = %s, image = %s WHERE id = %s"
    cursor.execute(query, (htmlDescription, image, id))
    connection.commit()
    print("Linhas atualizado com sucesso")

def delete_linhas_produto(connection, id):
    """Deleta um cliente da tabela TB_LINHAS_DE_PRODUTO."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_LINHAS_DE_PRODUTO WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Linhas deletado com sucesso")
    
def create_pagamentos(connection, id, id_costumerNumber,paymentDate,amount):
    """Insere um novo detalhe pedido na tabela TB_PAGAMENTOS."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_PAGAMENTOS (id, id_costumerNumber,paymentDate,amount) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, id_costumerNumber,paymentDate,amount))
    connection.commit()
    print("pagamentos de produto adicionado com sucesso")

def read_pagamentos(connection):
    """Lê todos os detalhes da tabela TB_PAGAMENTOS."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_PAGAMENTOS")
    pagamentos = cursor.fetchall()
    for pagamento in pagamentos:
        print(pagamento)

def update_pagamentos(connection, id, paymentDate, amount):
    """Atualiza um cliente existente na tabela TB_PAGAMENTOS."""
    cursor = connection.cursor()
    query = "UPDATE TB_PAGAMENTOS SET paymentDate = %s, amount = %s WHERE id = %s"
    cursor.execute(query, (paymentDate, amount, id))
    connection.commit()
    print("pagamento atualizado com sucesso")

def delete_pagamentos(connection, id):
    """Deleta um cliente da tabela TB_PAGAMENTOS."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_PAGAMENTOS WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("pagamento deletado com sucesso")
    
def create_pedidos(connection,id, id_costumerNumber, orderDate,requiredDate,shippedDate, status, comments ):
    """Insere um novo detalhe pedido na tabela TB_PEDIDOS."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_PEDIDOS (id, id_costumerNumber, orderDate,requiredDate,shippedDate, status, comments) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, id_costumerNumber,orderDate,requiredDate,shippedDate, status, comments))
    connection.commit()
    print("pedido de produto adicionado com sucesso")

def read_pedidos(connection):
    """Lê todos os detalhes da tabela TB_PEDIDOS."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_PEDIDOS")
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        print(pedido)

def update_pedidos(connection, id, orderDate, status):
    """Atualiza um cliente existente na tabela TB_PEDIDOS."""
    cursor = connection.cursor()
    query = "UPDATE TB_PEDIDOS SET orderDate = %s, status = %s WHERE id = %s"
    cursor.execute(query, (orderDate, status, id))
    connection.commit()
    print("pedido atualizado com sucesso")

def delete_pedidos(connection, id):
    """Deleta um cliente da tabela TB_PEDIDOS."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_PEDIDOS WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("pedido deletado com sucesso")
    
def create_produtos(connection, id, productName,id_productLine,productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP):
    """Insere um novo detalhe pedido na tabela TB_PRODUTOS."""
    cursor = connection.cursor()
    query = "INSERT INTO TB_PRODUTOS (id, productName,id_productLine,productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, productName,id_productLine,productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP))
    connection.commit()
    print("produto adicionado com sucesso")

def read_produtos(connection):
    """Lê todos os detalhes da tabela TB_PRODUTOS."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_PRODUTOS")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)

def update_produtos(connection, id, productName, buyPrice):
    """Atualiza um cliente existente na tabela TB_PRODUTOS."""
    cursor = connection.cursor()
    query = "UPDATE TB_PRODUTOS SET productName = %s, buyPrice = %s WHERE id = %s"
    cursor.execute(query, (productName, buyPrice, id))
    connection.commit()
    print("produto atualizado com sucesso")

def delete_produtos(connection, id):
    """Deleta um cliente da tabela TB_PRODUTOS."""
    cursor = connection.cursor()
    query = "DELETE FROM TB_PRODUTOS WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("produto deletado com sucesso")


def main():
    connection = create_connection()
    if connection is None:
        return

    # Exemplo de uso das funções CRUD
    create_cliente(connection, 1, 'Empresa A', 'Santos', 'Arthur', '8599999999', 'Rua 6', 'Casa 300', 'Fortaleza', 'CE', 'Brazil', '12243-987', None, 200000.00)
    read_clientes(connection)
    update_cliente(connection, 1, 'Empresa A & CIA', '77777777')
    read_clientes(connection)
    delete_cliente(connection, 1)
    read_clientes(connection)
    
    #Crud em TB_DETALHES_PEDIDOS
    create_detalhe_pedido(connection, 1, 23, 10, 5, '6')
    read_detalhe_pedido(connection)
    update_detalhe_pedido(connection, 1, 22, 63)
    read_detalhe_pedido(connection)
    delete_detalhe_pedido(connection, 1)
    read_detalhe_pedido(connection)
    
    #Crud em TB_EMPREGADOS
    create_empregados(connection, 1, 'Santos', 'Arthur', '2014', 'arthursantos@hotmail.com', '12345', 'None', 'Gerente')
    read_empregados(connection)
    update_empregado(connection, 1, 'Arthur', 'dos Santos')
    read_empregados(connection)
    delete_empregado(connection, 1)
    read_empregados(connection)
    
    #Crud em TB_ESCRITORIOS
    create_escritorios(connection, 1, 'Xique-xique', 'Bahia', 'Bazil', '8512345678', 'Rua Xique', 'Bairro Xique', '62670000', 'Cidade')
    read_escritorios(connection)
    update_escritorios(connection, 1, 'Fortaleza', '2222')
    read_escritorios(connection)
    delete_escritorios(connection, 1)
    read_escritorios(connection)
    
    #Crud em TB_LINHAS_DE_PRODUTO
    create_linhas_produto(connection, 1, '<p>Aviao preto</p>', 'Aviao preto.png', 'Aviao preto')
    read_linhas_produto(connection)
    update_linhas_produto(connection, 1, 'Nova descricao', 'Motor')
    read_linhas_produto(connection)
    delete_linhas_produto(connection, 1)
    read_linhas_produto(connection)
    
    #Crud em TB_PAGAMENTOS
    create_pagamentos(connection, 1, 100, '26/02/2025', 10)
    read_pagamentos(connection)
    update_pagamentos(connection, 1, '27/02/2025', 25)
    read_pagamentos(connection)
    delete_pagamentos(connection, 1)
    read_pagamentos(connection)
    
    #Crud em TB_PEDIDOS
    create_pedidos(connection, 1, '1234156', '10/01/2026','25/01/2025', '26/02/2025', 'A caminho', 'Fragil')
    read_pedidos(connection)
    update_pedidos(connection, 1, '2/02/2025', 'De boa')
    read_pedidos(connection)
    delete_pedidos(connection, 1)
    read_pedidos(connection)
    
    #Crud em TB_PRODUTOS
    create_produtos(connection, 1, 'Headset', 40,'1:30', 'Bom Som', 'Headset de qualidade', 2, 100, 120)
    read_produtos(connection)
    update_produtos(connection, 1, 'Head', 150)
    read_produtos(connection)
    delete_produtos(connection, 1)
    read_produtos(connection)

    connection.close()

if __name__ == "__main__":
    main()