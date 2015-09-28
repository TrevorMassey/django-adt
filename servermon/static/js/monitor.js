var sent = document.getElementById("sent");
var rcvd = document.getElementById("rcvd");
var cpu = document.getElementById("cpu");

//swampdragon.onChannelMessage(function (channels, message) {
//    sent.innerText = message.data.kb_sent;
//    rcvd.innerText = message.data.kb_received;
//    cpu.innerText = message.data.cpu + '%';
//});

swampdragon.onChannelMessage(function (channels, data){

    console.info(data);

});


swampdragon.ready(function() {
    //swampdragon.subscribe('sys', 'sysinfo', null);
    var params = {
        auth: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsZXgiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImFsZXhAYi5jb20iLCJleHAiOjE0MzU1NjUxNzN9.LK14v9ca00kS8P2L_zNQ8Cb_yAB_dwhiDntcy9ccVTA"
    };
    swampdragon.subscribe('online-users', 'get_online_user_count', params);
});