$( document ).ready(function() {
    $('#products_tbl').DataTable({
    	"pageLength": 6,
    });
    $('.chips').material_chip();
    $('.chips-placeholder').material_chip({
	    placeholder: 'Products tags.',
	    secondaryPlaceholder: '+Tag',
	  });
});

$(".delete_btn").click(function(){
  	var element = $(this);
  	var id = element.data("id");
  	$.ajax({
      url: '../delete/',
      type: 'POST',
      dataType: 'json',
		data: {
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
			id: id,
		},
      	beforeSend: function () {
      	},
      	success: function (response) {
			$('#'+id).remove();      		
      	}
    });

});

$( "#add_product_id" ).click(function() {
	if(my_functions.validate_empty()){
		tags_list = $('.chips').material_chip('data');
		tags_str = "";
		$.each(tags_list,function(key, value){
			tags_str += value.tag + ",";
		});
		$.ajax({
	      url: '../create/',
	      type: 'POST',
	      dataType: 'json',
			data: {
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
				product_name : $( "#product_name_id" ).val(),
			    product_description : $( "#product_description_id" ).val(),

			    product_tags : tags_str.substring(0,tags_str.length-1),
			    //photos : photos_list,
			},
	      	beforeSend: function () {
	        	console.log("se envian los datos");
	        	my_functions.clear_form();
	      	},
	      	success: function (response) {
	      		//console.log(response);
	      		var data = JSON.parse(response);
	        	my_functions.create_table(data);
	        	$("#similar_products_id").css("display", "block");
	        	$("#similar_products_id").click();
	      	}
	    });
	}
});
my_functions = {
	validate_empty : function(){
		product_name = $( "#product_name_id" ).val();
	    product_description = $( "#product_description_id" ).val();
	    if (product_name == "" || product_description == "" || $('.chips').material_chip('data').length == 0){
	    	return false;
	    }
	    return true;
	},
	clear_form : function () {
		// body...
		$( "#product_name_id" ).val("");
	    $( "#product_description_id" ).val("");
	    $('.chips').material_chip();
	    $('.chips-placeholder').material_chip({
		    placeholder: 'Products tags.',
		    secondaryPlaceholder: '+Tag',
		  });
		},
	create_table : function(data){
		table = '<table id="similar_products_datatbl" class="display" cellspacing="0" width="100%">';
		table += '<thead>';
        table +=  '<tr>';
        table +=      '<th>Product name</th>';
        table +=      '<th>Product description</th>';
        table +=      '<th>Product tags</th>';
        table +=      '<th>Creation date</th>';
        table +=  '</tr>';
        table += '</thead>';
        table += '<tbody>';
        for (var elem = 0; elem < data.length; elem ++){
        	table +=  '<tr id=' + data[elem].pk + '>';
	        table +=      '<td>' + data[elem].fields.product_name +'</th>';
	        table +=      '<td>' + data[elem].fields.product_description +'</th>';
	        table +=      '<td>' + data[elem].fields.product_tags +'</th>';
	        table +=      '<td>' + data[elem].fields.creation_date +'</th>';
	        table +=  '</tr>';
        }
        table += '</tbody>';
        table += '</table>';
        $("#similar_products_tbl").html(table);
        $('#similar_products_datatbl').DataTable();
	},
}