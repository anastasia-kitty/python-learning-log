# Daily Log - 2026-11-03

## Problem

Two Sum: given a list of integers and a target, return the indices of the
two numbers that add up to the target.

## First idea

Try every pair and check whether any pair adds up to the target.
(But this is very inefficient!)

## Final approach

A faster approach is to scan the list once. For each number, compute
`need = target - number`. If `need` is already in a hash map of numbers
we have seen, return the indices of `need` and the current number.
Otherwise, store the current number and its index in the map, then continue.

## Complexity

- Time: O(n), because each number is visited only once.
- Space: O(n), because the hash map may store up to n numbers.

## What I learned

A hash map can help me avoid checking every pair one by one.

## English words I used

- word or phrase: indices
- meaning: the plural of "index"
- example sentence: Return the indices of the two numbers.

## Next step

Learn more about hash maps.
