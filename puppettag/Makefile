USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
TITLE=puppet_tag_${TAG}
PACKAGE_VERSION=1.0.0
REVERSE_DOMAIN=edu.whitby
PAYLOAD= \
pack-script-preinstall \
pack-custom-fact

l_etc:
	@sudo mkdir -p ${WORK_D}/etc
	@sudo chown root:wheel ${WORK_D}/etc
	@sudo chmod 755 ${WORK_D}/etc

l_etc_facter: l_etc
	@sudo mkdir -p ${WORK_D}/etc/facter
	@sudo chown root:wheel ${WORK_D}/etc/facter
	@sudo chmod 755 ${WORK_D}/etc/facter

l_etc_facter_facts_d: l_etc_facter
	@sudo mkdir -p ${WORK_D}/etc/facter/facts.d
	@sudo chown root:wheel ${WORK_D}/etc/facter/facts.d
	@sudo chmod 755 ${WORK_D}/etc/facter/facts.d

pack-custom-fact: l_etc_facter_facts_d
	@sudo echo "role=${TAG}" > ./hardware_tag.txt
	@sudo cp ./hardware_tag.txt ${WORK_D}/etc/facter/facts.d/
	@sudo chown root:wheel ${WORK_D}/etc/facter/facts.d/hardware_tag.txt
	@sudo chmod 755 ${WORK_D}/etc/facter/facts.d/hardware_tag.txt

