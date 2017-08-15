function clear(){
		$("#username").val('');
		$("#password").val('');
}

$(function(){
		$("#error").hide();
		$("#b11").click(function(){
		var username = $("#username").val();
		var password = $("#password").val();
		if ( username == '') {
			$("#error").html("      please input username!");
			$("#error").show();
			clear();
			return false;
		}
		if ( password == '') {
			$("#error").html("      please input password!");
			$("#error").show();
			clear();
			return false;
		}
		$("#form").submit();
		})
})

	