from Manage.Directory import CompDirectory
from Manage.Buscador import Comp_Buscador
import msvcrt

if __name__ == '__main__':
    dirs = CompDirectory()
    buscardor = Comp_Buscador(dirs)
    buscardor.main()
    msvcrt.getch()
