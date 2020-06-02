#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
export PATH

next() {
    printf "%-70s\n" "-" | sed 's/\s/-/g'
}


echo "（host provider）[default:Enter]"
read hostp
echo "wait…………"


_included_benchmarks=""
upfile="y"


#取参数
while getopts "i:u" opt; do
    case $opt in
        i) _included_benchmarks=$OPTARG;;
		u) upfile="n";;
    esac
done

#默认参数
if [ "$_included_benchmarks" == "" ]; then
	_included_benchmarks="io,bandwidth,download,traceroute,backtraceroute,allping"
fi

_included_benchmarks="systeminfo,"${_included_benchmarks}


#要用到的变量
backtime=`date +%Y%m%d`
logfilename="91yuntest.log"
dir=`pwd`
IP=$(curl -s myip.ipip.net | awk -F ' ' '{print $2}' | awk -F '：' '{print $2}')
echo "==== collect information ====">${dir}/$logfilename

#创建测试目录
rm -rf ${dir}/91test
mkdir -p 91test
cd 91test

clear

#取得测试的参数值
arr=(${_included_benchmarks//,/ })    

#下载执行相应的代码
for i in ${arr[@]}    
do 
	wget -q --no-check-certificate https://raw.githubusercontent.com/catterdx/91test/master/test_code/${i}.sh
    . ${dir}/91test/${i}.sh
	eval ${i}
done    


#上传文件
updatefile()
{
	resultstr=$(curl -s -T ${dir}/$logfilename "http://logfileupload.91yuntest.com/logfileupload.php")
	echo -e $resultstr | tee -a ${dir}/$logfilename
}

if [[ $upfile == "y" ]]
then
	updatefile
else
	echo "log update to 91yuntest.log"
fi
#删除目录
rm -rf ${dir}/91yuntest

