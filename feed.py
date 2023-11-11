Run git config user.name github-actions
  git config user.name github-actions
  git config user.email github-actions@github.com
  git add .
  git commit -m "Modified feed"
  git push
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.10.13/x64
    PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.10.13/x64/lib/pkgconfig
    Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.13/x64
    Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.13/x64
    Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.13/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.10.13/x64/lib
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Error: Process completed with exit code 1.
