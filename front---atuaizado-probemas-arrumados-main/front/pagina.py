import flet as ft
from cores import Cores
 
 
# Dados de exemplo dos postos de recarga
# status pode ser: "disponivel", "ocupado" ou "manutencao"
postos = [
    {
        "nome": "EletroPosto Central",
        "local": "Av. Paulista, São Paulo",
        "imagem": "https://picsum.photos/seed/posto1/200/200",
        "preco": "R$ 1,20/kWh",
        "tipo": "RÁPIDO",
        "status": "disponivel",
    },
    {
        "nome": "Shopping Recarga Sul",
        "local": "Zona Sul, São Paulo",
        "imagem": "https://picsum.photos/seed/posto2/200/200",
        "preco": "R$ 0,95/kWh",
        "tipo": "PADRÃO",
        "status": "ocupado",
    },
    {
        "nome": "VoltPark Norte",
        "local": "Zona Norte, São Paulo",
        "imagem": "https://picsum.photos/seed/posto3/200/200",
        "preco": "R$ 1,35/kWh",
        "tipo": "RÁPIDO",
        "status": "disponivel",
    },
    {
        "nome": "Posto Verde Energia",
        "local": "Alphaville, Barueri",
        "imagem": "https://picsum.photos/seed/posto4/200/200",
        "preco": "R$ 1,10/kWh",
        "tipo": "PADRÃO",
        "status": "manutencao",
    },
]
 
 
def status_config(status: str):
    """Retorna (texto, cor) de acordo com o status do posto."""
    if status == "disponivel":
        return "Disponível", Cores.PRIMARIO_ESCURO
    elif status == "ocupado":
        return "Ocupado", Cores.PRIMARIO_ESCURO
    else:
        return "Manutenção", Cores.PRIMARIO_ESCURO
 
 
def main(page: ft.Page):
    page.title = "Postos de Recarga"
    page.bgcolor = Cores.FUNDO_ESCURO # fundo da pagina 
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN
    page.window.width = 400
    page.window.height = 800
 
    def selecionar_posto(nome):
        def handler(e):
            page.open(
                ft.SnackBar(
                    ft.Text(f"Navegando até {nome}..."),
                    bgcolor=Cores.PRIMARIO,
                )
            )
        return handler
 
    def criar_card_posto(posto: dict) -> ft.Container:
        texto_status, cor_status = status_config(posto["status"])
        pode_reservar = posto["status"] == "disponivel"
 
        return ft.Container(
            bgcolor=Cores.CARDS,
            border_radius=10,
            border=ft.Border.all(1, Cores.PRIMARIO_CLARO),
            padding=12,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Imagem do posto
                    ft.Container(
                        content=ft.Image(
                            src=posto["imagem"],
                            width=70,
                            height=70,
                            fit=ft.BoxFit.COVER,
                            border_radius=12,
                        ),
                        border_radius=12,
                    ),
                    ft.Container(width=12),
                    # Infos do posto
                    ft.Column(
                        expand=True,
                        spacing=2,
                        controls=[
                            ft.Text(
                                posto["tipo"],
                                size=10,
                                weight=ft.FontWeight.BOLD,
                                color=Cores.TEXTO_SECUNDARIO,
                                style=ft.TextStyle(letter_spacing=1),
                            ),
                            ft.Text(
                                posto["nome"],
                                size=15,
                                weight=ft.FontWeight.W_600,
                                color=Cores.TEXTO,
                            ),
                            ft.Row(
                                spacing=4,
                                controls=[
                                    ft.Icon(
                                        ft.Icons.LOCATION_ON,
                                        size=13,
                                        color=Cores.TEXTO_SECUNDARIO,
                                    ),
                                    ft.Text(
                                        posto["local"],
                                        size=12,
                                        color=Cores.TEXTO_SECUNDARIO,
                                    ),
                                ],
                            ),
                            ft.Container(height=4),
                            ft.Row(
                                spacing=6,
                                controls=[
                                    ft.Container(
                                        bgcolor=cor_status,
                                        border_radius=20,
                                        padding=ft.Padding.symmetric(
                                            horizontal=8, vertical=3
                                        ),
                                        content=ft.Text(
                                            texto_status,
                                            size=10,
                                            weight=ft.FontWeight.BOLD,
                                            color=Cores.FUNDO,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    
                    
                    
                    
                    # Preço e botão
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        spacing=8,
                        controls=[
                            ft.Text(
                                posto["preco"],
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color=Cores.TEXTO,
                            ),
                            ft.FilledButton(
                                content=ft.Text(
                                    "Reservar" if pode_reservar else "Indisponível",
                                    size=12,
                                ),
                                bgcolor=Cores.SUCESSO
                                if pode_reservar
                                else Cores.PRIMARIO_ESCURO,
                                color=Cores.TEXTO
                                if pode_reservar
                                else Cores.TEXTO_SECUNDARIO,
                                disabled=not pode_reservar,
                                on_click=selecionar_posto(posto["nome"]),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10)
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
 
    # Cabeçalho ---------------------------------------------------------------------------------------------------------------------
    
    
    cabecalho = ft.Container(
        padding=ft.Padding(left=20, right=20, top=20, bottom=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Icon(ft.Icons.ARROW_BACK, color=Cores.TEXTO),
                        ft.Text(
                            "Postos de Recarga",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=Cores.TEXTO,
                        ),
                    ],
                ),
                ft.Icon(ft.Icons.SEARCH, color=Cores.TEXTO),
            ],
        ),
    )
 
    # Lista de cards
    
    
    
    
    lista_postos = ft.ListView(
        expand=True,
        spacing=14,
        padding=ft.Padding.symmetric(horizontal=20),
        controls=[criar_card_posto(p) for p in postos],
    )
 
    # Barra de navegação inferior
    nav_inferior = ft.Container(
        padding=ft.Padding.symmetric(horizontal=30, vertical=16),
        bgcolor=Cores.PRIMARIO,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                #CORES CABEÇALHO
                ft.Icon(ft.Icons.HOME_FILLED, color=Cores.TEXTO),
                ft.Icon(ft.Icons.MAP_OUTLINED, color=Cores.TEXTO),
                ft.Icon(ft.Icons.EV_STATION, color=Cores.TEXTO),
                ft.Icon(ft.Icons.HISTORY, color=Cores.TEXTO),
                ft.Icon(ft.Icons.PERSON_OUTLINE, color=Cores.TEXTO),
            ],
        ),
    )
 
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                cabecalho,
                lista_postos,
                nav_inferior,
            ],
        )
    )
 
 
ft.run(main)
 