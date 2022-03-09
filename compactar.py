# importação dos módulos
import os
import zipfile
import pathlib
import datetime

def main():
    try:
        fulldata = datetime.datetime.now()
        data = (fulldata.strftime("%Y%m%d"))
        nome_arquivo = "bkp_sw_" + data + ".zip"
        # Informa e lista todos os arquivos do diretório
        path = "."
        dir_list = os.listdir(path)
         
        # Teste de impressão da lista
        #print(dir_list)

        # Cria o arquivo, valida a extensão e adiciona no arquivo.zip
        with zipfile.ZipFile(nome_arquivo, mode="w") as arquivo:
            for filename in dir_list:
                file_extension = pathlib.Path(filename).suffix
                #print("extensão: ", file_extension)
                if (file_extension == ".png") or (file_extension == ".PNG"):
                    #print("extensão PNG: ", filename)
                    arquivo.write(filename)
                    #os.remove(filename)
    except:
        print ('Erro ao criar arquivos, verifique!')
            

if __name__ == '__main__': main()