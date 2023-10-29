#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new;
print $cgi->header(-type => "text/html", -charset => "UTF-8");

# Obtén el nombre ingresado en el formulario
my $nombre = $cgi->param("nombre");

print <<ENDHTML;
<!DOCTYPE html>
<html>
<head>
    <title>Bienvenido</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
    <div class="container">
        <h1>Hola, $nombre. ¡Bienvenido!</h1>
    </div>
</body>
</html>
ENDHTML
