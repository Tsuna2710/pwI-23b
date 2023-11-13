#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl
use strict;
use warnings;
use CGI;

# Crear un objeto CGI para obtener los datos del formulario
my $cgi = CGI->new;

# Obtener la consulta de búsqueda del formulario
my $consulta = $cgi->param('q');

# Escapar la consulta de búsqueda para que sea segura en una URL
$consulta =~ s/ /+/g;  # Reemplazar espacios con +

# Construir la URL de búsqueda de Google
my $url = "https://www.google.com/search?q=$consulta";

# Imprimir una redirección para llevar al usuario a la página de resultados de Google
print $cgi->redirect(-url => $url);
