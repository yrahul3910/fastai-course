#!/usr/bin/env python3

import nbformat, fire
from nbconvert.preprocessors import ExecuteProcessor


def run_notebook(path):
    nb = nbformat.read(open(path), as_version=nbformat.NO_CONVERT)
    ExecuteProcessor(timeout=600).preprocess(nb, {})
    print('done')


if __name__ == '__main__':
    fire.Fire(run_notebook)
