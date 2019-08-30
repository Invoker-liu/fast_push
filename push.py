import subprocess
import os


def git(*args):
    return subprocess.check_call(['git'] + list(args))


# 合并南昌GIT
os.chdir('D:/clone/ddp-decision-service')
git("status")
git("fetch", "upstream")
git("checkout", "master")
git("merge", "upstream/master")
git("push", "origin", "master")
