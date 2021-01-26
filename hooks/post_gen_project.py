#!/usr/bin/env python3
import pathlib

if __name__=='__main__':
    temp_dir = pathlib.Path.cwd() / ".." / "{{cookiecutter.author}}__temp_dir"
    source = (temp_dir / "toolbox.yml").resolve()
    destination = pathlib.Path.cwd() / ".." / "toolbox.yml" 
    source.replace(destination)
    pathlib.Path.rmdir(temp_dir)
