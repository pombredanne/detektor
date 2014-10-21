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


#----------------------Running example---------------------

# ribera: uke7>ls
# caseinsensitive_sort.pl  pack.pl            test       unpack.pl
# findprograms.pl          rename.pl          test1.txt  yeah2
# old_and_large.pl         simviz1_Getopt.pl  test2.txt

# ribera: uke7>more test1.txt 
# dette er en test

# ribera: uke7>more test2.txt 
# testing

# ribera: uke7>pack.pl test1.txt test2.txt res.dat

# ribera: uke7>ls
# caseinsensitive_sort.pl  pack.pl    simviz1_Getopt.pl  test2.txt
# findprograms.pl          rename.pl  test               unpack.pl
# old_and_large.pl         res.dat    test1.txt          yeah2

# ribera: uke7>more res.dat 
# ###file: test1.txt
# dette er en test
# ###file: test2.txt
# testing
