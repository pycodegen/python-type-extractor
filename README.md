# Python TypeExtractor

## similar to: 
 - Java's Annotation Processor
 - Kotlin Annotation Processor

## what it does:

Suppose you have a function like:

```Python
def func_with_tuple(input: Tuple[str, int]) -> Tuple[int, str]:
    return (input[1], input[0])
```

if you run process this function with
```Python
type_extractor = TypeExtractor()
type_extractor.add()(func_with_tuple)
```

you get a "runtime-type tree" like the following:

```Python
FunctionFound(
    name=t.func_with_tuple.__qualname__,
    module_name=module_name,
    params={
      'input': TupleFound([str, int]),
    },
    return_type=TupleFound([int, str]),
)
```


## things to do:
 - refactor stuff
   - move typescript-codegen part to outside repo
   - rename things: 'Found' --> 'Node'?
   - other refactoring on folder structure...
 - add 'life count' for options? 
 