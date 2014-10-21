#/usr/bin/perl

die "Usage: $0 file1 file2 ... archive\n" unless $#ARGV >= 1;

# Get file name of archive.
$archive = pop @ARGV;

open OUTFILE, ">$archive" or die "Can't open file for writing archive.";

while (@ARGV) {
  $file = shift @ARGV;
  open INFILE, "<$file" or die "Can't open $file for reading.";
  print OUTFILE "###file: " . $file ." \n"; print $OUTFILE, " \n";
  
  foreach (<INFILE>) {
    print OUTFILE $_;
  }
}