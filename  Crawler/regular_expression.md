Regular Expression

aa*    a occurs at least once.
bbbbb  b occurs five times.
(cc)*  c occurs any even numbers.
(d|)   d and space follow or just space follows.


[A-Za-z0-9\._+]+:     The part of email address contains at least: capital, minuscules, 
		  Numbers between 0 and 9, '.', '+', and '_'

[A-Za-z]+:      Character occurs at least once.

\.       :      As escape character must be used.

(com|org|edu|net): One of four addresses.

[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)

*:	Occurs at least 0 time.
+:	Occurs at least 1 time.
[]:	Any one in [].
():	Priority.
{m, n}:	Characters between m and n, both boundaries included.
[^]:	Any not in [].
^:	Match character after ^.
$:	Match the end.
?1:	Not contains.