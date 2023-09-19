import pandas as pd 
import matplotlib.pyplot as plt
from fpdf import FPDF

df = pd.read_csv('C:\\Users\User\Desktop\Desafio Final Python\ProuniRelatorioDadosAbertos2020.csv', encoding='ISO-8859-1', sep=';', low_memory=False)
df.head()

# ANÁLISE EXPLORATÓRIA
print("Análise exploratória:")
print("Total de linhas:", len(df))
print("\nResumo estatístico:")
print(df.describe())
print("\nQuantidade de valores NaN por coluna:")
print(df.isna().sum())

# EXCLUINDO OS RESULTADOS NULOS
df.dropna(inplace=True)

print("Analise exploratoria: ")
print("Total de linhas: ", len(df))
print("Resumo estatistico:\n", df.describe())
print("\n")

#gerar gráfico modalidade de ensino PROUNI 2020
state_counts = df['MODALIDADE_ENSINO_BOLSA'].value_counts()
state_counts.plot(kind='bar', title='Bolsas do PROUNI distribuidas por modalidade no ano de 2020', figsize=(10, 6))
plt.xlabel('Modalidade de ensino')
plt.ylabel('Quantidade de bolsas')
plt.show()

#gerar gráfico modalidade de ensino PROUNI 2020
state_counts = df['RACA_BENEFICIARIO'].value_counts()
state_counts.plot(kind='bar', title='Bolsas do PROUNI distribuidas por raça no ano de 2020', figsize=(10, 6))
plt.xlabel('Raça do beneficiário')
plt.ylabel('Quantidade de bolsas')
plt.show()

#gerar gráfico modalidade de ensino PROUNI 2020
state_counts = df['NOME_TURNO_CURSO_BOLSA'].value_counts()
state_counts.plot(kind='bar', title='Bolsas do PROUNI distribuidas por horário no ano de 2020', figsize=(10, 6))
plt.xlabel('Horário de estudo do beneficiário')
plt.ylabel('Quantidade de bolsas')
plt.show()

#gerar arquivo pdf - gráfico 1/3
from fpdf import FPDF
pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font('helvetica', '', 16)
pdf.cell(w=0, h=0, txt="Bolsas do PROUNI distribuidas por modalidade no ano de 2020", align='C')

pdf.image(name="grafico_modalide_ensino.png", x=0, y=20, w=200)
pdf.output("prouni1.pdf")
print("pdf1 salvo")

#gerar arquivo pdf - gráfico 2/3
from fpdf import FPDF
pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font('helvetica', '', 16)
pdf.cell(w=0, h=0, txt="Bolsas do PROUNI distribuidas por raça no ano de 2020", align='C')

pdf.image(name="grafico_raca.png", x=0, y=20, w=200)
pdf.output("prouni2.pdf")
print("pdf2 salvo")

#gerar arquivo pdf - gráfico 3/3
from fpdf import FPDF
pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font('helvetica', '', 16)
pdf.cell(w=0, h=0, txt="Bolsas do PROUNI distribuidas por horário no ano de 2020", align='C')

pdf.image(name="grafico_horario.png", x=0, y=20, w=200)
pdf.output("prouni3.pdf")
print("pdf3 salvo")

#gerar relatório de conclusão da pesquisa 
import os
from fpdf import FPDF

pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', '', 16)

texto = "Detalhamento quantitativo das bolsas concedidas pelo Prouni por ano\n\nAtravés da interpretação dos gráficos, pude concluir que a maioria dos alunos preferem \na modalidade presencial. Grande parte dos alunos beneficiados pelas bolsas de estudo de até cem por centro do PROUNI são da raça negra. E a maioria dos alunos estudam no período noturno, provavelmente por trabalharem durante o dia.\n fonte: https://dadosabertos.mec.gov.br/images/conteudo/prouni/2020/ProuniRelatorioDadosAbertos2020.csv"

pdf.cell(w=0, h=7, txt=texto)

# Construir o PDF
pdf.output("relatorio.pdf")
print("pdf4 salvo")

#importa bibliotecas
import os
import glob
from PyPDF2 import PdfReader, PdfWriter

#função para unificar os pdfs e criar uma nova pasta concatenando
def concatenaPdf(caminho):
    os.chdir(caminho)
    arquivos = glob.glob('*.pdf')
    destino = r'C:\Users\User\Desktop\Desafio Final Python\pdf_projeto'

#cria o diretório de resultado, caso não exita
    if not os.path.exists(destino):
        os.makedirs(destino)
        print('Diretório de destino criado')
    else:
        print('Diretório de destino já existe')

    pdfWriter = PdfWriter()

#adiciona todas as páginas de cada arquivo
    for arquivo in arquivos:
        with open(arquivo, 'rb') as pdfDoc:
            pdfReader = PdfReader(pdfDoc)
            for pagina in pdfReader.pages:
                pdfWriter.add_page(pagina)

    pdfResultado = os.path.join(destino, 'concatenado.pdf')
    with open(pdfResultado, 'wb') as pdfOutput:
        pdfWriter.write(pdfOutput)

    print('PDFs concatenados com sucesso!')

concatenaPdf(r'C:\Users\User\Desktop\Desafio Final Python\pdf_projeto')