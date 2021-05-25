#!/usr/bin/env python3

import argparse
import sys

HASHTAG_RELEASE = "#release"
HASHTAG_HIDE_CHANGELOG = "#hide"

tags = [HASHTAG_RELEASE, HASHTAG_HIDE_CHANGELOG]

def filter_out_tags(commit):
    for tag in tags:
        commit = commit.replace(tag, "")
    return commit

if __name__ == '__main__':
    commits = [line.strip() for line in sys.stdin]

    build_new = True if len(commits) > 0 and HASHTAG_RELEASE in commits[0] else False
    if not build_new:
        sys.exit(0)

    first_commit = True
    for commit in commits:
        # read commits till the last commit that is marked by `HASHTAG_RELEASE`
        if not first_commit and HASHTAG_RELEASE in commit:
            break
        if first_commit:
            first_commit = False
        if HASHTAG_HIDE_CHANGELOG not in commit:
            print(filter_out_tags(commit))
