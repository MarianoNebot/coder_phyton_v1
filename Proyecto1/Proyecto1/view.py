
from datetime import date, datetime
from django.http import HttpResponse 
from django.template import Context, Template



def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto , es muy simple :" )


def diaDeHoy(request):
        dia = datetime.now()
        documentoDeTexto = f"hoy es dia: <br> {dia}"
        
        
        
        return HttpResponse(documentoDeTexto)
    

def miNombreEs(self, nombre):
         documentoDeTexto = f"Mi nombre es : <br><br> {nombre}"
         
         
         return HttpResponse(documentoDeTexto)


def tercera_vista(request , fecha):
    fecha_actual = date.today()
    anio = fecha_actual.year
    
    
    fecha= int(fecha)
    
    
    resultado = anio - fecha
    retorno = f"El año en que naciste es : {resultado}"
    return HttpResponse(retorno)



def probandoTemplate(self):
    miHtml = open("A:\django\Proyecto1\Proyecto1\plantillas\template1.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

    