#!/data/data/com.termux/files/usr/bin/python
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich import print
from sys import argv

exts = {
	"sh":"bash",
	"py":"python",
	"rb":"ruby",
	"go":"go",
	"html":"html",
	"js":"javascript",
	"md":"markdown",
}

fn = argv[-1]

try:
	fd = open(fn).read()
	lang = exts.get(fn.split(".")[-1])
	if lang == "markdown": exit(print(Markdown(fd)))
	if not lang:
		ln = fd.split("\n")[0]
		if ln.startswith("!#"):
			if " " in ln:
				lang = ln.split(" ")[-1]
			else:
				lang = ln.split("/")[-1]
	code = Syntax(fd, lang)
	print(code)
except Exception as e:
	print(f"[red]Error:[/red] {e}")
