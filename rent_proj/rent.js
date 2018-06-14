   //加载地图
   var map = new AMap.Map("container", {
        resizeEnable: true,
        zoomEnable: true,
        center: [116.397428, 39.90923],
        zoom: 11
    });


    //var scale = new AMap.Scale();
    //添加标尺
    var scale = new AMap.Scale({
        visible: true
    }),
    map.addControl(scale);

    //公交到达圈对象
    var arrivalRange = new AMap.ArrivalRange();
    //经度，纬度，时间，通勤方式（默认是地铁+公交）
    var x, y, t, vehicle = "SUBWAY,BUS";
    //工作地点，工作标记
    var workAddress, workMarker;
    //房源标记队列
    var rentMarkerArray = [];
    //多边形队列，存储公交到达的计算结果
    var polygonArray = [];
    //路径规划
    var amapTransfer;

    //信息窗体对象，在房源标记被点击时弹出
    var infoWindow = new AMap.InfoWindow({
        offset: new AMap.Pixel(0, -30)
    });

    //地址自动补全的使用
    var auto = new AMap.Autocomplete({
        // 通过Id指定输入元素，工作地点自动补全
        input: "work-location"
    });

    //添加事件监听，在选择补完的地址后调用workLocationSelected
    AMap.event.addListener(auto, "select", workLocationSelected);


    function takeBus(radio) {
        vehicle = radio.value;
        loadWorkLocation()
    }

    function takeSubway(radio) {
        vehicle = radio.value;
        loadWorkLocation()
    }

    //导入文件信息
    function importRentInfo(fileInfo) {
        var file = fileInfo.files[0].name;
        loadRentLocationByFile(file);
    }

    function workLocationSelected(e) {
        //更新工作地点，加载公交到达圈
        workAddress = e.poi.name;
        loadWorkLocation();
    }

    //加载工作标记
    function loadWorkMarker(x, y, locationName) {
        workMarker = new AMap.Marker({
            map: map,
            title: locationName,
            icon: 'http://webapi.amap.com/theme/v1.3/markers/n/mark_r.png',
            position: [x, y]

        });
    }

    //在地图上绘制到达圈
    function loadWorkRange(x, y, t, color, v) {
        arrivalRange.search([x, y], t, function(status, result) {
            if (result.bounds) {
                for (var i = 0; i < result.bounds.length; i++) {
                    //新建多边形对象
                    var polygon = new AMap.Polygon({
                        map: map,
                        fillColor: color,
                        fillOpacity: "0.4",
                        strokeColor: color,
                        strokeOpacity: "0.8",
                        strokeWeight: 1
                    });
                    //得到到达圈的多边形路径
                    polygon.setPath(result.bounds[i]);
                    polygonArray.push(polygon);
                }
            }
        }, {
            policy: v
        });
    }

    function addMarkerByAddress(address) {
        var geocoder = new AMap.Geocoder({
            city: "北京",
            radius: 1000
        });
        geocoder.getLocation(address, function(status, result) {
            if (status === "complete" && result.info === 'OK') {
                var geocode = result.geocodes[0];
                rentMarker = new AMap.Marker({
                    map: map,
                    title: address,
                    icon: 'http://webapi.amap.com/theme/v1.3/markers/n/mark_b.png',
                    position: [geocode.location.getLng(), geocode.location.getLat()]
                });
                rentMarkerArray.push(rentMarker);

                rentMarker.content = "<div>房源：<a target = '_blank' href='http://bj.58.com/pinpaigongyu/?key=" + address + "'>" + address + "</a><div>"
                rentMarker.on('click', function(e) {
                    infoWindow.setContent(e.target.content);
                    infoWindow.open(map, e.target.getPosition());
                    if (amapTransfer) amapTransfer.clear();
                    amapTransfer = new AMap.Transfer({
                        map: map,
                        policy: AMap.TransferPolicy.LEAST_TIME,
                        city: "北京市",
                        panel: 'transfer-panel'
                    });
                    amapTransfer.search([{
                        keyword: workAddress
                    }, {
                        keyword: address
                    }], function(status, result) {})
                });
            }
        })
    }

    function delWorkLocation() {
        if (polygonArray) map.remove(polygonArray);
        if (workMarker) map.remove(workMarker);
        polygonArray = [];
    }

    function delRentLocation() {
        if (rentMarkerArray) map.remove(rentMarkerArray);
        rentMarkerArray = [];
    }

    function loadWorkLocation() {
        //首先清空地图上已有的到达圈
        delWorkLocation();
        var geocoder = new AMap.Geocoder({
            city: "北京",  //城市
            radius: 1000   //范围
        });

        //地理编码
        geocoder.getLocation(workAddress, function(status, result) {
            if (status === "complete" && result.info === 'OK') {
                var geocode = result.geocodes[0];
                x = geocode.location.getLng();
                y = geocode.location.getLat();
                //加载工作地点标记
                loadWorkMarker(x, y);
                //加载60分钟内工作地点到达圈
                loadWorkRange(x, y, 60, "#3f67a5", vehicle);
                //地图移动到工作地点的位置
                map.setZoomAndCenter(12, [x, y]);
            }
        })
    }

    function loadRentLocationByFile(fileName) {
        //先删除现有的房源标记
        delRentLocation();
        //所有的地点都记录在集合中
        var rent_locations = new Set();
        //jqury操作
        $.get(fileName, function(data) {
            data = data.split("\n");
            data.forEach(function(item, index) {
                rent_locations.add(item.split(",")[1]);
            });
            rent_locations.forEach(function(element, index) {
                //加上房源标记
                addMarkerByAddress(element);
            });
        });
    }
