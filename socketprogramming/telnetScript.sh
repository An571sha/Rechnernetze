HOST='asmtp.htwg-konstanz.de'
USER='cm5ldGlu'
PASSWD='bnRzbW9iaWw='
(
echo open "$HOST"
sleep 2
echo "$USER"
sleep 2
echo "$PASSWD"
sleep 2
echo "exit"
) | telnet
