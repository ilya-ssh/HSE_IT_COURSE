**Grep Exercises**  

1. Find all lines containing the word "quick" in file1.txt and save to quick.txt  
grep "quick" file1.txt > quick.txt  
2. Count the number of lines containing the word "the" (case-insensitive) in file1.txt and save to the_count.txt  
grep -i -c "the" file1.txt > the_count.txt (-i for insensitive and c for count)  
3. Find all lines that start with "The" in file1.txt and save to the.txt  
grep "^The" file1.txt > the.txt (using anchor)  
4. Find all lines containing either "fox" or "dog" in file1.txt and save to animals.txt  
grep -E "fox|dog" file1.txt > animals.txt (using posix regex "or" - | )  
5. Extract all timestamps from file2.txt and save to timestamps.txt  
grep -o '^[0-9\-]\{10\} [0-9:]\{8\}' file2.txt > timestamps.txt ( o matching the pattern - 10 symbols of numbers or "-" followed by 8 symbols of numbers or ":")  
6. Find all ERROR and WARNING messages in file2.txt and save to errors.txt  
grep -E "ERROR|WARNING" file2.txt > errors.txt (same as fox/dog)  