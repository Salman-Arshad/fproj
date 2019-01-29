$(document).ready(()=>{
    $("#code").click(()=>{
        console.log(code,ref)
        $.ajax({
            data:{
                code:$("#pycode").val(),
                ref:$("#ref").val(),
                fee:$("#fee").val(),
                invest:$("#invest").val()
            },
            type : 'POST',
            url : '',
            success:(data2)=>{
               //alert(JSON.parse(data2).output.toString("utf-8"))
               data2 = JSON.parse(data2)
               $("#out").val(data2.output)
               $("#err").val(data2.error)

            }
        })
    })
})
