$(document).ready(() => {
    $("#myModal").modal({
        keyboard: false,
        show:false
    });
    $("#myModal").modal("hide");
    $("#codeRun").modal({
        keyboard: false,
        show:false,
        backdrop:'static'
    });
    $("#codeRun").modal("hide");
    $("#code").click(() => {
        $("#codeRun").modal("show");
        $.ajax({
            data: {
                code: $("#pycode").val(),
                ref: $("#ref").val(),
                fee: $("#fee").val(),
                invest: $("#invest").val()
            },
            type: "POST",
            url: "",
            success: data2 => {
                setTimeout(() => {
                    $("#codeRun").modal("hide");
                }, 1000);
                console.log("success");
                
                data2 = JSON.parse(data2);
                $("#out").val(data2.output);
                $("#err").val(data2.error);
                $("#codeRun").modal("hide");
                d = new Date();
                $("#img").attr(
                    "src",
                    "static/" + data2.range + ".png" + "?v=" + d.getTime()
                );
                $("#codeRun").modal("hide");
            }
        });
    });
    $("#jj").click(() => {
        $("#myModal").modal("show");
    });
});
