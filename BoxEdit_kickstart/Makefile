USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=BoxEdit_kickstart
PACKAGE_NAME=${TITLE}
REVERSE_DOMAIN=edu.whitby
PACKAGE_VERSION=1.0
PAYLOAD=\
	pack-Library-Management-scriptRunner-once-box-edit-2014-07-22

l_Library_Management: l_Library
	@sudo mkdir -p ${WORK_D}/Library/Management
	@sudo chown root:wheel ${WORK_D}/Library/Management
	@sudo chmod 755 ${WORK_D}/Library/Management

l_Library_Management_bin: l_Library_Management
	@sudo mkdir -p ${WORK_D}/Library/Management/bin
	@sudo chown root:wheel ${WORK_D}/Library/Management/bin
	@sudo chmod 755 ${WORK_D}/Library/Management/bin

l_Library_Management_scriptRunner: l_Library_Management
	@sudo mkdir -p ${WORK_D}/Library/Management/scriptRunner
	@sudo chown root:wheel ${WORK_D}/Library/Management/scriptRunner
	@sudo chmod 755 ${WORK_D}/Library/Management/scriptRunner

l_Library_Management_scriptRunner_once: l_Library_Management_scriptRunner
	@sudo mkdir -p ${WORK_D}/Library/Management/scriptRunner/once
	@sudo chown root:wheel ${WORK_D}/Library/Management/scriptRunner/once
	@sudo chmod 755 ${WORK_D}/Library/Management/scriptRunner/once

pack-Library-Management-scriptRunner-once-%: % l_Library_Management_scriptRunner_once
	@sudo ${INSTALL} -m 755 -g wheel -o root "${<}" ${WORK_D}/Library/Management/scriptRunner/once
