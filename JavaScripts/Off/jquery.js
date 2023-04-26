
const MyAPI =()=>{
    console.log("My all APIs")
    var requestOptions = {
                method: 'POST',
                redirect: 'follow'
              };
              
              fetch("http://103.77.155.78:5000/result/6386d5914ec1da8ef7c3f382", requestOptions)
                .then(response => response.json())
                .then(result => {
                    console.log(result.aaData)
                    $(document).ready(function () {
                        var table = $('#example').DataTable({
                            "data" :result.aaData,
                            "columns": [
                                { data: "Validation" },
                                { data: "account_type" },
                                { data: "date" },
                                { data: "messege_stutes" },
                                { data: "messge_from" },
                                { data: "num" },
                                { data: "reply" },
                                { data: "reply_date_time" },
                                { data: "sended" }
                              ]

                        })
                    });
                    
                })
                .catch(error => console.log('error', error))
        }

MyAPI()



const MyAPI3 =()=>{
    console.log("My all APIs")
    var requestOptions = {
                method: 'POST',
                redirect: 'follow'
              };
              
              fetch("http://103.77.155.78:5000/result/6386d5914ec1da8ef7c3f382", requestOptions)
                .then(response => response.json())
                .then(result => {
                    console.log(result.aaData)
                    $(document).ready(function () {
                        
                        $('#example thead th').each( function (i) {
                            var title = $('#example thead th').eq( $(this).index() ).text();
                            $(this).html( '<input type="text" class ="text-center" placeholder="'+title+'" data-index="'+i+'" />' );
                        } );
                        
                        var table = $('#example').DataTable({
                            "data" :result.aaData,
                            "columns": [
                                { data: "Validation" },
                                { data: "account_type" },
                                { data: "date" },
                                { data: "messege_stutes" },
                                { data: "messge_from" },
                                { data: "num" },
                                { data: "reply" },
                                { data: "reply_date_time" },
                                { data: "sended" }
                              ],
                            "ordering": false
                        });

                        // Filter event handler
                            $( table.table().container()).on( 'keyup', 'thead input', function () {
                                table.column( $(this).data('index') ).search( this.value ).draw();} );
                    });
                    
                })
                .catch(error => console.log('error', error))
        }

// MyAPI3()

