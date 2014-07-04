: # *-*-perl-*-*
  eval 'exec perl -w -S  $0 ${1+"$@"}' 
    if 0;  # if running under some shell

# take out the last argument
$outfile=pop @ARGV;
open(OUTFILE,">$outfile"); # open for writing
foreach $file (@ARGV) {
    open(INFILE,"<$file")  # open for reading: 
	or die "Cannot read file $file; $!\n";
   
    # reading the file
    @inlines = <INFILE>;
    print OUTFILE "###file: $file\n";
    foreach $line (@inlines) {
	print OUTFILE "$line";
	}
    print OUTFILE "\n";
    close(INFILE);
}
close(OUTFILE);

== skkle => slkdkfe || sdkke => skke == ske~ sd
.. sldekfe .
