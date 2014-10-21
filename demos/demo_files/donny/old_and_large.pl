:
  eval 'exec perl -w -S $0 ${1+"$@"}'
  if 0;

use File::Find;
use File::Path;
use File::Copy;

#See if there is an commandline argument:
die "Usage: $0 Mb days dirtree [-move] \n" unless $#ARGV>1;

($size, $days, $dirtree, $move)=@ARGV;

if ($move) {
    $trash='/home/ilmarw/inf3330/Perl/tmp/trash/';
    chdir($trash) or mkpath('tmp/trash/');
    chdir('/home/ilmarw/inf3330/Perl'); #Back to original directory
}

#Function to find the appropriate files and move them if -move is chosen:
sub findfiles {
    $file=$_;
    if (-f $file) {
 	$fsize= (-s $file)/1000000.0;
	$fdays= -A $file;
 	if ($fsize > $size && $fdays > $days) {
	    printf "%s %.2fMb %.0f\n", $file, $fsize, $fdays;
	    if ($move) {
		move($file, "$trash$file");
		print "File is moved\n";
	    }
 	}
    }
}

#Call the function:
find(\&findfiles, $dirtree);

# ilmarw@linux:~/inf3330/Perl> fakefiletree.py tree
#   file: ./tmpf-897206 8915Kb
#   file: ./tmpf-695022 1066Kb
#   file: ./tmpf-665838 1340Kb
# moved to /home/ilmarw/inf3330/Perl/tree
# generated 3 files and 1 directories
# ilmarw@linux:~/inf3330/Perl> old_and_large.pl 2 200 tree/ -move
# tmpf-897206 8.91Mb 246
# File is moved
# ilmarw@linux:~/inf3330/Perl>
