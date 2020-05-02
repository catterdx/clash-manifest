mtrinstall()
{
    apt-get >/dev/null 2>&1
	[ $? -le '1' ] && ( apt-get update >/dev/null 2>&1 | apt-get -y mtr >/dev/null 2>&1 )
	yum >/dev/null 2>&1
	[ $? -le '1' ] && yum -y install mtr >/dev/null 2>&1
}
mtrback(){
    type mtr >/dev/null 2>&1 || mtrinstall 
	echo "===测试 [$2] 的回程路由===" | tee -a ${dir}/$logfilename
	mtr -r --tcp -w -b -c 10 $1 | tee -a ${dir}/$logfilename
	echo -e "\n\n"
	echo -e "===回程 [$2] 路由测试结束===\n\n" >> ${dir}/$logfilename

}

backtraceroute()
{
	next
        mtrback "59.175.206.86" "武汉电信"
	mtrback "111.48.26.136 " "武汉移动"
	mtrback "113.57.249.2 " "武汉联通"
	mtrback "115.231.219.181" "泉州电信"
	mtrback "180.97.193.88" "江苏常州电信"
        mtrback "115.231.219.159" "浙江绍兴电信"
        mtrback "223.111.183.89" "江苏常州移动"
        mtrback "112.84.104.172" "江苏徐州联通"
	mtrback "103.36.209.82" "浙江杭州联通"
	mtrback "218.98.26.190" "江苏常州联通"
}
