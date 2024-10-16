def second_index(text, some_str):
    a_fstep = text.find(some_str)
    b_sstep = text.find(some_str, a_fstep+1 )
    if b_sstep == -1:
        return None
    else:
        return b_sstep


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')