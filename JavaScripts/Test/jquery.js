
const MyAPI =()=>{
    console.log("My all APIs")
    var requestOptions = {
                method: 'GET',
                redirect: 'follow'
              };
              
              fetch("https://cados.up.railway.app/advocates/", requestOptions)
                .then(response => response.json())
                .then(result => {
                    console.log(result.advocates)
                    $(document).ready(function () {
                        var table = $('#example').DataTable({
                            "data" :result.advocates,
                            "columns": [
                                { data: "profile_pic" , "render": function(data) {
                                    return "<a href='"+data+"'><img src='" + data + "' height='30' alt='Image'></a>";
                                  } },
                                { data: "name" },
                                { data: "username"},
                                { data: "twitter","render": function(data){
                                    return "<a href='"+data+"'>"+data+"</a> "
                                }  },
                                { data: "follower_count"}
                              ],
                            "processing": true,
                        })
                    });
                    
                })
                .catch(error => console.log('error', error))
        }

MyAPI()

//  This code for when we need seprate search box for colloems

// const MyAPI3 =()=>{
//     console.log("My all APIs")
//     var requestOptions = {
//                 method: 'GET',
//                 redirect: 'follow'
//               };
              
//               fetch("https://cados.up.railway.app/advocates/", requestOptions)
//                 .then(response => response.json())
//                 .then(result => {
//                     console.log(result.aaData)
//                     $(document).ready(function () {
                        
//                         $('#example thead th').each( function (i) {
//                             var title = $('#example thead th').eq( $(this).index() ).text();
//                             $(this).html( '<input type="text" class ="text-center" placeholder="'+title+'" data-index="'+i+'" />' );
//                         } );
                        
//                         var table = $('#example').DataTable({
//                             "data" :result.aaData,
//                             "columns": [
//                                 { data: "Validation" },
//                                 { data: "account_type" },
//                                 { data: "date" },
//                                 { data: "messege_stutes" },
//                                 { data: "messge_from" },
//                                 { data: "num" },
//                                 { data: "reply" },
//                                 { data: "reply_date_time" },
//                                 { data: "sended" }
//                               ],
//                             "ordering": false
//                         });

//                         // Filter event handler
//                             $( table.table().container()).on( 'keyup', 'thead input', function () {
//                                 table.column( $(this).data('index') ).search( this.value ).draw();} );
//                     });
                    
//                 })
//                 .catch(error => console.log('error', error))
//         }

// // MyAPI3()

