USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
PACKAGE_VERSION=0.0.1
TITLE=munki_postflight
PACKAGE_NAME=munki_postflight
REVERSE_DOMAIN=edu.whitby
PAYLOAD=\
	pack-postflight
	
pack-postflight: l_usr_local
	@sudo mkdir -p ${WORK_D}/usr/local/munki
	@sudo ${INSTALL} -m 755 -g wheel -o root postflight ${WORK_D}/usr/local/munki/

