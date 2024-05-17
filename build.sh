rm -rf **/History &>/dev/null
rm -rf **/**/History &>/dev/null
rm -rf **/**/**/History &>/dev/null
rm -rf History &>/dev/null
rm -rf dist build &>/dev/null
python setup.py sdist --format=gztar bdist_wheel \
  && twine upload dist/* 

