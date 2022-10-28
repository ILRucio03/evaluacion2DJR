from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def infousuario(request):
    user = """
<!DOCTYPE html>
<html lang="es">
    <head>
        <title></title>
        <style type="text/css">
            h1{
                 background-color: rgb(50, 100, 255);
                 }
        </style>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
    </head>
    <body class="container mt-5">
        <div class="alert alert-info display-1 text-center"><img src="/static/images/dj.png" >DJANGO SHOP</div>
        <div><h1><center>INFORMACION USUARIO</center></h1></div>

        <div class="card mb-3" style="max-width: 540px;">
         <div class="row g-0">
          <div class="col-md-4">
            <img src="/static/images/usuario.png" class="img-fluid rounded-start" alt="...">
        </div>
        
        <div class="col-md-8">
         <div class="card-body">
          <h5 class="card-title">USUARIO</h5>
          <p class="card-text">-Nombre Usuario: Sebastián Eliaz Torres Palma</p>
          <p class="card-text">-Carrera Profesinal: Analista Programador</p>
          <p class="card-text">-Institucion: Inacap</p>
        </div>
      </div>
  </div>
</div>

<br>

        <a class="btn btn-primary" href="/" role="button">Inicio</a>

    </body>
</html>
    """
    return HttpResponse(user)

def index(request):
    return render(request,'templatesApp/index.html')

def juguetes(request):
    return render(request,'templatesApp/juguetes.html')

def ropa(request):
    return render(request,'templatesApp/ropa.html')