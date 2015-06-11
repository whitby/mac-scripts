PKGVERSION=0.4.0
PKGNAME=logstash_forwarder
PKGID=com.elastic.logstash-forwarder
all: clean build

clean:
	rm out/${PKGNAME}-${PKGVERSION}.pkg
build:
	pkgbuild --root pkgroot --identifier ${PKGID} --version ${PKGVERSION} --scripts scripts out/${PKGNAME}-${PKGVERSION}.pkg
