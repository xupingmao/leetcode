# Read from the file words.txt and output the word frequency list to stdout.

# tr 用来替换字符串
# tr -d string1 删除string1
# tr -s string1 string2 把string1替换成string2
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'

