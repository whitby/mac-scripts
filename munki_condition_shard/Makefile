PKGNAME=munki_conditional_shard
PKGVERSION=1.0.0
PKGID=edu.whitby.munki_conditional_shard
all: clean build

clean:
	if [ -f out/${PKGNAME}-${PKGVERSION}.pkg ]; then rm out/${PKGNAME}-${PKGVERSION}.pkg; fi;

build: clean
	pkgbuild --root pkgroot --identifier ${PKGID} --version ${PKGVERSION} --scripts scripts out/${PKGNAME}-${PKGVERSION}.pkg
