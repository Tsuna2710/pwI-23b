#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;

my $expresion = $cgi->param('expresion');

my $resultado = evaluar_expresion($expresion);

if (defined $resultado) {
    print $cgi->header(-type => 'text/html');
    print "<html><head><title>Resultado</title></head><body>";
    print "<h1>Resultado:</h1>";
    print "<p>$expresion = $resultado</p>";
    print "</body></html>";
} else {
    print $cgi->header(-type => 'text/html', -status => '400 Bad Request');
    print "Error en la expresión matemática.";
}

sub evaluar_expresion {
    my ($expresion) = @_;

    $expresion =~ s/[^\d\+\-\*\/\(\)\.\s]//g;

    my $resultado = eval $expresion;
    return $resultado;
}
