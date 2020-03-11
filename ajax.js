var estado="0";
var luzestado="desligado";
$(function(){
$("#frente").click(function(){
	window.estado=1;
    
});

$("#esquerda").click(function(){
	window.estado=2;

    
});

$("#direita").click(function(){
	window.estado=3;

});

$("#re").click(function(){
	window.estado=4;

});

$("#panico").click(function(){
	window.estado=0;

 });
$("#lpd").click(function() {
	window.estado=45;
	window.luzestado="desligado";
});
$("#lpl").click(function() {
	window.estado=44;
	window.luzestado="ligado";
});
$(this).click(function(){
   	 console.log("estado: "+ estado);
	 console.log("luz: " + luzestado);
	$.ajax({
		data:{valor_estado: estado},
		url:'script.php',
		type:'POST',
		success: function(response){
            	//alert(response);
		console.log(response);
		}
	});
});
});
