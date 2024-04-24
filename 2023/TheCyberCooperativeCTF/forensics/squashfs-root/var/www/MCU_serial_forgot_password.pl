#!/usr/bin/perl

use POSIX qw(strftime);

local ($buffer, @pairs, $pair, $name, $value, %FORM);
# Read in text
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "GET") {
   $buffer = $ENV{'QUERY_STRING'};
}

# Split information into name/value pairs
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
   ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}

$timestamp = strftime("%j%m%H%M%Y", localtime);

print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<title>Secure Router</title>";
print "</head>";
print "<body>";
print "<form method='POST' action='MCU_check_serial.pl?id=$timestamp'>";
print "<p>Router Serial Number:</p>";
print "<input type='text' name='serial'>";
print "<br>";
print "<br>";
print "<input type='submit'>";
print "</form>";
print "</body>";
print "</html>";
