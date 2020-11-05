#インターネットの無尽蔵から株価データを持ってきて、会社別CSVにする
import datetime
import locale
import requests
import os
import time
import codecs
import zipfile
from plyer import notification

dataZipFilePath = 'h:/stockdata/zip/'
dataCsvFilePath = 'h:/stockdata/csv/'
#base_url_zip = "http://mujinzou.com/d_data/2020d/20_01d/T200106.zip"
base_url = 'http://mujinzou.com/d_data/'
dt = datetime.datetime(2020, 1, 6)

for x in range(366):
    dtd = dt + datetime.timedelta(days=x)

    if dtd.weekday() < 5 :

        sdata = dtd.strftime("%y-%m-%d")
        year, month, day = sdata.split('-')
        filename= "T{0}{1}{2}.zip".format(year, month, day)
        download_url = base_url + "20" + year + "d/"+year +"_"+month+"d/"+filename
        
        filePath = os.path.join(dataZipFilePath, filename)

        response = requests.get(download_url)

        if response.status_code != 200:
            print("dame")
        else:
            with codecs.open(filePath, 'wb', encoding=None) as f:
                f.write(response.content)


        if os.path.exists(os.path.join(dataZipFilePath,filename)):
            with zipfile.ZipFile(os.path.join(dataZipFilePath, filename)) as zf:
                zf.extractall(dataCsvFilePath)

    if dtd == datetime.datetime.today():
        break

notification.notify(
    title='１番ゲート通過',
    message='無尽蔵からデータゲット展開終了',
    app_name='アプリ名だよ',
    #app_icon='./icon.jpg'
)