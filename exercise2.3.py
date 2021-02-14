#You can set the Load limit as per your requirement
HIGHLIMIT=15
LOWLIMIT=5
loadavg=`uptime | awk ‘{print $9}’`
if [ “$loadavg” = “average:” ]
then
echo “not this one…”
loadavg=`uptime | awk ‘{print $10}’`
fi
#RESTARTCOMMAND=”/sbin/service httpd restart”
#STOPCOMMAND=”/sbin/service httpd stop”
RESTARTCOMMAND=”/scripts/restartsrv_httpd”
STOPCOMMAND=”/sbin/service httpd stop”
thisloadavg=`echo $loadavg|awk -F \. ‘{print $1}’`
if [ “$thisloadavg” -ge “$HIGHLIMIT” ]; then
echo “Busy – Load Average $loadavg ($thisloadavg) ”
#stop apache
$STOPCOMMAND
elif [ “$thisloadavg” -le “$LOWLIMIT” ]; then
echo “Okay – Load Average $loadavg ($thisloadavg) ”
pgrep httpd
if [ $? -ne 0 ] # if apache not running
then
$RESTARTCOMMAND
echo “restart!”
else
echo “no restart!”
fi
else
echo “waiting…!”
fi