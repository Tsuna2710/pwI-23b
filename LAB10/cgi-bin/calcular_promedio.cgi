#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use List::Util qw(min max);

my $cgi = CGI->new;
print $cgi->header("text/html");

# Obtén las notas ingresadas en el formulario
my $notas_input = $cgi->param("notas");

# Divide las notas por comas y almacénalas en un arreglo
my @notas = split /,/, $notas_input;

# Imprime las notas antes de la transformación
print "<h1>Notas antes: " . join(", ", @notas) . "</h1>";

# Encuentra la peor nota utilizando la función min
my $peor_nota = min(@notas);

# Encuentra la mejor nota utilizando la función max
my $mejor_nota = max(@notas);

# Elimina la peor nota del arreglo
@notas = grep { $_ != $peor_nota } @notas;

# Duplica la mejor nota en el arreglo
push @notas, $mejor_nota;

# Calcula el promedio de las notas
my $promedio = 0;
$promedio += $_ foreach @notas;
$promedio /= scalar @notas;


# Imprime las notas después de la transformación
print "<h1>Notas después: " . join(", ", @notas) . "</h1>";

# Imprime el promedio resultante
print "<h1>Promedio resultante: $promedio</h1>";

