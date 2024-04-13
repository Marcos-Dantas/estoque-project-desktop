import os
import xml.etree.ElementTree as Et


class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) if arq.lower().endswith(".xml")]

    def get_data_xml(self, xml):
        root = Et.parse(xml).getroot()

        dados = {}

        quantidade = root.find('quantidade')
        if quantidade is not None:
            dados['quantidade'] = quantidade.text

        medicacao = root.find('medicacao')
        if medicacao is not None:
            dados['medicacao'] = medicacao.text

        datadeentrada = root.find('datadeentrada')
        if datadeentrada is not None:
            dados['datadeentrada'] = datadeentrada.text
        
        datadesaida = root.find('datadesaida')
        if datadesaida is not None:
            dados['datadesaida'] = datadesaida.text

        usuario = root.find('usuario')
        if usuario is not None:
            dados['usuario'] = usuario.text
        
        paciente = root.find('paciente')
        if usuario is not None:
            dados['paciente'] = paciente.text

        return [value for key, value in dados.items()]
    
    

if __name__ == "__main__":
    xml_reader = Read_xml('arquivos_xml')

    all_xml_files = xml_reader.all_files()

    for xml_file in all_xml_files:
        result = xml_reader.get_data_xml(xml_file)
        print(result)