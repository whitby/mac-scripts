PKGVERSION=1.0.2
PKGNAME=ssl_trust
PKGID=edu.whitby.internalca
all: clean build

clean:
	rm out/${PKGNAME}-${PKGVERSION}.pkg
build:
	pkgbuild --root pkgroot --identifier ${PKGID} --version ${PKGVERSION} --scripts scripts /tmp/${PKGNAME}-${PKGVERSION}.pkg
	productbuild --package /tmp/${PKGNAME}-${PKGVERSION}.pkg out/${PKGNAME}-${PKGVERSION}.pkg
	rm /tmp/${PKGNAME}-${PKGVERSION}.pkg
