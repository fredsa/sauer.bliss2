#!/bin/bash
#
set -ue

VERSION=$(git log -1 --pretty=format:%h)
if [ -n "$(git status --porcelain)" ]
then
  VERSION="dirty-$VERSION"
fi

git status
echo
echo -e "Hit [ENTER] to continue: \c"
read

SCRIPTS_DIR=$( dirname $0 )
ROOT_DIR=$( dirname $SCRIPTS_DIR )

APPCFG="/fred/lib/sdk193vmruntime/appcfg.py -s preview.appengine.google.com"

echo -e "\n*** Rolling back any pending updates (just in case) ***\n"
$APPCFG --oauth2 rollback . $*

echo -e "\n*** DEPLOYING ***\n"
$APPCFG --oauth2 update --no_precompilation -V $VERSION . $*

echo -e "\n*** SETTING DEFAULT VERSION ***\n"
$APPCFG --oauth2 set_default_version -V $VERSION . $*
