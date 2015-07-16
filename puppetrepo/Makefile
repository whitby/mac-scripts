USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
TITLE=puppetrepo
PACKAGE_VERSION=3.3.8
REVERSE_DOMAIN=edu.whitby
PAYLOAD= \
pack-script-postinstall \
pack-environments \
pack-hieradata \
pack-Library-LaunchDaemons-edu.whitby.puppet.schedule.plist

l_etc:
	@sudo mkdir -p ${WORK_D}/etc
	@sudo chown root:wheel ${WORK_D}/etc
	@sudo chmod 755 ${WORK_D}/etc

l_etc_puppet: l_etc
	@sudo mkdir -p ${WORK_D}/etc/puppet
	@sudo chown puppet:puppet ${WORK_D}/etc/puppet
	@sudo chmod 755 ${WORK_D}/etc/puppet

pack-environments: l_etc_puppet
	@sudo cp -R ./environments ${WORK_D}/etc/puppet/
	@sudo chown -R puppet:puppet ${WORK_D}/etc/puppet/
	@sudo chmod -R 755 ${WORK_D}/etc/puppet

pack-hieradata: l_etc_puppet
	@sudo cp -R ./hieradata ${WORK_D}/etc/puppet/
	@sudo chown -R puppet:puppet ${WORK_D}/etc/puppet/
	@sudo chmod -R 755 ${WORK_D}/etc/puppet
