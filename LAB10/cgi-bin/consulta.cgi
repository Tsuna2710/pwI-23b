#!"C:/Program Files/xampp/perl/bin/perl.exe"
#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use File::Slurp;

# Cabecera para indicar que se está generando contenido HTML
print "Content-type: text/html\n\n";

# Obtener datos del formulario
my $cgi = CGI->new;
my $nombre_universidad = $cgi->param("nombre_universidad");
my $periodo_licenciamiento = $cgi->param("periodo_licenciamiento");
my $departamento_local = $cgi->param("departamento_local");
my $denominacion_programa = $cgi->param("denominacion_programa");

# Procesar el archivo CSV
# (Sustituye 'archivo_universidades.csv' con el nombre de tu archivo)
my $csv_data = read_file('archivo_universidades.csv');

# Dividir las líneas del archivo CSV y almacenarlas en un array de hashes
my @data;
my @lines = split /\n/, $csv_data;
my $header = shift @lines;
my @headers = split /\|/, $header;

foreach my $line (@lines) {
    my @values = split /\|/, $line;
    my %row;
    @row{@headers} = map { $_ + 1 . '. ' . $values[$_] } 0..$#values;
    push @data, \%row;
}

# Utilizar expresiones regulares para buscar coincidencias
my $pattern = qr/$nombre_universidad.*$periodo_licenciamiento.*$departamento_local.*$denominacion_programa/i;

# Filtrar las coincidencias
my @matches = grep { join('', values %$_) =~ /$pattern/ } @data;

# Muestra los resultados
print "<h2>Resultados de la consulta:</h2>";
if (@matches) {
    foreach my $match (@matches) {
        print "<p>";
        foreach my $key (keys %$match) {
            print "<strong>$key:</strong> $match->{$key}<br>";
        }
        print "</p>";
    }
} else {
    print "<p>No se encontraron resultados.</p>";
}
 
