# @id: script_1774780995283_5btclav34
# @title: check disk
# @description: 

# Check disk space
# Alert if disk usage is above 90%

DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ $DISK_USAGE -gt 90 ]; then
    echo "Disk usage is ${DISK_USAGE}%" | mail -s "Disk Space Alert" admin@example.com
fi