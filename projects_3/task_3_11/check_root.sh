#!/bin/bash
check_root() {
	local user_ID=$EUID
	if [ $user_ID -ne 0 ]; then
		echo "*Предупреждение!!!*"
		return
	else
		echo "Вы - СУПЕР(пользователь)<3"
	fi
}
check_root
