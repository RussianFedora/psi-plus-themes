#! /bin/sh

rm -fr resources
git clone --depth 1 git://github.com/psi-plus/resources.git
rev=$(cd resources && git log -1 --pretty=%h themes)
pkgrev=$(date +%Y%m%d)git${rev}
psiver=0.15-${pkgrev}
tar -C resources/ -czf psi-plus-themes-${psiver}.tar.gz themes
