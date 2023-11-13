#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new;
print $cgi->header("text/html");

# Obtén la cadena ingresada en el formulario
my $cadena = $cgi->param("cadena");

# Invierte la cadena utilizando un ciclo
my $cadena_invertida = "";
for (my $i = length($cadena) - 1; $i >= 0; $i--) {
    $cadena_invertida .= substr($cadena, $i, 1);
}

# Imprime la cadena invertida
print "<h1>Cadena Invertida: $cadena_invertida</h1>";

