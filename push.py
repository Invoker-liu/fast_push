import subprocess
import os
import time


def git(*args):
    return subprocess.check_call(['git'] + list(args))


# git clone --bare http://XXX.git
# git push --mirror http://XXXXXcopy.git
# git remote add upstream http://XXX.git
# git fetch upstream
# git checkout master
# git merge upstream/master
# git push origin master
# 基于GitUpStream的功能对于GIT在本地进行一次转发,方便进行急速同步
def loop_git_check():
    while True:
        os.chdir('D:/clone/ddp-decision-service')
        git("status")
        git("fetch", "upstream")
        git("checkout", "develop")
        git("merge", "upstream/develop")
        git("push", "origin", "develop")
        time.sleep(5)


loop_git_check()
