#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new;
print $cgi->header(-type => "text/html", -charset => "UTF-8");

# Obtén los números ingresados en el formulario
my $input = $cgi->param("numeros");

# Divide los números por comas y almacénalos en un arreglo
my @numeros = split /,/, $input;

# Inicializa la variable $mayor con el primer número del arreglo
my $mayor = $numeros[0];

# Encuentra el número mayor en el arreglo
foreach my $numero (@numeros) {
    if ($numero > $mayor) {
        $mayor = $numero;
    }
}

print <<ENDHTML;
<!DOCTYPE html>
<html>
<head>
    <title>Número Mayor</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
    <div class="container">
        <h1>El número mayor ingresado es: $mayor</h1>
    </div>
</body>
</html>
ENDHTML

