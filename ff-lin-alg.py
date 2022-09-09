"""ff-lin alg: ferry fast lin alg
A collection of org-mode shortcuts to speed up the creation of matrices (and other mathematical objects) with ~sympy~ + ~python~.

Transclusion Statement
#+transclude: [[file:./ff-lin-alg.py]]  :src python :rest ":session :exports none"

Sample Usage
------------

# #+begin_src python :session :results replace raw :exports none
    bas_mat_a = Matrix([[1,1,4],[-2,-1,-6],[2,2,9]])
    dl(bas_mat_a)
# #+end_src

# #+begin_src python :session :results replace raw :exports none
    mat_b = Matrix([[1,-1,2],[0,3,-11],[2,5,-22]])
    dl(mat_b.rref())
# #+end_src


# #+begin_src python :session :results replace raw :exports none
    temp = q1det.copy()
    temp.row_del(0)
    temp.col_del(0)
    det(latex(temp))
# #+end_src

"""

from sympy import * # wildcard import because we want to be able to access everything
from sympy.matrices import *
from sympy.abc import *
import numpy as np # this is imported for the user

def prettify(current: str):
    """Hand-made prettification function to make matrix output more digestible
    and editable. Only use if you intend to edit the output."""

    holder = """"""
    add_nl = False
    for (pos, char) in enumerate(current):
        if add_nl:
            holder += f"{char}\n"
            add_nl = False
        elif char == "}":
            holder += f"{char}\n "
        elif char == "\\":
            next = current[pos + 1]
            if next == "\\":
                add_nl = True
            holder += char
        else:
            holder += char

    return holder

def dl(s, p:bool=False, **kwargs):
    """Display line output.

    Parameters
    s: str
        input string
    p: bool
        whether to prettify or not
    kwargs
        additional args to pass to sympy.latex
    """

    tmp = latex(s, **kwargs)
    if p:
        tmp = prettify(tmp)
    return "\\[" + tmp + "\\]\n"

def il(s, p=False, **kwargs):
    """Inline output.

    Parameters
    s: str
        input string
    p: bool
        whether to prettify or not
    kwargs
        additional args to pass to sympy.latex
    """
    tmp = latex(s, **kwargs)
    if p:
        tmp = prettify(tmp)
    return "\\(" + tmp + "\\)"
