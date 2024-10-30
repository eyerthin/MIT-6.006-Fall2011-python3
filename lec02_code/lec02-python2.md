这里是 python2 的输出结果

```bash
python2 docdist1.py docdist1.py docdist2.py
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         30677 function calls in 0.042 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
     8935    0.004    0.000    0.004    0.000 :0(append)
    12280    0.005    0.000    0.005    0.000 :0(isalnum)
     1621    0.001    0.000    0.001    0.000 :0(join)
     5801    0.002    0.000    0.002    0.000 :0(len)
     1621    0.001    0.000    0.001    0.000 :0(lower)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(range)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
        1    0.000    0.000    0.041    0.041 <string>:1(<module>)
        2    0.002    0.001    0.002    0.001 docdist1.py:112(insertion_sort)
        2    0.003    0.001    0.036    0.018 docdist1.py:134(word_frequencies_for_file)
        3    0.005    0.002    0.005    0.002 docdist1.py:152(inner_product)
        1    0.000    0.000    0.005    0.005 docdist1.py:167(vector_angle)
        1    0.000    0.000    0.041    0.041 docdist1.py:177(main)
        2    0.000    0.000    0.000    0.000 docdist1.py:40(read_file)
        2    0.001    0.000    0.026    0.013 docdist1.py:55(get_words_from_line_list)
      393    0.014    0.000    0.025    0.000 docdist1.py:67(get_words_from_string)
        2    0.004    0.002    0.004    0.002 docdist1.py:95(count_frequency)
        1    0.000    0.000    0.042    0.042 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist2.py docdist1.py docdist2.py        
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         31070 function calls in 0.040 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
     8935    0.003    0.000    0.003    0.000 :0(append)
      393    0.000    0.000    0.000    0.000 :0(extend)
    12280    0.005    0.000    0.005    0.000 :0(isalnum)
     1621    0.001    0.000    0.001    0.000 :0(join)
     5801    0.002    0.000    0.002    0.000 :0(len)
     1621    0.001    0.000    0.001    0.000 :0(lower)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(range)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
        2    0.002    0.001    0.002    0.001 docdist2.py:113(insertion_sort)
        2    0.003    0.001    0.034    0.017 docdist2.py:135(word_frequencies_for_file)
        3    0.004    0.001    0.004    0.001 docdist2.py:153(inner_product)
        1    0.000    0.000    0.004    0.004 docdist2.py:168(vector_angle)
        1    0.000    0.000    0.039    0.039 docdist2.py:178(main)
        2    0.000    0.000    0.000    0.000 docdist2.py:40(read_file)
        2    0.000    0.000    0.025    0.012 docdist2.py:55(get_words_from_line_list)
      393    0.013    0.000    0.024    0.000 docdist2.py:68(get_words_from_string)
        2    0.004    0.002    0.004    0.002 docdist2.py:96(count_frequency)
        1    0.000    0.000    0.040    0.040 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist3.py docdist1.py docdist2.py
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         32385 function calls in 0.041 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
     8935    0.004    0.000    0.004    0.000 :0(append)
      393    0.000    0.000    0.000    0.000 :0(extend)
    12280    0.005    0.000    0.005    0.000 :0(isalnum)
     1621    0.001    0.000    0.001    0.000 :0(join)
     7116    0.003    0.000    0.003    0.000 :0(len)
     1621    0.001    0.000    0.001    0.000 :0(lower)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(range)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
        1    0.000    0.000    0.040    0.040 <string>:1(<module>)
        2    0.003    0.001    0.003    0.001 docdist3.py:114(insertion_sort)
        2    0.003    0.001    0.038    0.019 docdist3.py:136(word_frequencies_for_file)
        3    0.001    0.000    0.001    0.000 docdist3.py:154(inner_product)
        1    0.000    0.000    0.001    0.001 docdist3.py:180(vector_angle)
        1    0.000    0.000    0.039    0.039 docdist3.py:190(main)
        2    0.000    0.000    0.000    0.000 docdist3.py:41(read_file)
        2    0.000    0.000    0.028    0.014 docdist3.py:56(get_words_from_line_list)
      393    0.014    0.000    0.027    0.000 docdist3.py:69(get_words_from_string)
        2    0.005    0.002    0.005    0.002 docdist3.py:97(count_frequency)
        1    0.000    0.000    0.041    0.041 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist4.py docdist1.py docdist2.py
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         31954 function calls in 0.035 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
     8502    0.004    0.000    0.004    0.000 :0(append)
      393    0.000    0.000    0.000    0.000 :0(extend)
    12280    0.005    0.000    0.005    0.000 :0(isalnum)
        2    0.000    0.000    0.000    0.000 :0(items)
     1621    0.001    0.000    0.001    0.000 :0(join)
     7116    0.003    0.000    0.003    0.000 :0(len)
     1621    0.001    0.000    0.001    0.000 :0(lower)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(range)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
        1    0.000    0.000    0.034    0.034 <string>:1(<module>)
        2    0.002    0.001    0.002    0.001 docdist4.py:111(insertion_sort)
        2    0.003    0.001    0.032    0.016 docdist4.py:133(word_frequencies_for_file)
        3    0.001    0.000    0.001    0.000 docdist4.py:151(inner_product)
        1    0.000    0.000    0.001    0.001 docdist4.py:177(vector_angle)
        1    0.000    0.000    0.034    0.034 docdist4.py:187(main)
        2    0.000    0.000    0.000    0.000 docdist4.py:40(read_file)
        2    0.001    0.000    0.027    0.013 docdist4.py:55(get_words_from_line_list)
      393    0.014    0.000    0.026    0.000 docdist4.py:68(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist4.py:96(count_frequency)
        1    0.000    0.000    0.035    0.035 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist5.py docdist1.py docdist2.py
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         2924 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
      393    0.000    0.000    0.000    0.000 :0(extend)
        2    0.000    0.000    0.000    0.000 :0(items)
     1324    0.000    0.000    0.000    0.000 :0(len)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(range)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
      393    0.000    0.000    0.000    0.000 :0(split)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
      393    0.000    0.000    0.000    0.000 :0(translate)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        2    0.002    0.001    0.002    0.001 docdist5.py:106(insertion_sort)
        2    0.003    0.001    0.007    0.003 docdist5.py:128(word_frequencies_for_file)
        3    0.001    0.000    0.001    0.000 docdist5.py:146(inner_product)
        1    0.000    0.000    0.001    0.001 docdist5.py:172(vector_angle)
        1    0.000    0.000    0.008    0.008 docdist5.py:182(main)
        2    0.000    0.000    0.000    0.000 docdist5.py:42(read_file)
        2    0.000    0.000    0.001    0.001 docdist5.py:57(get_words_from_line_list)
      393    0.000    0.000    0.001    0.000 docdist5.py:75(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist5.py:91(count_frequency)
        1    0.000    0.000    0.010    0.010 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist6.py docdist1.py docdist2.py
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         15470 function calls (14608 primitive calls) in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
     2823    0.001    0.000    0.001    0.000 :0(append)
      824    0.000    0.000    0.000    0.000 :0(extend)
        2    0.000    0.000    0.000    0.000 :0(items)
     9325    0.003    0.000    0.003    0.000 :0(len)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.002    0.002    0.002    0.002 :0(setprofile)
      393    0.000    0.000    0.000    0.000 :0(split)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
      393    0.000    0.000    0.000    0.000 :0(translate)
        1    0.000    0.000    0.017    0.017 <string>:1(<module>)
    864/2    0.002    0.000    0.011    0.005 docdist6.py:106(merge_sort)
      431    0.005    0.000    0.009    0.000 docdist6.py:118(merge)
        2    0.003    0.001    0.015    0.008 docdist6.py:160(word_frequencies_for_file)
        3    0.001    0.000    0.001    0.000 docdist6.py:178(inner_product)
        1    0.000    0.000    0.001    0.001 docdist6.py:204(vector_angle)
        1    0.000    0.000    0.017    0.017 docdist6.py:214(main)
        2    0.000    0.000    0.000    0.000 docdist6.py:42(read_file)
        2    0.000    0.000    0.001    0.001 docdist6.py:57(get_words_from_line_list)
      393    0.000    0.000    0.001    0.000 docdist6.py:75(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist6.py:91(count_frequency)
        1    0.000    0.000    0.018    0.018 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist7.py docdist1.py docdist2.py
File docdist1.py : 196 lines, 804 words, 213 distinct words
File docdist2.py : 197 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         1601 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
      393    0.000    0.000    0.000    0.000 :0(extend)
        7    0.000    0.000    0.000    0.000 :0(len)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(readlines)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
      393    0.000    0.000    0.000    0.000 :0(split)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
      393    0.000    0.000    0.000    0.000 :0(translate)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        2    0.003    0.001    0.005    0.002 docdist7.py:106(word_frequencies_for_file)
        3    0.000    0.000    0.000    0.000 docdist7.py:122(inner_product)
        1    0.000    0.000    0.000    0.000 docdist7.py:136(vector_angle)
        1    0.000    0.000    0.005    0.005 docdist7.py:146(main)
        2    0.000    0.000    0.000    0.000 docdist7.py:42(read_file)
        2    0.000    0.000    0.001    0.001 docdist7.py:57(get_words_from_line_list)
      393    0.000    0.000    0.001    0.000 docdist7.py:75(get_words_from_string)
        2    0.000    0.000    0.000    0.000 docdist7.py:91(count_frequency)
        1    0.000    0.000    0.006    0.006 profile:0(main())
        0    0.000             0.000          profile:0(profiler)


python2 docdist8.py docdist1.py docdist2.py
File docdist1.py : 6096 lines, 804 words, 213 distinct words
File docdist2.py : 6184 lines, 817 words, 220 distinct words
The distance between the documents is: 0.071452 (radians)
         33 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(acos)
        7    0.000    0.000    0.000    0.000 :0(len)
        2    0.000    0.000    0.000    0.000 :0(open)
        2    0.000    0.000    0.000    0.000 :0(read)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        2    0.000    0.000    0.000    0.000 :0(split)
        1    0.000    0.000    0.000    0.000 :0(sqrt)
        2    0.000    0.000    0.000    0.000 :0(translate)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        3    0.000    0.000    0.000    0.000 docdist8.py:106(inner_product)
        1    0.000    0.000    0.000    0.000 docdist8.py:120(vector_angle)
        1    0.000    0.000    0.003    0.003 docdist8.py:130(main)
        2    0.000    0.000    0.000    0.000 docdist8.py:42(read_file)
        2    0.000    0.000    0.000    0.000 docdist8.py:63(get_words_from_line_list)
        2    0.000    0.000    0.000    0.000 docdist8.py:75(count_frequency)
        2    0.002    0.001    0.003    0.002 docdist8.py:90(word_frequencies_for_file)
        1    0.000    0.000    0.005    0.005 profile:0(main())
        0    0.000             0.000          profile:0(profiler)
```
