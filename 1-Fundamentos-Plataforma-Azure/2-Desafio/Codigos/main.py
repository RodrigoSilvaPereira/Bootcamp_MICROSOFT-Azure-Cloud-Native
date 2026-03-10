import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
from dotenv import load_dotenv

load_dotenv()

blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title('Cadastro de Produtos')

product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%.2f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'png', 'jpeg'])

# Preview da imagem
if product_image:
    st.image(product_image, width=200)

# Upload da imagem para o Blob Storage
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)

    blob_name = str(uuid.uuid4()) + file.name

    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)

    image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"

    return image_url


# Inserir produto no banco
def insert_product(product_name, product_price, product_description, product_image):
    try:
        conn = pymssql.connect(
            server=SQL_SERVER,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )

        cursor = conn.cursor()

        cursor.execute(f"""
            INSERT INTO Produtos (nome, preco, descricao, imagem_url)
            VALUES ('{product_name}', {product_price}, '{product_description}', '{product_image}')
        """)

        conn.commit()

        cursor.close()
        conn.close()

        return True

    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
        return False


# Listar produtos
def list_products():
    try:
        conn = pymssql.connect(
            server=SQL_SERVER,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Produtos")

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []


# Tela de listagem
def list_products_screen():
    products = list_products()

    for product in products:
        st.subheader(product[1])
        st.write(f'Preço: R$ {product[2]}')
        st.write(product[3])
        st.image(product[4], width=200)
        st.divider()


# Botão salvar
if st.button('Salvar Produto'):

    if product_image is not None:

        image_url = upload_blob(product_image)

        if insert_product(product_name, product_price, product_description, image_url):
            st.success('Produto salvo com sucesso')

    else:
        st.error('Selecione uma imagem')


st.header('Produtos Cadastrados')

# Botão listar
if st.button('Listar produtos'):
    list_products_screen()