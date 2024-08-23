import reflex as rx
from database.querys import Querys_return

class Submission_recents(rx.State):
    #! Variables de la tabla Submission_recents 'indice 0'
    @rx.var
    def publication_id_0(self):
        self=0
        data=Querys_return.mostrar_submission_recents(self,'publication_id')
        return data
        #retorna el submission_id de el articulo que mas se ha descargado en la posicion 0
    @rx.var
    def date_published_0(self):
        self=0
        data=Querys_return.mostrar_submission_recents(self,'date_published')
        return data
        #retorna el date_published de el articulo que mas se ha descargado en la posicion 0
    @rx.var
    def title_0(self):
        self=0
        data=Querys_return.mostrar_submission_recents(self,'title')
        return data
        #retorna el title de el articulo que mas se ha descargado en la posicion 0
    @rx.var
    def issue_id_0(self):
        self=0
        data=Querys_return.mostrar_submission_recents(self,'issue_id')
        return data
        #retorna el issue_id de el articulo que mas se ha descargado en la posicion 0
    @rx.var
    def journal_id_0(self):
        self=0
        data=Querys_return.mostrar_submission_recents(self,'journal_id')
        return data 
        # retorna el journal_id de el articulo que mas se ha descargado en la posicion 0


    #! Variables de la tabla Submission_recents 'indice 1'
    @rx.var
    def publication_id_1(self):
        self=1
        data=Querys_return.mostrar_submission_recents(self,'publication_id')
        return data
        #retorna el submission_id de el articulo que mas se ha descargado en la posicion 1
    @rx.var
    def date_published_1(self):
        self=1
        data=Querys_return.mostrar_submission_recents(self,'date_published')
        return data
        #retorna el date_published de el articulo que mas se ha descargado en la posicion 1
    @rx.var
    def title_1(self):
        self=1
        data=Querys_return.mostrar_submission_recents(self,'title')
        return data
        #retorna el title de el articulo que mas se ha descargado en la posicion 1
    @rx.var
    def issue_id_1(self):
        self=1
        data=Querys_return.mostrar_submission_recents(self,'issue_id')
        return data
        #retorna el issue_id de el articulo que mas se ha descargado en la posicion 1
    @rx.var
    def journal_id_1(self):
        self=1
        data=Querys_return.mostrar_submission_recents(self,'journal_id')
        return data
        #retorna el journal_id de el articulo que mas se ha descargado en la posicion 1


    #! Variables de la tabla Submission_recents 'indice 2'
    @rx.var
    def publication_id_2(self):
        self=2
        data=Querys_return.mostrar_submission_recents(self,'publication_id')
        return data
        #retorna el submission_id de el articulo que mas se ha descargado en la posicion 2
    @rx.var
    def date_published_2(self):
        self=2
        data=Querys_return.mostrar_submission_recents(self,'date_published')
        return data
        #retorna el date_published de el articulo que mas se ha descargado en la posicion 2
    @rx.var
    def title_2(self):
        self=2
        data=Querys_return.mostrar_submission_recents(self,'title')
        return data
        #retorna el title de el articulo que mas se ha descargado en la posicion 2
    @rx.var
    def issue_id_2(self):
        self=2
        data=Querys_return.mostrar_submission_recents(self,'issue_id')
        return data
        #retorna el issue_id de el articulo que mas se ha descargado en la posicion 2
    @rx.var
    def journal_id_2(self):
        self=2
        data=Querys_return.mostrar_submission_recents(self,'journal_id')
        return data
        #retorna el journal_id de el articulo que mas se ha descargado en la posicion 2


    #! Variables de la tabla Submission_recents 'indice 3'
    @rx.var
    def publication_id_3(self):
        self=3
        data=Querys_return.mostrar_submission_recents(self,'publication_id')
        return data
        #retorna el submission_id de el articulo que mas se ha descargado en la posicion 3
    @rx.var
    def date_published_3(self):
        self=3
        data=Querys_return.mostrar_submission_recents(self,'date_published')
        return data
        #retorna el date_published de el articulo que mas se ha descargado en la posicion 3
    @rx.var
    def title_3(self):
        self=3
        data=Querys_return.mostrar_submission_recents(self,'title')
        return data
        #retorna el title de el articulo que mas se ha descargado en la posicion 3
    @rx.var
    def issue_id_3(self):
        self=3
        data=Querys_return.mostrar_submission_recents(self,'issue_id')
        return data
        #retorna el issue_id de el articulo que mas se ha descargado en la posicion 3
    @rx.var
    def journal_id_3(self):
        self=3
        data=Querys_return.mostrar_submission_recents(self,'journal_id')
        return data
        #retorna el journal_id de el articulo que mas se ha descargado en la posicion 3
