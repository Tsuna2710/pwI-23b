#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl
use strict;
use warnings;
use CGI;

# Crear un objeto CGI para obtener los datos del formulario
my $cgi = CGI->new;
print $cgi->header;

# Obtener la expresión matemática del formulario
my $expresion = $cgi->param('expresion');

# Utilizar expresiones regulares para analizar la expresión
if ($expresion =~ /^([-+]?[0-9]*\.?[0-9]+)\s*([-+*\/])\s*([-+]?[0-9]*\.?[0-9]+)$/) {
    my $operando1 = $1;
    my $operador = $2;
    my $operando2 = $3;
    my $resultado;

    if ($operador eq '+') {
        $resultado = $operando1 + $operando2;
    } elsif ($operador eq '-') {
        $resultado = $operando1 - $operando2;
    } elsif ($operador eq '*') {
        $resultado = $operando1 * $operando2;
    } elsif ($operador eq '/') {
        $resultado = $operando1 / $operando2;
    }

    print "<h2>Resultado: $resultado</h2>";
} else {
    print "<h2>Error: Expresión no válida</h2>";
}
