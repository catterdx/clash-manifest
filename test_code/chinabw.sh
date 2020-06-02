cbw()
{

    arch=$( uname -m )
    wget --no-check-certificate https://bintray.com/ookla/download/download_file?file_path=ookla-speedtest-1.0.0-${arch}-linux.tgz -O speedtest.tgz 1>/dev/null 2>&1
    tar xfvz speedtest.tgz >/dev/null 2>&1
    chmod +x speedtest
    bd=`./speedtest --accept-license -s $1 2>/dev/null | awk -F '(' '{print $1}'`

	#获得相关数据
    latency=`echo "$bd" | awk -F ':' '/Latency/{print $2}'`
	download=`echo "$bd" | awk -F ':' '/Download/{print $2}'`
	upload=`echo "$bd" | awk -F ':' '/Upload/{print $2}'`

	#显示在屏幕上
    if [ -n "$latency" ]
    then
        printf "%-18s%-18s%-20s%-12s\n" "$2" "$upload" "$download" "$latency"
        #写入日志文件
	    echo "$2|$upload|$download|$latency">>${dir}/$logfilename
    fi


}
chinabw()
{
    next
    echo "=== CN bandwidth test ===">>${dir}/$logfilename
    printf "%-18s%-18s%-20s%-12s\n" " Node Name" "Upload Speed" "Download Speed" "Latency"
    cbw '3633' 'Shanghai CT'
    cbw '27377' 'Beijing CT 5G'
    cbw '23844' 'Wuhan CT'
    cbw '27594' 'Guangzhou CT 5G'
    cbw '21005' 'Shanghai CU'
    cbw '5145' 'Beijing CU'
    cbw '5485' 'Wuhan CU'
    cbw '26678' 'Guangzhou CU 5G'
    cbw '25637' 'Shanghai CM动5G'
    cbw '25858' 'Beijing CM'
    cbw '26547' 'Wuhan CM'
    cbw '6611' 'Guangzhou CM'
    echo -e "=== Done ==\n\n">>${dir}/$logfilename
}

