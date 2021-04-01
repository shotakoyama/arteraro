# utilaĵo

## progress

This command shows progress bar for standard input.

```
cat a.txt | progress > /dev/null
```

## m2_to_src

This command extracts source sentences from m2 file.

## m2_to_trg

This command extracts target sentneces from m2 file.
You can set coder as `m2_to_trg --coder 0 < hoge.m2`.
Default coder is 0.

## remove_identical

This command removes identical source target sentence pairs.

```
remove_identical source_input_path target_input_path source_output_path target_output_path
```

