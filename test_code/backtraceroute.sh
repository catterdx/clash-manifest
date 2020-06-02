mtrinstall()
{
    apt-get >/dev/null 2>&1
	[ $? -le '1' ] && ( apt-get update >/dev/null 2>&1 | apt-get -y mtr >/dev/null 2>&1 )
	yum >/dev/null 2>&1
	[ $? -le '1' ] && yum -y install mtr >/dev/null 2>&1
}
mtrback(){
    type mtr >/dev/null 2>&1 || mtrinstall 
	echo "===Test [$2] backtrace route ===" | tee -a ${dir}/$logfilename
	mtr -r --tcp -w -b -c 10 $1 | tee -a ${dir}/$logfilename
	echo -e "\n\n"
	echo -e "=== [$2] test done===\n\n" >> ${dir}/$logfilename

}

backtraceroute()
{
	next
        mtrback "59.175.206.86" "Wuhan CT"
	mtrback "111.48.26.136 " "Wuhan CM"
	mtrback "113.57.249.2 " "Wuhan CU"
        mtrback "113.59.224.1" "Beijing CT"
        mtrback "123.125.99.1" "Beijing CU"
        mtrback "211.136.25.153" "Beijing CM"
	mtrback "14.215.116.1" "Guangzhou CT"
        mtrback "122.13.195.129" "Guangzhou CU"
	mtrback "120.237.53.17" "Guangzhou CM"
	mtrback "58.32.0.1" "Shanghai CT"
	mtrback "223.166.94.126" "Shanghai CU"
	mtrback "221.183.55.22" "Shanghai CM"
}
