#!/usr/local/bin/gosh --
(include "html.scm")
(print
header
(html
(string-append
(title "Chocola test page")
(body
(string-append
	(h1 "Chocola running!")(br)
	"This page is written with " (a "Chocola"
	"https://github.com/windymelt/chocola") "." (br)
	(h2 "What is Chocola?")(br)
	"Chocola is Scheme-based html vending machine." (br)
	(h3 "Features")
	(ul '("Written with Scheme" "So Smart" "So obvious"))
)
)
)
)
)
