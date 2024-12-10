# Python Function with Uncommon Zero Division Behavior

This repository demonstrates a Python function that exhibits unexpected behavior when dealing with zero division.  The function `function_with_uncommon_error` returns 0 instead of raising a `ZeroDivisionError` when both inputs are zero. This can lead to subtle and difficult-to-detect bugs.

The `bug.py` file contains the buggy function, while `bugSolution.py` provides a corrected version.

## Bug Description

The original function does not explicitly handle the case where both inputs are zero, leading to a return value of 0 instead of raising an error. This silent failure might go unnoticed and cause unexpected consequences in a larger program.

## Solution

The solution involves adding an explicit check for both inputs being zero and raising a `ZeroDivisionError` if this condition is met.
