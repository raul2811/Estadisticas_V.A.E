import reflex as rx
from database.querys import Querys_return

class Totals(rx.State):
    @rx.var(cache=True)
    def journals_total(self) -> str:
        total=Querys_return.mostrar_statistics('journals')
        return total
        #retorna el total de revistas.
    @rx.var(cache=True)
    def volumen_total(self) -> str:
        total=Querys_return.mostrar_statistics('volumen')
        return f"{total:,.2f}".replace(",", ".")
        #retorna el total de volumenes de revistas en general.
    @rx.var(cache=True)
    def arti_ess_total(self) -> str:
        total=Querys_return.mostrar_statistics('arti_ess')
        return f"{total:,.2f}".replace(",", ".")
        #retorna el total de  articulos y ensayos.
    @rx.var(cache=True)
    def users_total(self) -> str:
        total=Querys_return.mostrar_statistics('users')
        return f"{total:,.2f}".replace(",", ".")
        #retorna el total de  usuarios general.
    @rx.var(cache=True)
    def users_pa_total(self) -> str:
        total=Querys_return.mostrar_statistics('users_pa')
        return f"{total:,.2f}".replace(",", ".")
        #retorna el total de  usuarios panamenos.
    @rx.var(cache=True)
    def users_ext_total(self) -> str:
        total=Querys_return.mostrar_statistics('users_ext')
        return f"{total:,.2f}".replace(",", ".")
        #retorna el total de  usuarios extranjeros.
    @rx.var(cache=True)
    def downloads_total(self) -> str:
        total=Querys_return.mostrar_statistics('downloads')
        return f"{total:,.2f}".replace(",", ".")
        #retorna el total de  descargas.