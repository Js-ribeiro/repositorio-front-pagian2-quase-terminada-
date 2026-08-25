


from enum import Enum, EnumType
import flet as ft

class Constantes(Enum):
    HOST="http://localhost:5000"
    OBTER_POSTO = lambda x: f"postos/{x}"
    
    
    
    
class Cores(EnumType):
    PRIMARIO= "#0C0505"
    PRIMARIO_ESCURO= "#D62627"
    PRIMARIO_CLARO = "#FD502D"
    PRIMARIO_ESCURO_TRANSPARENT= "0x88D62627"
    PRIMARIO_CLARO_TRANSPARENT = "0x88FD502D"
    CARDS =  "#140100"
    FUNDO= "#17181B"
    SUPERFICIE= "#292729"
    SUPERFICIE_ESCURO= "#120909"

    TEXTO= "#FDE6DE"
    TEXTO_SECUNDARIO= "#B9ADBA"
    TEXTO_DESATIVADO= "#944749"

    BORDA= "#EBB3A4"
    BORDA_FOCADA= "#FD502D"

    SUCESSO= "#4CAF50"
    ATENCAO= "#724B3B"
    ERRO= "#FD241B"
    PRETO = "#0A0A0A"
    TESTE= "#F5D20F"
    
    FUNDO_ESCURO= "#18191A"
    INPUT_FUNDO= "#120909"
    INPUT_BORDA= "#EBB3A4"
    INPUT_FOCADO= "#FD502D"
    # TEXTO_PRINCIPAL ="#FDE6DE",
    # TEXTO_SECUNDARIO= "#B9ADBA",
    
    
class EstiloConstantes(Enum):
    borda=ft.Border.all(1, Cores.PRIMARIO_CLARO, )
    arredondamento=ft.BorderRadius.all(6)
class Assets(EnumType):
    login_fundo="assets/login-fundo.jpeg"