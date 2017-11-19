# !/bin/sh
#android:
#APP ID：3101819740	APP KEY：A88HI53BJKTV
#iOS:
#APP ID：3201776428	APP KEY：IPI3G1YN69CE

last_ds=`date -d "-1 day" +%Y%m%d`
curr_time=`date +"%Y-%m-%d_%H:%M:%S"`

domain='http://openapi.mta.qq.com'
os='android'
idx='10501,10502'
err_ty='1'
start_date=$last_ds
end_date=$last_ds
url='/ctr_crash_anal/get_err_list'
android_app_id='3101819740'
tmp_pull_data_from_cloud="/data/tss/instance/bdap_03/App/tmp/ctr_crash_anal_err_list_${curr_ds}"_$RANDOM".dat"

sign=`python /tmp/GenSign.py $os $idx $err_ty $start_date $end_date $url`
full_url="${domain}${url}?app_id=${android_app_id}&idx=${idx}&err_ty=${err_ty}&start_date=${start_date}&end_date=${end_date}&sign=${sign}"
echo $full_url
echo $tmp_pull_data_from_cloud
wget -t 5 -c --limit-rate=300k -O ${tmp_pull_data_from_cloud} ${full_url}

