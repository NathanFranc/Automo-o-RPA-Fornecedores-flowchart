from botcity.web.browsers.firefox import default_options
from webdriver_manager.firefox import GeckoDriverManager
import os
from botcity.web import *
from datetime import datetime
from botcity.plugins.excel import *
from tkinter import filedialog, messagebox, simpledialog, colorchooser
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk

class Bot:
    def bot(self):

        # Flowchart Activity
        # Displayname: Flowchart
        flowStep = "__ReferenceID6"

        while True:

            if flowStep == "__ReferenceID6":

                # Sequence: Abrir a planilha de fonecedores

                # Read Excel Activity
                # Displayname: Read_Excel
                excelBot = BotExcelPlugin()
                file_or_path = "C:\\Users\\JEFFERSON LIMA\\Downloads\\Lista_exemplo.xlsx"

                listaFornecedores = excelBot.read(file_or_path=file_or_path).as_list(sheet="lista")[1:]
                # Count List Activity
                # Displayname: Count_List
                fornecedoresQTDE = len(listaFornecedores)

                # Assign Activity
                # Displayname: Assign_Values
                linha = 0

                flowStep = "__ReferenceID7"
                continue

            if flowStep == "__ReferenceID7":

                # Sequence: Fazer o login no site de cadastro de Fornecedores

                # Open Browser Activity
                # Displayname: OpenBrowser
                webDriverPath = GeckoDriverManager().install()
                webBot = WebBot()
                webBot.driver_path = webDriverPath
                webBot.browser = Browser.FIREFOX
                webBot.headless = False
                webBot.page_load_strategy = "Normal"
                webBotDef_options = default_options()
                webBot.options = webBotDef_options
                webBot.browse("https://jornadarpa.com.br/alunos/desafios/cadfor25")

                # DisplayName: Mapeamento do campos Login

                # Sequence: Mapeameto dos campos dos Elementos de Login

                # Find Element Activity
                # Displayname: Mapeamento do campo Email
                campoEmail = webBot.find_element(selector="usuario", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Mapeamento do campo Senha
                campoSenha = webBot.find_element(selector="senha", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Botão GPD
                botaoGPD = webBot.find_element(selector="lgpd", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: 
                botaoLogin = webBot.find_element(selector="btnLogin", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # DisplayName: Realizar o login

                # Sequence: Action list

                # Type Into Activity
                # Displayname: Type Into campoEmail field
                campoEmail.send_keys("participante@desafiosrpa.com.br")

                # Type Into Activity
                # Displayname: Type Into campoSenha field
                campoSenha.send_keys("evento")

                # Click Activity
                # Displayname: Click in botaoGPD element
                botaoGPD.click()

                # Click Activity
                # Displayname: Click in botaoLogin element
                botaoLogin.click()

                flowStep = "__ReferenceID10"
                continue

            if flowStep == "__ReferenceID10":

                # DisplayName: mapeamento dos campos de cadastro de Fornecedores

                # Sequence: Element list

                # Find Element Activity
                # Displayname: Campo PF
                botaoPF = webBot.find_element(selector="pf", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Campo PJ
                botaoPJ = webBot.find_element(selector="pj", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Campo Nome Razão
                campoNomeRazao = webBot.find_element(selector="nomeRazao", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Campo CPF/CNPJ
                campoCpfCnpj = webBot.find_element(selector="cpfCnpj", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Botão
                botaoEnviar = webBot.find_element(selector="btnEnviar", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                flowStep = "__ReferenceID5"
                continue

            if flowStep == "__ReferenceID5":

                # Displayname: Verificar se tem dados na planilha para cadastro
                if linha <= (fornecedoresQTDE -1):

                    flowStep = "__ReferenceID8"
                    continue
                else:

                    flowStep = "__ReferenceID9"
                    continue

            if flowStep == "__ReferenceID8":

                # Sequence: Cadastramento de Dados


                # Flowchart Activity
                # Displayname: Realizar por cadastro de fornecedores
                flowStep = "__ReferenceID1"

                while True:

                    if flowStep == "__ReferenceID1":

                        # Displayname: Se é cliente PF ou PJ
                        if listaFornecedores[linha][0] == "PF":

                            flowStep = "__ReferenceID2"
                            continue
                        else:

                            flowStep = "__ReferenceID3"
                            continue

                    if flowStep == "__ReferenceID2":

                        # Click Activity
                        # Displayname: Click
                        botaoPF.click()

                        flowStep = "__ReferenceID0"
                        continue

                    if flowStep == "__ReferenceID0":

                        # Sequence: Entrada de  dados do Fornecedor

                        # Type Into Activity
                        # Displayname: Type_Into
                        campoNomeRazao.send_keys(listaFornecedores[linha][1])

                        # Type Into Activity
                        # Displayname: Type_Into
                        campoCpfCnpj.send_keys(listaFornecedores[linha][2])

                        flowStep = "__ReferenceID4"
                        continue

                    if flowStep == "__ReferenceID4":

                        # Click Activity
                        # Displayname: Click
                        botaoEnviar.click()

                    if flowStep == "__ReferenceID3":

                        # Click Activity
                        # Displayname: Click
                        botaoPJ.click()

                        flowStep = "__ReferenceID0"
                        continue

                    break

                # Assign Activity
                # Displayname: Assign_Values
                linha = linha +1

                flowStep = "__ReferenceID5"
                continue

            if flowStep == "__ReferenceID9":

                # Sequence: Encerramento do rpa

                # Tk MessageBox Activity
                # Displayname: Tk_MessageBox
                root = tk.Tk()
                root.title("Atenção")
                root.withdraw()
                messageBoxResult = messagebox.showinfo("Atenção", "O cadastramento dos fornecedores foram realizados com sucesso")
                root.quit()

            break


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()