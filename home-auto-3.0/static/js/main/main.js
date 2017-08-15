var device;
var value;
function init(){	
	$("#led_panel").hide();
	$("#data_panel").hide();
	$("#title_content").hide();
}


$(function(){
	init();
	$("#led1").click(function(){
		$("#title_content").show();
		$("#title_content").html('led1');
		$("#data_panel").hide();
		$("#led_panel").show();
		device = 'led1';
	})
	$("#led2").click(function(){
		$("#title_content").show();
		$("#title_content").html('led2');
		$("#data_panel").hide();
		$("#led_panel").show();
		device = 'led2';
	})
	$("#led3").click(function(){
		$("#title_content").show();
		$("#title_content").html('led3');
		$("#data_panel").hide();
		$("#led_panel").show();
		device = 'led3';
	})
	$("#sensor").click(function(){
		$("#title_content").show();
		$("#title_content").html('sensor');
		$("#led_panel").hide();
		$("#data_panel").show();
		device = 'sensor';
		$.post("/getSensorData", {value:-1,device:device}, function(data) {
		var info = 'Temperature: ' + data.temperature + '*C, ' + 'Humidity: ' + data.humidity + '%';
  			$("#data_info").html(info);
		});
	})


	$("#video").click(function(){
		$("#title_content").show();
		$("#title_content").html('video');
		$("#led_panel").hide();
		$("#data_panel").show();
		device = 'video';
		$.post("/getVideoIP", {value:-1,device:device}, function(data) {
			var text = "Here to see the video"
			var html_info = "<a href=\"http://" + data.ip + "/stream_simple.html\" target=\"_blank\">" + text + "</a>";
			console.log(html_info);
  			$("#data_info").html(html_info);
		});
	})
	$("#on").click(function(){
		value = 'on';
		$.post("/control", {value:value,device:device}, function(data) {

		});
	})
	$("#off").click(function(){
		value = 'off';
		$.post("/control", {value:value,device:device}, function(data) {
  			
		});
	})
})

