'''
Problem Statement:
Valentina is looking for a new game to play with her friends. She asks her mom Marcia for an idea. After a moment Marcia described to girls the following simple game.

Girls are divided into
n
n teams, indexed
1
1 through
n
n. Each girl chooses a lowercase letter, one of 'a' - 'z'. Of course, some girls can choose the same letter. Then, Marcia, as a judge, shows a string
s
s, consisting of lowercase letters. For each letter in
s
s, each girl with the same letter gets one point.

We define the score of a team as the total number of points of its members.

Your task is to find the winning team, determined according to the following rules:

The winning team is the one with the largest score.
In case of a tie between two or more teams, the one with the fewest members wins.
If there is still a tie between two or more teams then the one with the lowest index wins.
Given all the information about the game, find the index of the winning team.

Input format
The first line of the input contains one integer
T
T denoting the number of test cases.

The first line of each test case description contains an integer
n
n and a string
s
s denoting the number of teams and a string showed by Marcia.

The
i
i-th of the next
n
n lines contains one non-empty string containing letters chosen by girls in the
i
i-th team. The length of a string is equal to the number of members in a team.

All strings in the input consist of lowercase letters only.

Output format
For each test case, output a single line containing the 1-based index of the winning team.

Constraints
1
≤
T
≤
10
1≤T≤10
2
≤
n
≤
10
000
2≤n≤10000
1
≤
|
s
|
≤
100
000
1≤|s|≤100000
1
≤
size of a team
≤
10
1≤size of a team≤10
Subtasks
Extra constraints	Points	Which tests
n
,
|
s
|
≤
100
n,|s|≤100	40	1-4
no extra constraints	60	5-10
SAMPLE INPUT
3
2 qwopwasp
wdw
abco
5 eeeessaa
valentina
esta
jugando
con
marcia
5 ahi
valentina
esta
jugando
con
susamigas
SAMPLE OUTPUT
1
2
1
Explanation
In the first sample test case, there are
n
=
2
n=2 teams. The string showed by Marcia is
s
=
"qwopwasp"
s="qwopwasp". There are two letters 'w' in
s
s, so two points are given to every girl who has chosen a letter 'w'.

Team 1 has three members. Two of them has chosen a letter 'w', and the other one has chosen a letter 'd'. The two girls get two points each, but the other girl has zero points because a letter 'd' doesn't occur in
s
s at all. The score of team 1 is
2
+
2
=
4
2+2=4.

Team 2 has four members. A girl who has chosen a letter 'a' gets one point, and so does a girl who has chosen a letter 'o'. The score of team 2 is
1
+
1
=
2
1+1=2.

So, in the first sample test case there is no tie and team 1 clearly wins.

Stack Limit for C++ is 8MB. You are allowed to increase it in your code, e.g. using setrlimit().

Time Limit: 3.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Visual Basic
'''

# Write your code here
t=int(input())
while t:
    girls,x=[],[]
    n,s = map(str,input().split())
    s=list(s)
    n=int(n)
    for i in range(1,n+1):
        girls.append(input())
    count=0
    for i in range(0,n):
        for j in girls[i]:
            if j in s:
                count+=1
        x.append(count)

    ma=max(x)
    print(ma)
    t=t-1
