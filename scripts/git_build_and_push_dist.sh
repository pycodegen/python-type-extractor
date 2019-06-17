if [ "${GIT_BRANCH}" == "master" ] || [[ "${GIT_BRANCH}" == dist* ]]
then
  exit
fi
if [ "${GIT_BRANCH}" == "develop" ]
then
  git checkout master
else
  git checkout -b $'dist-'"$GIT_BRANCH"
fi
git checkout master
mkdir -p ~/.git && git config user.email "devdoomari@gmail.com" && git config user.name "devdoomari.circleci"
git merge -X theirs --no-edit $GIT_BRANCH

git add -f lib docs
git commit --allow-empty -m $'generated from:'"$GIT_COMMIT_HASH"$'\ntriggered by:'"$CI_USERNAME"$'\n[ci skip]'
git tag -a $'dist_'"$GIT_BRANCH"'_'"$CI_BUILD_NUM" -m "."
if [ "${GIT_BRANCH}" == "develop" ]
then
  git push --set-upstream origin master --force --follow-tags
else
  git push --set-upstream origin $'dist-'"$GIT_BRANCH" --force --follow-tags
fi