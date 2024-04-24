#!/usr/bin/perl

use POSIX qw(strftime);

local ($buffer, @pairs, $pair, $name, $value, %FORM);
# Read in text
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "GET") {
   $buffer = $ENV{'QUERY_STRING'};
    # Split information into name/value pairs
    @pairs = split(/&/, $buffer);

    foreach $pair (@pairs) {
       ($name, $value) = split(/=/, $pair);
       $value =~ tr/+/ /;
       $value =~ s/%(..)/pack("C", hex($1))/eg;
       $FORM{$name} = $value;
    }
}


if ($ENV{'REQUEST_METHOD'} eq "POST") {
   $buffer = $ENV{'QUERY_STRING'};
    # Split information into name/value pairs
    @pairs = split(/&/, $buffer);

    foreach $pair (@pairs) {
       ($name, $value) = split(/=/, $pair);
       $value =~ tr/+/ /;
       $value =~ s/%(..)/pack("C", hex($1))/eg;
       $FORM{$name} = $value;
    }

    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $FORM{$name} = $value;
    }
}

$timestamp = strftime("%j%m%H%M%Y", localtime);

open(FH,"username.txt") or &dienice("Can't open username.txt: $!");
$username = <FH>;
close(FH);

open(FH,"password.txt") or &dienice("Can't open password.txt: $!");
$password = <FH>;
close(FH);

print "Content-type:text/html\r\n\r\n";

if ($FORM{id} ne $timestamp){
    print "<html>";
    print "<head>";
    print "<title>Secure Router</title>";
    print "</head>";
    print "<body>";
    print "<center><p>Sorry, your timestamp nonce has expired</p></center>";
    print "</body>";
    print "</html>";
    exit 0;
}

print "<html>";
print "<head>";
print "<title>Secure Router</title>";
print "</head>";
print "<body>";
print "<p>Password recovered</p>";
print "<p>$username</p>";
print "<p>$password</p>";
print "</body>";
print "</html>";
