# [Unrated] Hotfix - 32556 

[문제 링크](https://www.acmicpc.net/problem/32556) 

### 성능 요약

메모리: 1695060 KB, 시간: 23996 ms

### 분류

분류 없음

### 제출 일자

2025년 2월 3일 21:48:45

### 문제 설명

<p>In an earlier contest, contestants had to solve a simple problem. They were given a string and had to print each unique substring of it, along with the number of occurrences it had in the original string. For example <code>AB</code> would print <code>A 1 B 1 AB 1</code> and <code>AAA</code> would print <code>A 3 AA 2 AAA 1</code>.</p>

<p>When copying over this problem for reuse in this contest, several mistakes were made. The input constraints were changed significantly, making the problem absolutely impossible! Luckily this was partially cancelled out by the output validator being mangled as well. Now instead of checking for absolute correctness it only requires the number of occurrences of each character in the output to be correct. With a quick hotfix of applying run length encoding to the output, the problem was finally solvable again and the contest could continue on as planned. Right?</p>

### 입력 

 <p>The input contains a single string of length at least <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> and at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^6$</span></mjx-container>. It contains only ASCII upper and lower case characters. This string is then followed by a single newline character.</p>

### 출력 

 <p>For each non-whitespace character that appears a non-zero number of times in the output of the problem described above, print it along with its number of occurrences on a single line, separated by a space. Print the lines ordered by ascending values of the ASCII characters. </p>

