from plasTeX.ConfigManager import *
from plasTeX.DOM import Node

def addConfig(config: ConfigManager):
    section = config.addSection('html5', 'Html5 renderer Options')

    section['extra-css'] = MultiStringOption(
        """ Extra css files to use """,
        options='--extra-css',
        default=[],
    )

    section['extra-js'] = MultiStringOption(
        """ Extra javascript files to use """,
        options='--extra-js',
        default=[],
    )

    section['theme-css'] = StringOption(
        """ Theme css file""",
        options='--theme-css',
        default='white',
    )

    section['use-theme-css'] = BooleanOption(
        """ Use theme css """,
        options='--use-theme-css !--no-theme-css',
        default=True,
    )

    section['use-theme-js'] = BooleanOption(
        """ Use theme javascript """,
        options='--use-theme-js !--no-theme-js',
        default=True,
    )

    section['display-toc'] = BooleanOption(
        """ Display table of contents on each page """,
        options='--display-toc !--no-display-toc',
        default=True,
    )

    section['localtoc-level'] = IntegerOption(
        """ Create local toc above this level """,
        options='--localtoc-level',
        default=Node.DOCUMENT_LEVEL-1,
    )

    section['breadcrumbs-level'] = IntegerOption(
        """ Create breadcrumbs from this level """,
        options='--breadcrumbs-level',
        default=10,
    )

    section['use-mathjax'] = BooleanOption(
        """ Use mathjax """,
        options='--use-mathjax !--no-mathjax',
        default=True,
    )

    section['mathjax-url'] = StringOption(
        """ Url of the MathJax lib """,
        options='--mathjax-url',
        default='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML',
    )

    section['mathjax-dollars'] = BooleanOption(
        """ Use single dollars as math delimiter for mathjax """,
        options='--dollars !--no-dollars',
        default=True,
    )

section['mathjax-url'] = StringOption(
    """ Url of the MathJax lib """,
    options='--mathjax-url',
    category='html5',
    default='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML',
)

section['mathjax-dollars'] = BooleanOption(
    """ Use single dollars as math delimiter for mathjax """,
    options='--dollars !--no-dollars',
    category='html5',
    default=False,
)

section['filters'] = MultiOption(
    """Comma separated list of commands to invoke on each output page.""",
    options='--filters',
    category='html5',
    default='',
)

section['tikz-compiler'] = StringOption(
    """ LaTeX compiler for TikZ pictures """,
    options='--tikz-compiler',
    category='html5',
    default='pdflatex',
)

section['tikz-converter'] = StringOption(
    """ PDF to SVG converter for tikz and tikz-cd """,
    options='--tikz-converter',
    category='html5',
    default='pdf2svg',
)

section['tikz-template'] = StringOption(
    """ Jinja2 template file for tikz """,
    options='--tikz-template',
    category='html5',
    default='',
)

section['tikz-cd-template'] = StringOption(
    """ Jinja2 template file for tikz-cd """,
    options='--tikz-cd-template',
    category='html5',
    default='',
)
