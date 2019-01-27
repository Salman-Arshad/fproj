$(document).ready(()=>{
    $("#code").click(()=>{
        console.log(code,ref)
        $.ajax({
            data:{
                code:$("#pycode").val(),
                ref:$("#ref").val()
            },
            type : 'POST',
            url : '/',
            success:(data2)=>{
                
            }
        })
    })
})
