#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new;
print $cgi->header("text/html");

# Obtén la matriz M ingresada en el formulario
my $matriz_input = $cgi->param("matriz");

# Divide la matriz en filas
my @filas = split /\n/, $matriz_input;

# Inicializa la variable para la posición potencial de la celebridad
my $posible_celebridad = 0;

# Itera a través de las filas para encontrar una posible celebridad
foreach my $fila (@filas) {
    my @conocimientos = split /,/, $fila;
    my $conoce_a = $conocimientos[$posible_celebridad];
    if ($conoce_a == 0) {
        $posible_celebridad++;
    }
}

# Verifica si la posible celebridad cumple con las condiciones
my $es_celebridad = 1;
foreach my $fila (@filas) {
    my @conocimientos = split /,/, $fila;
    my $conoce_a = $conocimientos[$posible_celebridad];
    if ($conoce_a == 1) {
        $es_celebridad = 0;
        last;
    }
}

if ($es_celebridad) {
    print "<h1>¡Hay una celebridad en la posición $posible_celebridad!</h1>";
} else {
    print "<h1>No se encontró una celebridad.</h1>";
}
