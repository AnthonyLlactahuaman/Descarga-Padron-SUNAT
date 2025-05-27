import os.path
import pandas as pd
import requests
from tqdm import tqdm
from Manage.Driver import CompDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import remove


class Comp_Buscador:
    def __init__(self, dirs):
        self.__dirs = dirs
        self.__ruta_carpeta_descarga = dirs.get_output_doc()
        self.__driver = CompDriver.get_driver(self.__ruta_carpeta_descarga)
        self.__zip = dirs.get_input_zip()
        self.__txt_final = dirs.get_output_final()

    def login(self):
        url = self.__dirs.get_url()
        self.__driver.get(url)
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]')))

    def descarga_archivo(self):
        try:
            ruta_desc = WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/a')))
            enlace = ruta_desc.get_attribute('href')
            self.__driver.close()
            response = requests.get(enlace, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            with open(self.__zip, 'wb') as archivo, tqdm(
                desc='Descargando',
                total=total_size, unit='B', unit_scale=True, unit_divisor=1024
            ) as barra_progreso:
                for datos in response.iter_content(chunk_size=1024):
                    barra_progreso.update(len(datos))
                    archivo.write(datos)
            print('Descarga completa..')
        except requests.exceptions.RequestException as e:
            print("El internet esta lento, no se pudo terminar la descarga")
            print("Error:", e)
            remove(self.__zip)

    def extrac_datos(self):
        print("Extrayendo Datos...")
        self.__zip.name.replace(".zip", ".txt")
        for chunk in pd.read_csv(self.__zip, header=None, encoding='ISO-8859-1', sep='|', usecols=[0, 1], chunksize=100000):
            chunk_replace = chunk.apply(lambda col: col.astype(str).apply(lambda x: f'"{x.strip()}"'))
            chunk_replace.to_csv(self.__txt_final, sep='|', mode='a', index=False, header=None)

    def main(self):
        if os.path.exists(self.__zip):
            pass
        else:
            self.login()
            self.descarga_archivo()
        self.extrac_datos()
        remove(self.__zip)
        print("****************************************")
        print("Programa Ejecutado con exito")
        print("****************************************")
        self.__driver.close()
