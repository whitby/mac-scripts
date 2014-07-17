USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
TITLE=puppetrepo
PACKAGE_VERSION=3.0.0
REVERSE_DOMAIN=edu.whitby
PAYLOAD= \
pack-script-postinstall \
pack-environments \
pack-hieradata

l_etc:
	@sudo mkdir -p ${WORK_D}/etc
	@sudo chown root:wheel ${WORK_D}/etc
	@sudo chmod 755 ${WORK_D}/etc

l_etc_puppet: l_etc
	@sudo mkdir -p ${WORK_D}/etc/puppet
	@sudo chown puppet:puppet ${WORK_D}/etc/puppet
	@sudo chmod 755 ${WORK_D}/etc/puppet

pack-environments: l_etc_puppet
	@sudo cp -R ./environments /etc/puppet/
	@sudo chown -R puppet:puppet ${WORK_D}/etc/puppet/
	@sudo chmod -R 755 ${WORK_D}/etc/puppet

pack-hieradata: l_etc_puppet
	@sudo cp -R ./hieradata /etc/puppet/
	@sudo chown -R puppet:puppet ${WORK_D}/etc/puppet/
	@sudo chmod -R 755 ${WORK_D}/etc/puppet
