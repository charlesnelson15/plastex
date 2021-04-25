# plastex

Read more at the github page for the plasTeX project:  http://plastex.github.io/plastex/

Installation of this package is done just like any other Python package.
See the INSTALL file for details.

Once you have plasTeX installed, you can use the command-line utility,
called "plastex" just like latex or pdflatex.  For example, if you
have a LaTeX file called mybook.tex, simple run:

```
plastex mybook.tex
```

This will convert mybook.tex into XHTML (the default renderer).  Of course,
there are many options to control the execution of plastex.  Simply type
"plastex" on the command line without options or arguments to see the
full list of command-line options.

It is also possible to write your own command-line utilities that leverage
the power of the plasTeX framework.  In fact, the essence of the "plastex"
command can be written in just one line of code (not including the Python
import commands):

```
import sys
from plasTeX.TeX import TeX
from plasTeX.Renderers.XHTML import Renderer
Renderer().render(TeX(file=sys.argv[1]).parse())
```

plasTeX is really much more than just a LaTeX-to-other-format converter 
though.  See the documentation at http://plastex.github.io/plastex/ for a complete
view of what it is capable of.

## Testing
To run the tests locally, run tox.
This will run tests locally using python 3.5 to 3.8.

## Status
[![Build Status](https://github.com/plastex/plastex/workflows/tests/badge.svg)](https://github.com/plastex/plastex/actions)
[![Coverage Status](https://coveralls.io/repos/github/plastex/plastex/badge.svg?branch=master)](https://coveralls.io/github/plastex/plastex?branch=master)

Documentation for Gerby (a fork of plasTeX, to be used for large online mathematical texts with stable cross-referencing) is available at the [Gerby project page](https://gerby-project.github.io).
