### Mixed-Integer-Programming-Sudoku-Solver

A basic, but different implementation of a Sudoku Solver using Mixed-Integer-Programming.

Uses not-equal-to constraints instead of truth-value type of constraints that most examples on the internet use. Most datascience blogs simply paraphrase/refactor the code found on the
PuLP Sudoku documentation page. This uses a different, but equivalent, type of constraints that are not natively linear. The absolute difference is linearized using pair-wise
comparisons and a binary variable. 

It is less efficient than but, I believe it's more intuitive when coming from a Mathematical/Statistical Background instead of natively coming from a Programming background.
