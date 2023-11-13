#!"C:/Program Files/xampp/perl/bin/perl.exe"
use strict;
use CGI;
my $cgi = new CGI;
my $numero1 = $cgi->param('numero1');
my $numero2 = $cgi->param('numero2');
my $total = $numero1 + $numero2;
if($numero1 !~ /^[0-9]+$/ or $numero2 !~ /^[0-9]+$/)
{
print $cgi->header("text/html");
print 'Solo se aceptan numeros';
return;
}
else
{
print $cgi->header("text/html");
print 'El total es ... '.$total;
}
