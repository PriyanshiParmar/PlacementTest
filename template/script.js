$(document).ready(function(){
    console.log("Hii");
	
    var element = $("#html-content-holder"); // global variable
    var getCanvas; // global variable
     
        $("#btn-Preview-Image").on('click', function () {
            console.log("Hello");
             html2canvas(element, {
             onrendered: function (canvas) {
                    $("#previewImage").append(canvas);
                    getCanvas = canvas;
                    console.log("getCanvas");
                 }
             });
        });
    
        $("#btn-Convert-Html2Image").on('click', function () {
        var imgageData = getCanvas.toDataURL("image/png");
        // Now browser starts downloading it instead of just showing it
        var newData = imgageData.replace(/^data:image\/png/, "data:application/octet-stream");
        $("#btn-Convert-Html2Image").attr("download", "your_pic_name.png").attr("href", newData);
        });
    
    });