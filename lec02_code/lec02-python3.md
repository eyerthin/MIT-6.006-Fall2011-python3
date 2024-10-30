这里是python3版本的输出结果

```bash
python .\docdist1-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         30698 function calls in 0.024 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
        2    0.003    0.001    0.003    0.001 docdist1-py3.py:111(insertion_sort)
        2    0.000    0.000    0.019    0.009 docdist1-py3.py:130(word_frequencies_for_file)
        3    0.005    0.002    0.005    0.002 docdist1-py3.py:145(inner_product)
        1    0.000    0.000    0.005    0.005 docdist1-py3.py:159(vector_angle)
        1    0.000    0.000    0.024    0.024 docdist1-py3.py:167(main)
        2    0.000    0.000    0.000    0.000 docdist1-py3.py:40(read_file)
        2    0.001    0.000    0.010    0.005 docdist1-py3.py:56(get_words_from_line_list)
      393    0.005    0.000    0.010    0.000 docdist1-py3.py:67(get_words_from_string)
        2    0.004    0.002    0.005    0.002 docdist1-py3.py:93(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
     5801    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     8935    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12280    0.002    0.000    0.002    0.000 {method 'isalnum' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}

python .\docdist2-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         31091 function calls in 0.024 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
        2    0.003    0.001    0.003    0.001 docdist2-py3.py:113(insertion_sort)
        2    0.000    0.000    0.019    0.010 docdist2-py3.py:132(word_frequencies_for_file)
        3    0.005    0.002    0.005    0.002 docdist2-py3.py:147(inner_product)
        1    0.000    0.000    0.005    0.005 docdist2-py3.py:161(vector_angle)
        1    0.000    0.000    0.024    0.024 docdist2-py3.py:169(main)
        2    0.000    0.000    0.000    0.000 docdist2-py3.py:40(read_file)
        2    0.000    0.000    0.010    0.005 docdist2-py3.py:56(get_words_from_line_list)
      393    0.005    0.000    0.010    0.000 docdist2-py3.py:69(get_words_from_string)
        2    0.005    0.002    0.005    0.002 docdist2-py3.py:95(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
     5801    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     8935    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      393    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
    12280    0.002    0.000    0.002    0.000 {method 'isalnum' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}


python .\docdist3-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         32406 function calls in 0.020 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        2    0.003    0.001    0.003    0.001 docdist3-py3.py:114(insertion_sort)
        2    0.000    0.000    0.019    0.010 docdist3-py3.py:133(word_frequencies_for_file)
        3    0.000    0.000    0.001    0.000 docdist3-py3.py:148(inner_product)
        1    0.000    0.000    0.001    0.001 docdist3-py3.py:174(vector_angle)
        1    0.000    0.000    0.020    0.020 docdist3-py3.py:182(main)
        2    0.000    0.000    0.001    0.000 docdist3-py3.py:41(read_file)
        2    0.000    0.000    0.010    0.005 docdist3-py3.py:57(get_words_from_line_list)
      393    0.005    0.000    0.010    0.000 docdist3-py3.py:70(get_words_from_string)
        2    0.005    0.002    0.005    0.002 docdist3-py3.py:96(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
     7116    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     8935    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      393    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
    12280    0.002    0.000    0.002    0.000 {method 'isalnum' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}


python .\docdist4-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         30660 function calls in 0.015 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
        2    0.003    0.001    0.003    0.001 docdist4-py3.py:112(insertion_sort)
        2    0.000    0.000    0.015    0.007 docdist4-py3.py:135(word_frequencies_for_file)
        3    0.000    0.000    0.000    0.000 docdist4-py3.py:150(inner_product)
        1    0.000    0.000    0.000    0.000 docdist4-py3.py:169(vector_angle)
        1    0.000    0.000    0.015    0.015 docdist4-py3.py:177(main)
        2    0.000    0.000    0.001    0.000 docdist4-py3.py:41(read_file)
        2    0.000    0.000    0.010    0.005 docdist4-py3.py:57(get_words_from_line_list)
      393    0.005    0.000    0.010    0.000 docdist4-py3.py:70(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist4-py3.py:96(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
     5801    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     8502    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      393    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
    12280    0.002    0.000    0.002    0.000 {method 'isalnum' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
     1621    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
     1621    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}


python .\docdist5-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         1630 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        2    0.003    0.001    0.003    0.001 docdist5-py3.py:107(insertion_sort)
        2    0.000    0.000    0.006    0.003 docdist5-py3.py:130(word_frequencies_for_file)
        3    0.000    0.000    0.000    0.000 docdist5-py3.py:145(inner_product)
        1    0.000    0.000    0.000    0.000 docdist5-py3.py:164(vector_angle)
        1    0.000    0.000    0.006    0.006 docdist5-py3.py:172(main)
        2    0.000    0.000    0.001    0.000 docdist5-py3.py:43(read_file)
        2    0.000    0.000    0.001    0.001 docdist5-py3.py:59(get_words_from_line_list)
      393    0.000    0.000    0.001    0.000 docdist5-py3.py:77(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist5-py3.py:91(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      393    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      393    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
      393    0.001    0.000    0.001    0.000 {method 'translate' of 'str' objects}


python .\docdist6-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         13986 function calls (13124 primitive calls) in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
    864/2    0.001    0.000    0.004    0.002 docdist6-py3.py:109(merge_sort)
      431    0.002    0.000    0.003    0.000 docdist6-py3.py:122(merge)
        2    0.000    0.000    0.007    0.003 docdist6-py3.py:165(word_frequencies_for_file)
        3    0.000    0.000    0.000    0.000 docdist6-py3.py:181(inner_product)
        1    0.000    0.000    0.000    0.000 docdist6-py3.py:200(vector_angle)
        1    0.000    0.000    0.007    0.007 docdist6-py3.py:208(main)
        2    0.000    0.000    0.000    0.000 docdist6-py3.py:43(read_file)
        2    0.000    0.000    0.001    0.001 docdist6-py3.py:59(get_words_from_line_list)
      393    0.000    0.000    0.001    0.000 docdist6-py3.py:77(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist6-py3.py:91(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
     7881    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     2760    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      824    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      393    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
      393    0.001    0.000    0.001    0.000 {method 'translate' of 'str' objects}


python .\docdist7-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：196
单词数量：804
词频表长度：213
文件docdist2.py:
行数：197
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         1624 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        4    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        2    0.000    0.000    0.003    0.001 docdist7-py3.py:107(word_frequencies_for_file)
        3    0.000    0.000    0.000    0.000 docdist7-py3.py:122(inner_product)
        1    0.000    0.000    0.000    0.000 docdist7-py3.py:137(vector_angle)
        1    0.000    0.000    0.003    0.003 docdist7-py3.py:145(main)
        2    0.000    0.000    0.001    0.000 docdist7-py3.py:43(read_file)
        2    0.000    0.000    0.001    0.001 docdist7-py3.py:59(get_words_from_line_list)
      393    0.000    0.000    0.001    0.000 docdist7-py3.py:77(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist7-py3.py:91(count_frequency)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      393    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      393    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
      393    0.001    0.000    0.001    0.000 {method 'translate' of 'str' objects}


python .\docdist8-py3.py docdist1.py docdist2.py
文件docdist1.py:
行数：6096
单词数量：804
词频表长度：213
文件docdist2.py:
行数：6184
单词数量：817
词频表长度：220
两个文档间的文本相似度为：0.071452(弧度单位)
         52 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        2    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        3    0.000    0.000    0.000    0.000 docdist8-py3.py:110(inner_product)
        1    0.000    0.000    0.000    0.000 docdist8-py3.py:125(vector_angle)
        1    0.000    0.000    0.002    0.002 docdist8-py3.py:133(main)
        2    0.000    0.000    0.001    0.000 docdist8-py3.py:43(read_file)
        2    0.000    0.000    0.000    0.000 docdist8-py3.py:65(get_words_from_line_list)
        2    0.000    0.000    0.000    0.000 docdist8-py3.py:79(count_frequency)
        2    0.000    0.000    0.002    0.001 docdist8-py3.py:95(word_frequencies_for_file)
        2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {built-in method _io.open}
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.acos}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        2    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'str' objects}
```