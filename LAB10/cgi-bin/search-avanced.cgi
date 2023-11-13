#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl
use strict;
use warnings;
use CGI;

# Crear un objeto CGI para obtener los datos del formulario
my $cgi = CGI->new;

# Obtener los valores de los campos de búsqueda avanzada
my $todas_estas_palabras = $cgi->param('todas_estas_palabras');
my $frase_exacta = $cgi->param('frase_exacta');
my $ninguna_de_estas_palabras = $cgi->param('ninguna_de_estas_palabras');

# Escapar las consultas de búsqueda para que sean seguras en una URL
$todas_estas_palabras =~ s/ /+/g;
$frase_exacta =~ s/ /+/g;
$ninguna_de_estas_palabras =~ s/ /+/g;

# Construir la URL de búsqueda avanzada de Google
my $url = "https://www.google.com/search?q=$todas_estas_palabras";
$url .= "+%22$frase_exacta%22" if $frase_exacta;
$url .= "+-$ninguna_de_estas_palabras" if $ninguna_de_estas_palabras;

# Imprimir una redirección para llevar al usuario a la página de resultados de Google
print $cgi->redirect(-url => $url);
