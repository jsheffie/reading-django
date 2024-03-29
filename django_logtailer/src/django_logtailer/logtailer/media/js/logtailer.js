/*
 * Logtailer object
 */

var LogTailer = {
	timeout_id: null,
	timeout: 2000,
	scroll: true,
	file_id: 0,
}

LogTailer.getLines = function (){
	LogTailer.currentScrollPosition = django.jQuery("#log-window").scrollTop();
	django.jQuery.ajax({
	  url: "../../get-log-line/"+LogTailer.file_id,
	  success: function(result){
	  				LogTailer.printLines(result);
	  		   },
	  dataType: "json",
	});

}

LogTailer.printLines = function(result){
	if(django.jQuery("#apply-filter").is(':checked')){
		for(var i=0;i<result.length;i++){
			pattern = django.jQuery("#filter").val();
			if(django.jQuery('#filter-select').val()!="custom"){
				pattern = django.jQuery('#filter-select').val();
			}
			try {
			    regex = eval(pattern);
			}
			catch(err) {
			    regex = pattern;
			}
			position = result[i].search(regex);
			if(position>-1){
				django.jQuery("#log-window").append(result[i]);
			}
		}		
	}
	else{
		for(var i=0;i<result.length;i++){
			if(result[i].length>0){
				django.jQuery("#log-window").append(result[i]);
			}
		}
	}
	if(LogTailer.scroll){
		django.jQuery("#log-window").scrollTop(django.jQuery("#log-window")[0].scrollHeight - django.jQuery("#log-window").height());
	}
	else{
		django.jQuery("#log-window").scrollTop(LogTailer.currentScrollPosition);
	}
	LogTailer.timeout_id = window.setTimeout("LogTailer.getLines("+LogTailer.file_id+")", LogTailer.timeout);
}

LogTailer.startReading = function (){
	LogTailer.timeout_id = window.setTimeout("LogTailer.getLines("+LogTailer.file_id+")", LogTailer.timeout);
	django.jQuery("#start-button").hide();
	django.jQuery("#stop-button").show();
}

LogTailer.stopReading = function (){
	window.clearTimeout(LogTailer.timeout_id);
	django.jQuery("#stop-button").hide();
	django.jQuery("#start-button").show();
}


LogTailer.changeAutoScroll = function(){
	if(LogTailer.scroll){
      	LogTailer.scroll = false;
      	django.jQuery('#auto-scroll').val("OFF");
      	django.jQuery('#auto-scroll').css('color', 'red');
    }
    else{
      	LogTailer.scroll = true;
      	django.jQuery('#auto-scroll').val("ON");
      	django.jQuery('#auto-scroll').css('color', 'green');
    }
}

LogTailer.customFilter = function(){
	if(django.jQuery('#filter-select').val()=="custom"){
	    django.jQuery('#filter').show();
	}
	else{
		django.jQuery('#filter').hide();
	}
}
