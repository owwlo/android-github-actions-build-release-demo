# [Github Workflow to Build & Release Android App](https://github.com/owwlo/android-github-actions-build-release-demo)
This project all starts as I need some CI tooling to build and publish my personal Android for fun. Before crafting it, I did some research but hardly find any project satisfy my need enough. So, here we go...

## Features
- Whether making a new "Release" is controlled by hashtags embedded in the commit message
	- If a commit message contains `#release`, a new Action job will be kicked off: [example](https://github.com/owwlo/android-github-actions-build-release-demo/commit/86cb28057654ea1a00b847f6627827bc315bc3eb)
	- If `#hide` appears in the commit message, the commit message will be excluded from the changelog: [example](https://github.com/owwlo/android-github-actions-build-release-demo/commit/73b28d2b4913478e0cbd96656f28d834791dc629)
	- If you want to change the above behaviors or to add secret sauce, you can edit `scripts/filter_changelog.py`
- A changelog will be generated along with the "Release", the changelog starts from the last `#release` hashtag to the most recent one: [example](https://github.com/owwlo/android-github-actions-build-release-demo/releases)

## Adapt it into your Project
Easy! Follow these steps:
1. Have your Android App checked into your repo
_(assuming your project uses `./gradlew build` to build. wait... what?! you don't use `gradle`? alright, you can update the build instruction in the `Build Repo` step defined in `.github/workflows/main.yml`)_
2. Copy `.github/workflows/main.yml`, `scripts/filter_changelog.py` to your repo

Wa-lah! You are done! Try triggering your first build run by pushing a change with `#release` in its commit message! If everything works well, you will see: [example](https://github.com/owwlo/android-github-actions-build-release-demo/runs/2660848267?check_suite_focus=true)

## FAQs
**Q: My project doesn't use Gradle. Will this workflow work for me?**
A: No(sort of). You will have to update the build instruction that is defined in the `Build Repo` step in `.github/workflows/main.yml`

**Q: I hate the release naming `release.20210123_123456`, can I change it?**
A: Sorry bro, life isn't prefect, deal with it! ... kidding, the naming is defined as the `tag` field in the `Upload APKs to Release` step in `.github/workflows/main.yml`

**Q: Your changelog format s\*\*ks! How I can replace it with mine?**
A: Alright, update it in `scripts/filter_changelog.py`

## This Workflow is Inspired by...
- https://github.com/xxf098/shadowsocksr-v2ray-trojan-android/blob/xxf098/master/.github/workflows/main.yml
- https://github.com/AoEiuV020/FlutterDemo/blob/master/.github/workflows/main.yml
- https://github.community/t/set-output-truncates-multiline-strings/16852