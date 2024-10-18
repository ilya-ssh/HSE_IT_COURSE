**Sed Exercises**  

1. Replace all occurrences of "quick" with "swift" in file1.txt inplace  
sed -i 's/quick/swift/g' file1.txt (i flag for inplace s for substitution; g for all lines)  
2. Delete all lines containing the word "dog" in file1.txt inplace and save the backup to a file with .orig extension  
sed -i.orig '/dog/d' file1.txt (deleting lines with d; -i editing inplace and saving backup specified after dot)  