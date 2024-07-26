import pandas as pd 

df = pd.read_csv("tabela_livros.csv")
print(df)

livro_novo = {"Titulo do Livro":["Python para Todos"],
"Autor":["Charles Severance"],"Categoria":["Programação"],
"Ano de Publicação": [2016],"Ativo": ["True"]}

novo_livro = pd.DataFrame (livro_novo)


print(novo_livro)

# Exercicio 1
print("Exercicio 2")
#df.append(livro, ignore_index=True)
print(novo_livro)
# Exercicio 2
livros_programacao = df[df["Categoria"]== "Programming"]
print("Exercicio 2")
print("Livros de Programação", livros_programacao)


"""df_filtrado = df[df["Ano de Publicação"] == 1993]

print(df_filtrado)"""
## 

# Exercicio 3
df.loc[df["Titulo do Livro"]=="O Alquimista", "Ativo"] = False
print("Exercio 3", df[df["Titulo do Livro"]=="O Alquimista"])


# Exercicio 4
df_ordenado = df.sort_values(by="Ano de Publicação")
print("Exercicio 4")
print(df_ordenado)

#Exercicio 5
def imprimir_livros_por_categoria(dataframe, categoria):
    filtro_categoria = dataframe[dataframe['Categoria'] == categoria]
    for index, livro in filtro_categoria.iterrows():
        print(
            f"Titulo: {livro['Titulo do Livro']}, Autor: {livro['Autor']}, Categoria: {livro['Categoria']}, Ano: {livro['Ano de Publicação']}, Ativo: {livro['Ativo']}"
        )

print("Exercicio 5")
imprimir_livros_por_categoria(df, "Fiction")


















class Livro:
    def __init__(self, titulo, autor, categoria, ano, ativo):
        self.titulo = titulo
        self.categoria = categoria
        self.ano = ano
        self.ativo = ativo
        self.autor = autor

livro0 = Livro("Livro 0", "Julio", "Progração",2012, "Sim")
livro1 = Livro("Livro 1", "Julio", "Progração",2012, "Sim")
livro2 = Livro("Livro 2", "Julio", "Progração",2012, "Sim")
lista_de_livros = [livro0, livro1, livro2]

#for livro in lista_de_livros:
    #print(livro.titulo)



