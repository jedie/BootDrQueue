# coding: utf-8

# imports not really needed and just for the editor warning ;)
import os
from bootstrap_env.utils.bootstrap_install_pip import EnvSubprocess


def after_install(options, home_dir):
    # --- CUT here ---
    """
    called after virtualenv was created and pip/setuptools installed.
    Now we install DrQueue
    """
    env_subprocess = EnvSubprocess(home_dir) # from bootstrap_env.bootstrap_install_pip
    logfile = os.path.join(env_subprocess.abs_home_dir, "install.log")

    # First ensure that we use the last pip version:
    env_subprocess.call_env_pip(["install", "--log=%s" % logfile, "--upgrade", "pip"])


    # install DrQueueIPython from github (readonly) as editable
    cmd = ["install", "--log=%s" % logfile]
    cmd += ["-e", "git+https://github.com/kaazoo/DrQueueIPython.git#egg=DrQueueIPython"]

    env_subprocess.call_env_pip(cmd)

    print("\n")
    print("*"*79)
    print("* DrQueueIPython installed here:")
    print("\t%s" % home_dir)
    print("*"*79)
