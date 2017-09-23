
# Read from the file words.txt and output the word frequency list to stdout.

# tr 用来分隔字符串
# tr -d string1 使用string1分隔，并且删除string1
# tr -s string1 
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'

