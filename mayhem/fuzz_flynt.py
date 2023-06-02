#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports(include=['flynt']):
    from flynt.lexer import split
    from flynt.static_join.transformer import transform_join
    from flynt.string_concat.transformer import transform_concat

ctr = 0
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    choice = fdp.ConsumeIntInRange(0, 2)
    global ctr
    ctr += 1
    try:
        if choice == 0:
            split.get_fstringify_chunks(fdp.ConsumeRemainingString())
        elif choice == 1:
            transform_join(fdp.ConsumeRemainingString())
        elif choice == 2:
            transform_concat(fdp.ConsumeRemainingString())
    except (ValueError):
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
