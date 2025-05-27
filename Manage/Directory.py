from pathlib import Path


class CompDirectory:
    def __init__(self):
        self.__root = Path.cwd()
        self.__url = 'https://www.sunat.gob.pe/descargaPRR/mrc137_padron_reducido.html'
        self.__output_doc = self.__root.joinpath('Output')
        self.__ouput_final = self.__output_doc.joinpath('Padron_SUNAT.txt')
        self.__input_zip = self.__output_doc.joinpath('padron_reducido_ruc.zip')

    def get_url(self):
        return self.__url

    def get_output_doc(self):
        return self.__output_doc

    def get_output_final(self):
        return self.__ouput_final

    def get_input_zip(self):
        return self.__input_zip
