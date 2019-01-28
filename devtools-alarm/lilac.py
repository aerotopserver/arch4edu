#!/bin/python3
from lilaclib import *

update_on = [{'github': 'archlinuxarm/PKGBUILDs', 'path': 'alarm/devtools-alarm'}]
build_prefix = 'extra-x86_64'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxarm/PKGBUILDs', 'alarm/devtools-alarm'])
    vcs_update()

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)