function fillData() {
    let option = {
        title: {
            text: `中国疫情图 ${getTimeStr()}`,
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['中国疫情图']
        },
        visualMap: {
            type: 'piecewise',
            pieces: [
                { min: 1000, max: 1000000, label: '大于等于1000人', color: '#372a28' },
                { min: 500, max: 999, label: '确诊500-999人', color: '#4e160f' },
                { min: 100, max: 499, label: '确诊100-499人', color: '#974236' },
                { min: 10, max: 99, label: '确诊10-99人', color: '#ee7263' },
                { min: 1, max: 9, label: '确诊1-9人', color: '#f5bba7' },
            ],
            color: ['#E0022B', '#E09107', '#A3E00B']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        roamController: {
            show: true,
            left: 'right',
            mapTypeControl: {
                'china': true
            }
        },
        series: [
            {
                name: '确诊数',
                type: 'map',
                mapType: 'china',
                roam: false,
                label: {
                    show: true,
                    color: 'rgb(249, 249, 249)'
                },
                data: [{
                    name: '北京',
                    value: 942
                  }, {
                    name: '天津',
                    value: 270
                  }, {
                    name: '上海',
                    value: 1176
                  }, {
                    name: '重庆',
                    value: 589
                  }, {
                    name: '河北',
                    value: 373
                  }, {
                    name: '河南',
                    value: 1284
                  }, {
                    name: '云南',
                    value: 213
                  }, {
                    name: '辽宁',
                    value: 283
                  }, {
                    name: '黑龙江',
                    value: 949
                  }, {
                    name: '湖南',
                    value: 1020
                  }, {
                    name: '安徽',
                    value: 991
                  }, {
                    name: '山东',
                    value: 847
                  }, {
                    name: '新疆',
                    value: 953
                  }, {
                    name: '江苏',
                    value: 672
                  }, {
                    name: '浙江',
                    value: 1286
                  }, {
                    name: '江西',
                    value: 935
                  }, {
                    name: '湖北',
                    value: 68139
                  }, {
                    name: '广西',
                    value: 260
                  }, {
                    name: '甘肃',
                    value: 170
                  }, {
                    name: '山西',
                    value: 212
                  }, {
                    name: '内蒙古',
                    value: 288
                  }, {
                    name: '陕西',
                    value: 454
                  }, {
                    name: '吉林',
                    value: 157
                  }, {
                    name: '福建',
                    value: 436
                  }, {
                    name: '贵州',
                    value: 147
                  }, {
                    name: '广东',
                    value: 1919
                  }, {
                    name: '青海',
                    value: 18
                  }, {
                    name: '西藏',
                    value: 1
                  }, {
                    name: '四川',
                    value: 743
                  }, {
                    name: '宁夏',
                    value: 75
                  }, {
                    name: '海南',
                    value: 171
                  }, {
                    name: '台湾',
                    value: 555
                  }, {
                    name: '香港',
                    value: 5323
                  }, {
                    name: '澳门',
                    value: 46
                  }
                ]
            }
        ]
    };



    var url = `${getTimeStr()}.json`
    var request = new XMLHttpRequest();
    request.open("get", url);
    request.send(null);
    request.onload = function () {
        if (request.status == 200) {
            data = JSON.parse(request.responseText);
            for (let i = 0; i <= 33; i++) {
                let info = {
                    name: data["name"][i],
                    value: data["value"][i]
                }
                // option["series"][0]["data"][i]=info;
            }
        }
    }

    console.log(option);
    return option;
}

function getTimeStr() {
    let date = new Date();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (day >= 0 && day <= 9) {
        day = "0" + day;
    }
    let str = `${date.getFullYear()}-${month}-${day}`;
    return str;
}