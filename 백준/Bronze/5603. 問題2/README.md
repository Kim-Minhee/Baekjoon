# [Bronze II] 問題2 - 5603 

[문제 링크](https://www.acmicpc.net/problem/5603) 

### 성능 요약

메모리: 33432 KB, 시간: 64 ms

### 분류

구현, 문자열

### 제출 일자

2025년 5월 9일 13:00:38

### 문제 설명

<p>0 から 9 までの数字だけで構成された文字列が与えられたとき，その文字列 から次の規則に従って新しい文字列を作る操作を考える．与えられた文字列を左端 から１文字ずつ順に読んで行き，同じ数字 a が r 個続いていた場合，個数 r と数字 a を空白で区切らずにこの順で書き出す．与えられた文字列の右端まで読み，最後 の書き出しが終わったところまでを途中何回書き出しがあったとしても全部まとめ て操作１回とカウントする．２回目以降の操作は前回の操作により書き出された文 字列を与えられた文字列として同様の操作を実施する．例えば “122244” という文 字列が与えられた場合には左端から順に１個の１， ３個の２，２個の４なのでこの 操作１回で得られる文字列は “113224” であり，“44444444444” （11 個の４）の場 合には得られる文字列は “114” となる．</p>

<p>100 文字以下の与えられた文字列に上の操作を n 回実施した文字列を出力するプ ログラムを作成せよ．ただし， n ≤ 20 とする．</p>

### 입력 

 <p>2 行からなり, 1 行目に操作回数 n, 2 行目に最初の文字列が書かれている．</p>

### 출력 

 <p>1 行であ り, 指定された回数の操作を施した文字列の後に改行を入れること.</p>

